import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = 'user01'
confirm_code = '499748'
password = 'xxxxxxx'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
response = client.confirm_forgot_password(
    ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
    Username=username,
    Password=password,
    ConfirmationCode=confirm_code,
)

print(response)