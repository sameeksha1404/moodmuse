# 🎵 Mood Music Generator

**An AI-powered music generator that creates melodies based on your mood using MIDI and Gradio.**

---

## 🚀 Features

- 🎼 **Mood-Based Music Generation**  
  Select from moods like **Happy**, **Sad**, or **Chill**, and the app generates a unique melody just for you.

- 🎧 **Real-Time Audio Playback**  
  Listen to your generated music instantly through a simple, interactive **Gradio** interface.

- 💾 **Downloadable MIDI Output**  
  Save the generated tunes as `.midi` files for remixing, editing, or personal use.

- 🖥 **One-Click Web Interface**  
  No coding required — just launch and interact via your browser.

- ☁ **AWS EC2 Deployment Ready**  
  Fully configured to run on **AWS EC2 Free Tier** (Ubuntu 22.04, t2.micro), making it scalable and accessible from anywhere.

---

## 🧠 How It Works

1. Launch the app on your local machine or AWS EC2 instance.  
2. Choose a mood using the Gradio UI.  
3. MIDI music is generated using Python and **MIDIUtil**.  
4. **Timidity** converts the MIDI into audio for instant playback.  
5. Download the track if you like it! 🎶

---
🛠 Tech Stack
Python 3
MIDIUtil
Gradio
Timidity (for audio conversion)
AWS EC2
