import os
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
from faker import Faker
import openai

# Function to convert text to speech
def text_to_speech(text, output_file, language='en', accent='us'):
    tts = gTTS(text=text, lang=language, tld='com', slow=False)
    tts.save(output_file)

# Function to convert speech to text
def speech_to_text(input_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Function to clone voice from audio
def clone_voice(input_file, text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Function to generate phishing email using OpenAI GPT-3
def generate_phishing_email(topic):
    openai.api_key = ''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a phishing email with the topic: {topic}",
        max_tokens=150
    )
    email_content = response.choices[0].text.strip()
    return email_content

def main():
    while True:
        print("Choose an option:")
        print("1. Text to Speech")
        print("2. Speech to Text")
        print("3. Clone Voice")
        print("4. Generate Phishing Email")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            text = input("Enter the text to convert to speech: ")
            output_file = input("Enter the output file name (with .mp3 extension): ")
            text_to_speech(text, output_file)
            print(f"Text has been converted to speech and saved in {output_file}")
        elif choice == '2':
            input_file = input("Enter the input file name (with .wav extension): ")
            text = speech_to_text(input_file)
            print(f"The converted text is: {text}")
        elif choice == '3':
            input_file = input("Enter the input file name (with .wav extension): ")
            text = input("Enter the text to convert to the cloned voice: ")
            output_file = input("Enter the output file name (with .mp3 extension): ")
            clone_voice(input_file, text, output_file)
            print(f"Voice has been cloned and saved in {output_file}")
        elif choice == '4':
            topic = input("Enter the topic for the phishing email: ")
            email_content = generate_phishing_email(topic)
            print(f"Generated phishing email content:\n{email_content}")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

