#!/bin/bash
# PanMatrix Pipeline One-Click Orchestration Launcher

# Get the directory where this script is located
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$PROJECT_DIR"

echo "===================================================="
echo "🌌 INITIALIZING PANMATRIX TELEMETRY PIPELINE GRID"
echo "===================================================="

# Check if Docker engine is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Error: Docker Desktop is not running. Please start Docker first."
    exit 1
fi

echo "[*] Cleaning legacy caching blocks and orphaned assets..."
docker compose down --remove-orphans > /dev/null 2>&1

echo "[*] Spinning up all infrastructure containers in detached mode..."
if docker compose up -d --build; then
    echo "===================================================="
    echo "🚀 DEPLOYMENT SUCCESSFUL // TELEMETRY GRID IS LIVE"
    echo "===================================================="
    echo "• Dashboard Interface : Open or double-click 'dashboard.html'"
    echo "• Prometheus Matrix   : http://localhost:9090"
    echo "• Raw Metrics Stream  : http://localhost:9100/metrics"
    echo "===================================================="
    echo "[*] Streaming live core processing loops (Press Ctrl+C to stop trailing logs)..."
    echo ""
    docker compose logs -f panmatrix-core
else
    echo "❌ Critical Failure: Docker Compose build system encountered errors."
    exit 1
fi
