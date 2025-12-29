# H.A.S - Desktop Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**H.A.S** (Helper Assistant System) is a Python-based desktop voice assistant designed to automate daily tasks, manage workflow, and provide hands-free control of your computer. It utilizes speech recognition and text-to-speech synthesis to interact with the user, functioning similarly to tools like Jarvis or Alexa.

## 🚀 Features

* **Voice Interaction:** Converts speech to text using Google Speech API and speaks back using `pyttsx3`.
* **Web Scraper:** Searches **Wikipedia** and reads out summaries of topics on command.
* **Application Control:** Launches desktop applications (e.g., Spotify, Games) and websites (YouTube) via voice.
* **Task Management:** Specific commands to **Add**, **Read**, and **Remove** items from a dynamic To-Do list.
* **System Info:** Provides real-time updates on current time and date.

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**
    * `speech_recognition`: For converting audio into text.
    * `pyttsx3`: Offline Text-to-Speech (TTS) engine.
    * `wikipedia`: To fetch data from Wikipedia.
    * `webbrowser`: To interact with web browsers.
    * `os`: For operating system interaction and file execution.

## ⚙️ Installation & Setup

Follow these steps to run the assistant on your local machine:

### 1. Clone the Repository
git clone [https://github.com/AdityaChauhan225/H.A.S.git](https://github.com/AdityaChauhan225/H.A.S.git)
cd H.A.S
### 2. Install Dependencies
You will need to install the required Python libraries. Open your terminal and run:


pip install pyttsx3 speechrecognition wikipedia
> Note: You may also need pyaudio. If pip install pyaudio fails, use pipwin install pyaudio.

### 3. Configure Paths
Important: The script uses local file paths to open applications.

Open the main python file.

Locate the lines containing os.startfile(...).

Replace the file paths with the location of the shortcuts/exes on your specific computer.

### 4. Run the Assistant
Bash

python main.py
📋 Usage Guide
Once the script is running, the assistant will start listening. Here are some command examples:

"Wikipedia [Topic]": Searches Wikipedia for the topic.

"Open YouTube": Opens YouTube in your default browser.

"Open Spotify": Launches the Spotify desktop app.

"Add to list": Activates the To-Do list mode to save a task.

"What is the time?": Tells the current time.

🔮 Future Improvements
Integration with OpenAI API for more natural conversational abilities.

Adding a Graphical User Interface (GUI).

Automating email sending and calendar scheduling.

##### Created by Aditya Chauhan
