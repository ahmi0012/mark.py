# Python Personal Assistant: Friday
This repository contains a Python-based personal assistant named Friday. The assistant is designed to perform a variety of tasks using voice commands. Friday listens to user commands through speech recognition, processes them, and executes tasks like web searches, playing music, sending emails, and more. It's built with simple yet powerful Python libraries, making it an ideal project for anyone interested in building their own virtual assistant.

# Key Features:
Speech Recognition: Listens to user voice commands using Google's speech recognition API.
Text-to-Speech: Uses pyttsx3 to provide spoken feedback to the user.
Wikipedia Integration: Searches and summarizes information from Wikipedia.
Web Browsing: Opens popular websites like YouTube, Google, and Stack Overflow based on voice commands.
YouTube Control: Plays music and videos on YouTube using pywhatkit.
Local Music Playback: Plays music from a predefined directory on the local system.
Time Check: Tells the current time when asked.
Email Sending: Sends an email to a specific contact using SMTP.
Task Automation: Opens Visual Studio Code or any other application based on commands.
Interactive Conversations: Responds to basic conversational queries like "Hello", "How are you?", "Thank you", etc.
Sleep Mode: Can go into sleep mode and wake up on user command.
#Technologies Used:
pyttsx3: Text-to-speech engine for providing audio feedback.
SpeechRecognition: For processing and converting voice input to text.
Wikipedia: To fetch and summarize information from Wikipedia.
Webbrowser: To automate web searches and open websites.
pywhatkit: For playing YouTube videos.
smtplib: For sending emails through Gmail's SMTP server.
os: To interact with the file system and open local applications.
datetime: To check and announce the current time.
# How to Use:
Clone the repository and install the required dependencies.
Set up your Gmail credentials in the code for email functionality.
Run the script, and the assistant will start listening for commands.
Say "wake up" to activate Friday and "goodbye" to exit the assistant.
# Installation:
Clone the repository:
bash
git clone https://github.com/your-username/friday-assistant.git
Install dependencies:
bash
pip install -r requirements.txt
Run the script:
bash
Copy code
python assistant.py
Commands:
"Open YouTube"
"Search Wikipedia for [topic]"
"Play songs on YouTube"
"What's the time?"
"Send email to [contact]"
And more...
⚠️ Note: This project is for educational purposes only. Modify the code to fit your own preferences and customize the assistant further.
