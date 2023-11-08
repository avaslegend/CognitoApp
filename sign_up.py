import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = 'user01'
password = 'zzzzzzzzzz'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))

response = client.sign_up(
    ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
    Username=username,
    Password=password,
    UserAttributes=[
        {
            'Name': 'name',
            'Value': 'Smith'
        },
        {
            'Name': 'profile',
            'Value': 'sava'
        },
        {
            'Name': 'email',
            'Value': 'sava25.mit@gmail.com'
        },
        {
            'Name': 'gender',
            'Value': 'Male'
        },
        {
            'Name': 'birthdate',
            'Value': '1985-02-12'
        },
        {
            'Name': 'phone_number',
            'Value': '+51964214557'
        },
        {
            'Name': 'address',
            'Value': 'av alamos 241'
        },
    ]
)

print(response)