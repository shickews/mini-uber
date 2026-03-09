class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        return f"User {self.username} registered successfully!"

# Example usage
if __name__ == '__main__':
    user = User('jane_doe', 'securepassword123')
    print(user.register())