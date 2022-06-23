class Participant:
    """
    Participant in an auction.
    """
    def __init__(self, name, email, login, password, address, phone) -> None:
        self.name = name
        self.email = email
        self.login = login
        self.password = password
        self.address = address
        self.phone = phone
    
    def change_password(self, old_password, password):
        """
        Changes participants password.
        """
        if self.password == old_password:
            self.password = password
        else:
            raise Exception("Wrong Password")
