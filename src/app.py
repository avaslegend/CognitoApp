from flask import Flask
from flask_cors import CORS
from flask import request
from util import build_user_json_response, generate_key
from config_client_cloud import CognitoClientID, CognitoClient

app = Flask(__name__)
CORS(app)


@app.route('/createUser', methods=['POST'])
def create_user():
    user_attributes = [
        {
            'Name': 'name',
            'Value': request.json['name']
        },
        {
            'Name': 'profile',
            'Value': request.json['profile']
        },
        {
            'Name': 'email',
            'Value': request.json['email']
        },
        {
            'Name': 'gender',
            'Value': request.json['gender']
        },
        {
            'Name': 'birthdate',
            'Value': request.json['birthDate']
        },
        {
            'Name': 'phone_number',
            'Value': request.json['phone']
        },
        {
            'Name': 'address',
            'Value': request.json['address']
        },
    ]

    response = CognitoClient.sign_up(
        ClientId=CognitoClientID,
        Username=request.json['userName'],
        Password=generate_key(20),
        UserAttributes=user_attributes
    )
    print(response)
    return build_user_json_response("", ""), 201


@app.route('/listUser', methods=['GET'])
def list_user():
    return [{"id": "123456", "name": "Jean"}, {"id": "987654", "name": "Mary"}]


@app.route('/updateUser/<id>', methods=['PUT'])
def update_user(id):
    if id.isnumeric():
        return build_user_json_response("id", "modified"), 200
    else:
        return build_user_json_response("Parameter ID is invalid", "error"), 400


@app.route('/deleteUser/<id>', methods=['DELETE'])
def delete_user(id):
    if id.isnumeric():
        return build_user_json_response("id", "deleted"), 200
    else:
        return build_user_json_response("id parameter is invalid", "error"), 400


@app.route('/forgotPassword/<username>', methods=['POST'])
def forgot_password_user(username):
    response = CognitoClient.forgot_password(
        ClientId=CognitoClientID,
        Username=username,
    )
    print(response)
    return build_user_json_response("", ""), 200


@app.route('/confirmForgotPassword', methods=['POST'])
def confirm_forgot_password_user():
    try:
        response = CognitoClient.confirm_forgot_password(
            ClientId=CognitoClientID,
            Username=request.json['userName'],
            Password=generate_key(20),
            ConfirmationCode=request.json['code'],
        )
        print(response)
        return build_user_json_response("", ""), 200

    except Exception:
        return build_user_json_response("Code verification is not valid", "error"), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
