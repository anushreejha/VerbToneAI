import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.google_service import create_service
from configs.credentials_manager import get_google_creds_file
from assistant.response_generation import speak

# Set the credentials and scopes
CLIENT_SECRET_FILE = get_google_creds_file()
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

# Create the Gmail service using the Create_Service function
service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def send_email(to_email, subject, message_body):
    """
    Sends an email using the Gmail API and OAuth2 authentication.

    This function constructs an email with the provided recipient, subject, and message body. 
    It then sends the email using the Gmail API, after encoding it in base64 format.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        message_body (str): The body content of the email.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the email sending process.
    """
    try:
        # Create the email 
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = to_email
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(message_body, 'plain'))

        # Encode the email (base64)
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        # Send the email via the Gmail API
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

        print(f'Email sent successfully: {message}')
        speak("Email sent successfully.")

    except Exception as e:
        print(f'An error occurred: {e}')
