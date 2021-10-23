def jwt_response_payload_handler(token, user=None, request=None):
    # Modifies the original JWT response to include
    # elements such as the user_id and the email
    return {
        'token': token,
        'user_id': user.id,
        'email': user.email
    }
