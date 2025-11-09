# WhatsApp Messages Generator

Automatically generates and sends formatted WhatsApp messages to the currently open chat window in WhatsApp Desktop. Supports multi-language messages with embedded links.

**⚠️ macOS Only** - This tool uses AppleScript and macOS-specific utilities.

## Features

- Parse messages from input file with Facebook and YouTube links
- Format messages with special styling (bold text, emojis)
- Automatically send multiple messages to open WhatsApp chat
- Support for multi-language content
- Clean message formatting with link separation

## Prerequisites

- macOS (required for AppleScript functionality)
- Python 3.6 or higher
- WhatsApp Desktop application installed
- Terminal access with appropriate permissions

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd WhatsApp-Messages-Generator
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Grant necessary permissions:**
   - Allow Terminal to control WhatsApp in System Preferences > Security & Privacy > Privacy > Accessibility
   - Ensure WhatsApp Desktop has necessary permissions

## Usage

### Quick Start

1. **Open WhatsApp Desktop** and navigate to the chat where you want to send messages

2. **Prepare your input file** (`live_input.txt`):
   ```
   🔴 LIVE NOW: Sunday Feast Class 🔽
   🔴 सीधा प्रसारण: रविवार प्रीति भोज प्रवचन 🔽
   🔴 সরাসরি সম্প্রচারিত হচ্ছে: রবিবারের প্রীতিভোজ প্রবচন 🔽
   
   https://www.facebook.com/share/v/1EuUn8JUWi/?mibextid=wwXIfr
   https://www.youtube.com/watch?v=nwsJ2MWn8aA
   ```

3. **Run the script:**
   ```bash
   python live_script.py
   ```

### Input File Format

The `live_input.txt` file should contain:
- Message lines (will be formatted with bold styling)
- Facebook links (lines containing "facebook.com")
- YouTube links (lines containing "youtu")
- Empty lines for separation (will be cleaned up automatically)

### Message Processing

- Messages starting with 🔴 get special formatting with bold text
- Facebook and YouTube links are automatically detected and appended
- Each message line becomes a separate WhatsApp message
- Links are included with each message

## File Structure

```
WhatsApp-Messages-Generator/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── live_script.py        # Main script for processing and sending messages
├── apple_util.py         # macOS utilities for clipboard and AppleScript
├── live_input.txt        # Input file with messages and links
└── .gitignore           # Git ignore rules
```

## How It Works

1. **Parse Input**: Reads `live_input.txt` and separates messages from links
2. **Format Messages**: Applies formatting rules (bold text, emoji spacing)
3. **Send Messages**: Uses AppleScript to:
   - Activate WhatsApp Desktop
   - Copy message to clipboard
   - Paste and send each message
   - Add delays for reliable delivery

## Troubleshooting

### Common Issues

**Script doesn't send messages:**
- Ensure WhatsApp Desktop is open and a chat is selected
- Check Terminal has Accessibility permissions in System Preferences
- Verify WhatsApp is the active application

**Messages appear malformed:**
- Check input file encoding (should be UTF-8)
- Ensure proper line breaks in `live_input.txt`

**Permission errors:**
- Grant Terminal access in System Preferences > Security & Privacy > Privacy > Accessibility
- Restart Terminal after granting permissions

### Debug Mode

To see what messages will be sent without actually sending them, modify `live_script.py` and comment out the `send_message_to_open_chat(msg)` line.

## Safety Notes

- Always test with a personal chat first
- Review messages in `live_input.txt` before running
- The script sends messages immediately - there's no undo
- Ensure you have the correct chat window open

