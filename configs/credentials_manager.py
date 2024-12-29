import os

def get_google_creds_file():
    """
    Fetches the path to the Google credentials JSON file.
    """
    creds_file = os.getenv('CREDS_FILE', 'configs/creds.json')  # Default path to creds.json
    if not os.path.exists(creds_file):
        raise FileNotFoundError(f"Credentials file {creds_file} not found.")
    return creds_file
