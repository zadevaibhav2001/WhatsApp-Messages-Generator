import subprocess
import time

# ---------------- Clipboard / AppleScript ----------------
def set_clipboard(text: str):
    """Set macOS clipboard"""
    p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
    p.communicate(text.encode("utf-8"))

def run_applescript(script: str):
    """Run AppleScript via osascript"""
    proc = subprocess.Popen(["osascript", "-e", script],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return proc.returncode, out.decode().strip(), err.decode().strip()

# ---------------- Send messages ----------------
def send_message_to_open_chat(message: str):
    """Send message to currently open chat"""
    set_clipboard(message)
    apple_script = '''
    tell application "System Events"
        tell application "WhatsApp" to activate
        delay 0.3
        -- paste clipboard content
        keystroke "v" using {{command down}}
        delay 1.0
        keystroke return
    end tell
    '''
    run_applescript(apple_script)
    time.sleep(0.5)
