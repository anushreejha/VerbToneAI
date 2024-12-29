import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.google_service import create_service  
from configs.credentials_manager import get_google_creds_file

# Set the credentials and scopes
CLIENT_SECRET_FILE = get_google_creds_file()  
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

# Create the Gmail service using the Create_Service function
service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def send_email(to_email, subject, message_body):
    """
    This function sends the email via Gmail API using OAuth2.
    """
    try:
        # Create the email 
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = to_email
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(message_body, 'plain'))

        # Encode the email (base 64)
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        # Send the email via the Gmail API
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

        print(f'Email sent successfully: {message}')

    except Exception as e:
        print(f'An error occurred: {e}')
