from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle
from google.auth.transport.requests import Request


def create_service(client_secret_file, api_name, api_version, *scopes):
    """
    Creates an authenticated service object for accessing a specified Google API.
    
    The OAuth 2.0 authentication is used to generate and store credentials for accessing a given 
    API service. It uses the provided client secret file to initiate the authentication process 
    and retrieves the necessary credentials (either by refreshing an existing token or generating 
    a new one). The credentials are then used to create and return a service object for the API.

    Args:
        client_secret_file (str): Path to the client secret file (JSON file) 
                                   containing the OAuth 2.0 client credentials.
        api_name (str): The name of the API to connect to.
        api_version (str): The version of the API to connect to.
        *scopes (list): One or more OAuth 2.0 scopes (define level of access).

    Returns:
        googleapiclient.discovery.Resource: An authenticated service object to interact with
                                             the specified API, or None if the authentication
                                             or connection fails.

    Raises:
        Exception: If the service cannot be created or the authentication fails.
    """
    print(client_secret_file, api_name, api_version, scopes, sep='-')

    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    print(SCOPES)

    cred = None
    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            # OAuth flow runs on port 10000 for authentication
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server(port=10000)  # Fixed port

        # Save the credentials for the next run
        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'Service created successfully.')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None
