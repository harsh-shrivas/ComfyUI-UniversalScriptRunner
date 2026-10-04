# ComfyUI-UniversalScriptRunner

A non-blocking process launcher and automation orchestration node for ComfyUI.

Built for VFX pipeline engineers, technical directors, and automation developers who need ComfyUI to trigger external host software (such as Adobe After Effects via ExtendScript CLI), render scripts, background batch utilities, Python processes, or standalone binaries without freezing the ComfyUI server.

---

## Features

- **Asynchronous Non-Blocking Execution:** Launches target binaries and scripts in their native working directory using decoupled shell subprocesses, keeping the ComfyUI canvas responsive.
- **Dedicated Windows Shell Handling:** Automatically detects `.bat` and `.cmd` scripts and wraps them in a dedicated shell instance, while launching standard executables (`.exe`) directly.
- **Dynamic Argument Ingestion:** Accepts arbitrary CLI arguments and runtime flags (such as `-r Path\To\script.jsx` or `--headless`) to pass data directly into external tools.
- **Pipeline Signal Chaining:** Consumes upstream execution triggers and emits timestamped completion tokens (`trigger_signal`) to coordinate strict chronological execution order across your graph.
- **Zero External Dependencies:** Built 100% on native Python standard libraries (`os`, `subprocess`, `time`) with zero external pip requirements.

---

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   cd ComfyUI/custom_nodes

2. Clone this repository:
   git clone https://github.com/harsh-shrivas/ComfyUI-UniversalScriptRunner.git

3. Restart ComfyUI. (Zero external pip packages required).

---

## Usage

- **Category:** `Automation/Script Runner`
- **Node Name:** `Universal Script Runner`
- **Workflow:**
  1. In `script_path`, enter the absolute path to your target executable or script (e.g., `Path\To\Script\run_pipeline.bat` or `C:\Program Files\Adobe\Adobe After Effects <VERSION>\Support Files\afterfx.exe`).
  2. In `arguments`, supply any required CLI arguments or execution flags (e.g., `-r Path\To\Script\render.jsx`).
  3. *(Optional)* Connect an upstream node output into `trigger_signal` to delay execution until prerequisites finish.
  4. Click **Queue Prompt**. The node will launch the external process in its parent directory, log the action, and emit a downstream trigger token.

---

## Inputs & Outputs

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **script_path** | `STRING` (Input) | `""` | Absolute path to the executable or script to run |
| **arguments** | `STRING` (Input) | `""` | Command-line arguments and flags passed to the script |
| **trigger_signal** | `STRING` (Optional Input) | — | Upstream dependency trigger to sequence execution |
| **execution_log** | `STRING` (Output) | — | Process launch status message and verified path |
| **trigger_signal** | `STRING` (Output) | — | Timestamped downstream execution token |

---

## License

MIT License. Free to use, adapt, and integrate into internal studio pipelines and personal automation workflows.
