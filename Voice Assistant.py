import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
import tkinter as tk

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")

        self.label = tk.Label(root, text="Press the button and speak")
        self.label.pack(pady=20)

        self.listen_button = tk.Button(root, text="Listen", command=self.listen_and_respond)
        self.listen_button.pack(pady=20)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=20)

    def listen_and_respond(self):
        text = recognize_speech()
        if text:
            self.output_text.insert(tk.END, f"You said: {text}\n")
            response = self.process_query(text)
            self.output_text.insert(tk.END, f"Assistant: {response}\n")
            speak(response)

    def process_query(self, query):
        # Simplified response logic
        if "hello" in query.lower():
            return "Hello! How can I help you?"
        else:
            return "I am not sure how to respond to that."

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
