import abc

class Document:
    """
    Document with different states.
    """
    def __init__(self, text, user) -> None:
        self.text = text
        self.user = user
        self.state = Draft(self)
    
    def render(self):
        """
        Render document.
        """
        self.state.render()
    
    def publish(self):
        """
        Publish document.
        """
        self.state.publish()
    
    def change_state(self, new_state):
        """
        Changes document's state.
        """
        self.state = new_state


class State(abc.ABC):
    """
    Document's states.
    """
    def __init__(self, document : Document) -> None:
        self.document = document

    @abc.abstractmethod
    def render(self):
        """
        Render document in state.
        """
        pass

    @abc.abstractmethod
    def publish(self):
        """
        Publish document in state.
        """
        pass


class Draft(State):
    """
    Document's state of Draft.
    """
    def __init__(self, document: Document) -> None:
        super().__init__(document)

    def render(self):
        """
        Render document in draft.
        """
        print("Draft:")
        print(self.document.text)

    def publish(self):
        """
        Publish document in state.
        """
        if self.document.user.isAdmin:
            self.document.change_state(Published(self.document))
        else:
            self.document.change_state(Moderation(self.document))


class Moderation(State):
    """
    Document's state of Moderation.
    """
    def __init__(self, document : Document) -> None:
        super().__init__(document)

    def render(self):
        """
        Render document in Moderation.
        """
        print("Moderation:")
        print(self.document.text)

    def publish(self):
        """
        Publish document in Moderation.
        """
        if self.document.user.isAdmin:
            self.document.change_state(Published(self.document))
        else:
            self.document.change_state(Draft(self.document))


class Published(State):
    """
    Document's state of Published.
    """
    def __init__(self, document : Document) -> None:
        super().__init__(document)
        self.publication_expired = False

    def render(self):
        """
        Render document in Published.
        """
        print("Published:")
        print(self.document.text)
        self.publication_expired = True

    def publish(self):
        """
        Publish document in Published.
        """
        if self.publication_expired:
            self.document.change_state(Draft(self.document))
        self.publication_expired = True


class User(abc.ABC):
    """
    User of the documents.
    """
    def __init__(self, isAdmin) -> None:
        self.isAdmin = isAdmin


class Member(User):
    """
    Non admin user of the documents.
    """
    def __init__(self) -> None:
        super().__init__(False)


class Admin(User):
    """
    User of the documents.
    """
    def __init__(self) -> None:
        super().__init__(True)


if __name__ == "__main__":
    user = Member()
    admin = Admin()

    print("Document made by user:")
    doc = Document("I am an user", user)
    doc.render()
    print()
    print("Published the document:")
    doc.publish()
    doc.render()
    print()
    print("Switch user to admin:")
    doc.user = admin
    doc.publish()
    doc.render()
    print()
    print("Publication expired:")
    doc.publish()
    doc.render()

    print()
    print("Document made by admin:")
    doc = Document("I am an admin", admin)
    doc.render()
    print()
    print("Published the document:")
    doc.publish()
    doc.render()
    print()
    print("Publication expired:")
    doc.publish()
    doc.render()

