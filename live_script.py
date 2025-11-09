import re
from pathlib import Path

from apple_util import send_message_to_open_chat


# ---------------- Parse & format messages ----------------
def detect_links_and_message(content):
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    fb_link = yt_link = None
    message_lines = []
    for line in lines:
        if "facebook.com" in line:
            fb_link = line
        elif "youtu" in line:
            yt_link = line
        else:
            message_lines.append(line)
    return "\n".join(message_lines), fb_link, yt_link

def clean_and_format_messages(raw_message, fb_link, yt_link):
    cleaned = re.sub(r"\n\s*\n+", "\n", raw_message.strip())
    lines = [line.strip() for line in cleaned.split("\n") if line.strip()]
    formatted_messages = []
    for line in lines:
        line = re.sub(r"^🔴\s*", "🔴 ", line)
        formatted_line = re.sub(r"(🔴 )(.*?)( 🔽)", r"\1*\2*\3", line)
        msg = f"{formatted_line}\n\n{fb_link}\n\n{yt_link}"
        formatted_messages.append(msg)
    return formatted_messages


# ---------------- Main ----------------
def main():
    # if len(sys.argv) < 2:
    #     print("Usage: python send_whatsapp_mac.py input.txt")
    #     return

    input_file = Path("live_input.txt")
    if not input_file.exists():
        print("Input file not found:", input_file)
        return

    content = input_file.read_text(encoding="utf-8")
    raw_msg, fb, yt = detect_links_and_message(content)
    messages = clean_and_format_messages(raw_msg, fb, yt)

    print(f"Found {len(messages)} message(s). Sending to currently open chat...\n")

    for i, msg in enumerate(messages, start=1):
        print(f"🟢 Sending message {i}/{len(messages)}...")
        send_message_to_open_chat(msg)

    print("\n✅ All messages sent successfully.")

if __name__ == "__main__":
    main()
