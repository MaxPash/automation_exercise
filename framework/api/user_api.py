class UserAPI:

    def __init__(self, request_context):
        self.request = request_context

    def create_user(self, payload):

        return self.request.post(
            "/api/createAccount",
            form=payload
        )

    def verify_login(self, email, password):

        return self.request.post(
            "/api/verifyLogin",
            form={
                "email": email,
                "password": password
            }
        )

    def delete_user(self, email, password):

        return self.request.delete(
            "/api/deleteAccount",
            form={
                "email": email,
                "password": password
            }
        )