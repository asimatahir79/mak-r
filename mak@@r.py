import os
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
from faker import Faker
import random

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

# Function to generate phishing email
def generate_phishing_email(topic):
    fake = Faker()
    templates = [
        f"Dear {fake.name()},\n\nI hope this email finds you well. I am writing to inform you about an important matter regarding your account security. We have noticed some unusual activity on your account and require immediate action to verify your information.\n\nPlease click on the following link to verify your account: {fake.url()}\n\nThank you for your cooperation.\n\nSincerely,\n{fake.company()}",
        f"Hi {fake.name()},\n\nI'm reaching out to you regarding some unusual activity detected on your account. We need you to verify your account information promptly to ensure its security. Please follow the link below to verify your account:\n\n{fake.url()}\n\nBest Regards,\n{fake.company()}",
        f"Hello {fake.name()},\n\nThis is an important notification regarding your account security. We've identified some suspicious activities on your account and need your immediate attention to rectify the issue. Please proceed to the following link to verify your account:\n\n{fake.url()}\n\nThank you for your cooperation.\n\nRegards,\n{fake.company()}"
    ]
    template = random.choice(templates)
    return template

def main():
    # Define color symbols (replace with your preferences)
    color_red = chr(9829)  # Red heart symbol (❤️)
    color_green = chr(9827)  # Green clover symbol (♣️)
    color_blue = chr(9830)  # Blue diamond symbol (♦️)

    # Build the banner text with color-coded characters
    banner = f"""
            /\\_/\\  
           ( o.o )  mak@@r
             > ^ < 
          /  \\_/\\  \\
         /  '---'  \\
        /  |     |  \\
       /  |  {color_red}  |  \\  
      | @   \\___/   @ |
      \\  \\  `---'  /  /
       \\  \\       /  /
        \\  \\     /  /
         \\  \\   /  /      
          \\  \\_/  /       
           /  _  \\  
          /  / \\  \\  
         /_/   \\_\\ 
    """

    print(banner)

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
