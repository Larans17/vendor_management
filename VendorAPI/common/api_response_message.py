# API RESPONSE MESSAGES
USER_ALREADY_EXISTS = 'Username already exists'
CODE = 'authorization'
VALIDATION_MSG = 'Must include "username" and "password"'
INVALID_ACCOUNT = "This account is invalid."
LOGIN_VERIFIED = "Logged-in successfully"
INVALID_USERNAME = "Username is incorrect"
INVALID_PASSWORD = "Password is incorrect"



class CommonApiMessages:

    @staticmethod

    def create(msg):
        message = {'message':f"{msg} created successfully"}
        return message
    
    def delete (msg):
        message = {'message':f"{msg} deleted successfully"}
        return message
    
    def restrict_delete (msg):
        message = {'message':f"{msg} is being referenced with another instance"}
        return message
    
    def does_not_exists(msg):
        message = f'{msg} ID does not exists.'
        return message
    
    def update(msg):
        message = {'message':f"{msg} updated successfully"}
        return message