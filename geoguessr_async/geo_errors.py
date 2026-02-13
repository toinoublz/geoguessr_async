class NonExistingUser(Exception):
    def __init__(self, userId) -> None:
        self.message = f"The ID {userId} does not exist."
        super().__init__(self.message)
