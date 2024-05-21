import pyttsx3
from faker import Faker
import whois
import requests
from bs4 import BeautifulSoup
import random

fake = Faker()

def text_to_speech(text, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()

def generate_phishing_email():
    templates = [
        {
            "subject": "Important Update Required for Your Account",
            "body": """
            Dear {name},

            We have detected unusual activity on your account. Please update your information immediately to avoid suspension.

            Click here to update: {url}

            Best regards,
            {company}
            """
        },
        {
            "subject": "Your Invoice is Ready",
            "body": """
            Hello {name},

            Your invoice for this month is ready. Please review and pay your invoice using the link below.

            View Invoice: {url}

            Thank you,
            {company}
            """
        },
        {
            "subject": "Reset Your Password",
            "body": """
            Hi {name},

            We received a request to reset your password. Use the link below to set up a new password.

            Reset Password: {url}

            If you didn't request a password reset, please ignore this email.

            Regards,
            {company}
            """
        }
    ]
    
    template = random.choice(templates)
    subject = template["subject"]
    body = template["body"].format(
        name=fake.name(),
        url=fake.url(),
        company=fake.company()
    )
    
    print(f"Subject: {subject}\n{body}")

def get_domain_info(domain):
    domain_info = whois.whois(domain)
    print(domain_info)

def find_emails(domain):
    url = f"https://{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    emails = set()
    for a in soup.find_all('a', href=True):
        if "mailto:" in a['href']:
            email = a['href'].split(':')[1]
            emails.add(email)
    for email in emails:
        print(email)

def print_logo():
    logo = """
     _______________ 
    |#####|_____   /|
    |#####|#####| / |
    |#####|#####|/| |
    |#####|###{ O } |
    |#####|#####| | |
    |#####|#####|/| |
    |#####|#####| | /
    |#####|#####|/ /
    |#####|_____/_/
    |  /          |
    | /    SIMA   |
    |/    CLOAK   |
    """
    print(logo)

def main():
    print_logo()
    while True:
        print("\nSelect an option:")
        print("1. Clone voice and generate speech")
        print("2. Generate phishing email samples")
        print("3. Find details about a domain")
        print("4. Find emails of an organization")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            text = input("Enter the text to convert to speech: ")
            filename = input("Enter the output filename (with .mp3 extension): ")
            text_to_speech(text, filename)
        elif choice == '2':
            generate_phishing_email()
        elif choice == '3':
            domain = input("Enter the domain name: ")
            get_domain_info(domain)
        elif choice == '4':
            domain = input("Enter the domain name: ")
            find_emails(domain)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
