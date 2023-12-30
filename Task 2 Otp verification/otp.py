from decouple import config
import smtplib
import random
from config import password
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_email_credentials():
    email_username ="m29649927@gmail.com"
    email_password = password            #Your email App password should be here

    return email_username, email_password

def generate_otp():
    # Generate a 6-digit OTP
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    email_username, email_password = get_email_credentials()

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = email_username
    message["To"] = receiver_email
    message["Subject"] = "OTP Verification"

    # Body of the email
    body = f"Your OTP for verification is: {otp}"
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_username, email_password)
        server.sendmail(email_username, receiver_email, message.as_string())

def verify_otp(user_input_otp, generated_otp):
    return user_input_otp == generated_otp

# Example usage
if __name__ == "__main__":
    # Replace with the recipient's email address
    recipient_email = "recipient@example.com"

    # Generate and send OTP
    otp = generate_otp()
    send_otp_email(recipient_email, otp)

    # Simulate user input (you would get this from the user)
    user_input_otp = input("Enter the OTP received: ")

    # Verify OTP
    if verify_otp(user_input_otp, otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")
