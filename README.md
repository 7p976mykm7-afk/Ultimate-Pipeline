# 🌌 PanMatrix Data Pipeline & Telemetry Grid

An automated data orchestration system featuring integrated infrastructure monitoring, Prometheus metrics archiving, and a custom cryptographic signature validation loop.

---

## 🏗️ Repository Architecture

*   `PANMATRIX_PIPELINE.core.py`: Main processing simulation engine generating synthetic spatial correlation loops.
*   `PANMATRIX_PROXY_BINDING.py`: FastAPI server proxy handling metric translations and full-duplex WebSockets.
*   `PROMeTHEUS.yml`: Hardened scraper target profile and HTTP compliance header injections.
*   `panmatrix_alerts.rules.yml`: Active Prometheus alerting thresholds for blind control loops.
*   `docker-compose.yml`: Multi-container virtualization topography orchestration file.
*   `dashboard.html`: Single-file holographic cyberpunk telemetry front-end interface.

---

## 🚀 Deployment Instructions

> [!IMPORTANT]  
> Execute these commands directly on your local machine using an interactive terminal window. These deployment operations require direct system access to your machine's Docker engine and cannot be executed inside an AI text assistant chat box.
>
> ### 💡 Note on Using the Automated `deploy.sh` Script

For one-click deployments, an automated shell script (`deploy.sh`) is provided. Depending on your Operating System, observe the following execution guidelines:

*   **Mac / Linux Users**: 
    Before running the script for the very first time, your system requires explicit execution permissions. Open your terminal inside the project directory and run this one-time command:
    ```bash
    chmod +x deploy.sh
    ```
    Once permissions are granted, you can launch the entire grid anytime by running:
    ```bash
    ./deploy.sh
    ```

*   **Windows Users**: 
    The `.sh` file format is a Bash script meant for Unix environments. It will **not** work inside standard Windows Command Prompt (`cmd`) or basic PowerShell. To use it on Windows, you must run it inside:
    *   **Git Bash** (installed automatically alongside Git for Windows)
    *   **WSL** (Windows Subsystem for Linux)
    
    *If you do not have Git Bash or WSL, simply bypass the script and type the native `docker compose up -d --build` command directly into your regular PowerShell window instead.*

    ### 💡 Automated One-Click Deployment Scripts

To bypass typing docker instructions manually, cross-platform automation execution targets are provided in the root repository folder:

*   **Windows Environment Users**: 
    Simply double-click the **`deploy.bat`** script file using File Explorer. It automatically checks your Docker status, mounts your data volumes, and starts trailing the processing engine logs instantly.

*   **Mac / Linux Environment Users**: 
    Open your system terminal within this directory and execute the following permission enablement rule once:
    ```bash
    chmod +x deploy.sh
    ```
    Once authorized, launch the entire operational matrix grid anytime using the local execution pointer:
    ```bash
    ./deploy.sh
    ```



### Prerequisites
1. Ensure **Docker Desktop** is installed and actively running on your machine.
2. Open your system's native command utility:
   *   **Mac**: Terminal app (`Cmd + Space` -> type "Terminal")
   *   **Windows**: PowerShell or Command Prompt
   *   **Linux**: Your default system shell

### Step 1: Navigate to Your Project Directory
Before executing Docker routines, orient your terminal window inside your code directory using the change directory (`cd`) command:
```bash
cd /path/to/your/panmatrix-project-folder
```

### Step 2: Spin Up Containers
Initialize the network matrix, build the core images, and spin up all telemetry components in detached background mode:
```bash
docker compose up -d --build
```

### Step 3: Stream Runtime Logs
Inspect active matrix routines to verify that your synthetic pipeline metrics are calculating and streaming correctly:
```bash
docker compose logs -f panmatrix-core
```

---

## 🖥️ Network & Dashboard Access Nodes

Once your container engine completes initialization, your application binds to the following network points on your machine:

*   **Holographic Live Dashboard**: Double-click your local `dashboard.html` file to open it in any web browser. It instantly binds to the active WebSocket stream on `ws://localhost:9100`.
*   **Prometheus Engine Interface**: Navigate to `http://localhost:9090` to review real-time historical graphing metrics, expression queries, and active target states.
*   **Raw Telemetry Endpoint**: Query `http://localhost:9100/metrics` to verify data outputs (requires exact compliance scraping headers to avoid an `HTTP 403 Forbidden` response).

---

## ⚖️ Legal Status & Licensing Framework

This repository is governed under the **First-Principles Humanity Commons License (Version 3.2)**, as registered by Kameron Knowlton (2026). 

*   **17 U.S.C. § 102 Secured**: Active copyrightable expression protection is enforced.
*   **Defensive Trademark Priority**: This project utilizes mandatory brand compliance tracking via the `X-Panmatrix-Trademark-Rider` header context constraint layers.
*   **Anti-Containment Mechanism**: Any downstream commercial ingestion, proprietary hoarding, or unauthorized machine learning parsing of this specific expression triggers automatic system closure revoking and immediate copyright infringement liability under standard Berne Convention global statutes.
