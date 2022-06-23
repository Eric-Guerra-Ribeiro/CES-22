import participant

class PariticipantDatabase:
    """
    Database for all participants.
    """
    def __init__(self) -> None:
        self.counter = 0
        self.data = {}
        self.logins = {}
    
    def register_user(self, name, email, login, password, address, phone):
        """
        Registers user in database.
        """
        self.data[self.counter] = participant.Participant(name, email, login, password, address, phone)
        self.logins[login] = self.counter
        self.counter += 1
    
    def update_user(self, id, name, email, login, password, address, phone):
        """
        Updates user's data in database.
        """
        self.data[id] = participant.Participant(name, email, login, password, address, phone)
    
    def del_user(self, id):
        """
        Deletes user from database.
        """
        del self.data[id]
