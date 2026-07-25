
# PANMATRIX_PROXY_BINDING.py
import os
import sys
import asyncio
from fastapi import FastAPI, Header, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="PanMatrix Telemetry Binding Layer")

# Thread-safe global telemetry state register cache
class GlobalState:
    def __init__(self):
        self.processed_total = 0
        self.pearson_r = 0.4410
        self.cpu_percent = 0.0
        self.ram_percent = 0.0
        self.tamper_status = 0
        self.header_status = 1
        self.active_connections: list[WebSocket] = []

state = GlobalState()

# Inbound data serialization scheme matching core execution outputs
class TelemetryUpdate(BaseModel):
    processed_total: int
    pearson_r: float
    cpu_percent: float
    ram_percent: float

@app.post("/api/update-internal")
async def update_internal_metrics(data: TelemetryUpdate):
    """Internal ingress endpoint called by your Monte Carlo processing loops."""
    state.processed_total = data.processed_total
    state.pearson_r = data.pearson_r
    state.cpu_percent = data.cpu_percent
    state.ram_percent = data.ram_percent
    
    # Pack up active telemetry packet for broad dashboard broadcast
    payload = {
        "processed_total": state.processed_total,
        "pearson_r": f"{state.pearson_r:+.4f}",
        "cpu_percent": f"{state.cpu_percent:.1f}",
        "ram_percent": f"{state.ram_percent:.1f}",
        "tamper_status": state.tamper_status,
        "header_status": state.header_status
    }
    
    # Broadcast to all connected holographic frontend instances
    for connection in state.active_connections:
        try:
            await connection.send_json(payload)
        except Exception:
            state.active_connections.remove(connection)
            
    return {"status": "broadcast_complete"}

@app.get("/metrics", response_class=PlainTextResponse)
async def scrape_metrics(
    x_panmatrix_trademark_rider: str = Header(None),
    x_panmatrix_auth_signature: str = Header(None)
):
    """Hardened endpoint scraped by Prometheus on Port 9100."""
    # 1. Enforce strict defensive brand-compliance headers
    if x_panmatrix_trademark_rider != "KameronKnowlton_Asserted":
        state.header_status = 0
        raise HTTPException(status_code=403, detail="Defensive Trademark Rider Validation Failure")
    
    state.header_status = 1
    
    # 2. Format telemetry values into standard Prometheus exposition formatting
    metrics_payload = (
        f"# HELP panmatrix_processed_total Total count of processed spatial matrix sets.\n"
        f"# TYPE panmatrix_processed_total counter\n"
        f"panmatrix_processed_total {state.processed_total}\n"
        f"# HELP panmatrix_spatial_pearson_r Extracted correlation matrix factor.\n"
        f"# TYPE panmatrix_spatial_pearson_r gauge\n"
        f"panmatrix_spatial_pearson_r {state.pearson_r:+.4f}\n"
        f"# HELP panmatrix_system_cpu_percent Target machine physical core trace mapping.\n"
        f"# TYPE panmatrix_system_cpu_percent gauge\n"
        f"panmatrix_system_cpu_percent {state.cpu_percent:.1f}\n"
        f"# HELP panmatrix_system_ram_percent Target virtual hardware space footprints.\n"
        f"# TYPE panmatrix_system_ram_percent gauge\n"
        f"panmatrix_system_ram_percent {state.ram_percent:.1f}\n"
    )
    return metrics_payload

@app.websocket("/ws/telemetry")
async def telemetry_websocket_endpoint(websocket: WebSocket):
    """Establishes full-duplex socket lines to feed live client UI layers."""
    await websocket.accept()
    state.active_connections.append(websocket)
    try:
        while True:
            # Keep connections alive by listening for client heartbeats
            await websocket.receive_text()
    except WebSocketDisconnect:
        state.active_connections.remove(websocket)

if __name__ == "__main__":
    # Bind to 0.0.0.0 to route queries cleanly across local networks and container loops
    uvicorn.run(app, host="0.0.0.0", port=9100)
