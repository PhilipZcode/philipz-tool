# 🛠️ PhilipZ Tool

**PhilipZ Tool** is a feature-rich, standalone Windows Command Line (CLI) utility built with Python. Designed for productivity, system monitoring, media processing, and AI interaction—all wrapped inside a single tool.

<p align="center">
  <img width="386" height="267" alt="PhilipZ Tool Demo" src="https://github.com/user-attachments/assets/06fa2db8-0e32-43bc-af68-f33c4a807995" />
</p>
---

## ✨ Features

- **🔑 Secure Password Generator:** Generate strong, customizable passwords instantly.
- **📊 System Monitor (CPU & RAM):** Track hardware performance in real-time with clean CLI tables.
- **🎵 Multi-Platform Media Downloader:** Download videos and MP3 tracks from YouTube, Spotify, SoundCloud, and other platforms with metadata included.
- **🤖 PhilipZ AI:** Conversational AI powered by Google's Gemini Cloud API (`gemini-3.6-flash`) supporting multi-turn chats.

---

## 🚀 Getting Started (Standalone Executable)

No Python installation required! You can download and run the pre-compiled executable directly:

1. Navigate to the **[Releases](https://github.com/PhilipZcode/philipz-tool/releases)** section.
2. Download `PhilipZ Tool.zip`.
3. Double-click the file to launch.

---

## 💻 Local Development

To run or build the project from source:

```bash
# Clone the repository
git clone [https://github.com/PhilipZcode/philipz-tool.git](https://github.com/PhilipZcode/philipz-tool.git)

# Enter the project directory
cd philipz-tool

# Install required dependencies
pip install rich psutil google-genai yt-dlp spotdl pyinstaller

# Run the application
python main.py
