import os
import subprocess
import time

class UniversalScriptRunner:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "script_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "placeholder": "C:\\path\\to\\executable.exe or script.bat"
                }),
                "arguments": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "placeholder": "-r C:\\path\\to\\script.jsx"
                }),
            },
            "optional": {
                "trigger_signal": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("execution_log", "trigger_signal")
    FUNCTION = "run_script"
    OUTPUT_NODE = True
    CATEGORY = "Automation/Script Runner"

    @classmethod
    def IS_CHANGED(s, script_path, arguments="", trigger_signal=None):
        return float(time.time())

    def run_script(self, script_path, arguments="", trigger_signal=None):
        clean_path = script_path.strip().strip('"').strip("'")
        print(f"[Universal Script Runner] Initiating launch for: '{clean_path}'")

        if not clean_path or not os.path.exists(clean_path):
            err_msg = f"ERROR: Target executable/script not found -> '{clean_path}'"
            print(f"[Universal Script Runner] {err_msg}")
            return (err_msg, f"FAILED_{time.time()}")

        try:
            working_dir = os.path.dirname(clean_path)
            clean_args = arguments.strip()

            if clean_path.endswith('.bat') or clean_path.endswith('.cmd'):
                cmd = f'start "Script Runner" /d "{working_dir}" cmd.exe /c ""{clean_path}" {clean_args}"'
            else:
                cmd = f'start "" /d "{working_dir}" "{clean_path}" {clean_args}'

            subprocess.Popen(cmd, shell=True, cwd=working_dir)
            log = f"Launched successfully: {clean_path} {clean_args}"

            time.sleep(1.5)
            return (log, f"TRIGGER_OK_{time.time()}")

        except Exception as e:
            err = f"EXCEPTION executing script: {str(e)}"
            print(f"[Universal Script Runner] {err}")
            return (err, f"ERROR_{time.time()}")

NODE_CLASS_MAPPINGS = {"UniversalScriptRunner": UniversalScriptRunner}
NODE_DISPLAY_NAME_MAPPINGS = {"UniversalScriptRunner": "Universal Script Runner"}
