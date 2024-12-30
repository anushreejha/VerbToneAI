import os


def get_google_creds_file():
    """
    Fetches the path to the Google credentials JSON file.

    This function retrieves the path to the Google credentials file, either from an environment 
    variable 'CREDS_FILE' or defaults to 'configs/creds.json'. If the file does not exist, 
    it raises a `FileNotFoundError`.

    Args:
        None

    Returns:
        str: The path to the Google credentials file.

    Raises:
        FileNotFoundError: If the credentials file cannot be found at the specified path.
    """
    creds_file = os.getenv('CREDS_FILE', 'configs/creds.json')

    # Check if the credentials file exists at the specified path
    if not os.path.exists(creds_file):
        raise FileNotFoundError(f"Credentials file {creds_file} not found.")

    return creds_file
