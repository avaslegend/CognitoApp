import os
import boto3
from dotenv import load_dotenv
load_dotenv()

CognitoClientID = os.getenv('COGNITO_USER_CLIENT_ID')
CognitoClient = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
