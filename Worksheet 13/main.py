from tkinter import *
from tkinter import ttk

from participant import Participant
from database import PariticipantDatabase

class ParticipantGUI:

    def __init__(self, root):

        root.title("Participante")
        self.database = PariticipantDatabase()

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.id = StringVar()
        id_entry = ttk.Entry(mainframe, width=15, textvariable=self.id)
        id_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="ID:").grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text="Consultar", command=self.consult).grid(column=3, row=1, sticky=W)

        self.name = StringVar()
        name_entry = ttk.Entry(mainframe, width=15, textvariable=self.name)
        name_entry.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="Nome:").grid(column=1, row=2, sticky=W)

        self.email = StringVar()
        email_entry = ttk.Entry(mainframe, width=15, textvariable=self.email)
        email_entry.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(mainframe, text="e-mail:").grid(column=1, row=3, sticky=W)

        self.address = StringVar()
        address_entry = ttk.Entry(mainframe, width=15, textvariable=self.address)
        address_entry.grid(column=2, row=4, sticky=(W, E))
        ttk.Label(mainframe, text="Endereço:").grid(column=1, row=4, sticky=W)

        self.phone = StringVar()
        phone_entry = ttk.Entry(mainframe, width=15, textvariable=self.phone)
        phone_entry.grid(column=2, row=5, sticky=(W, E))
        ttk.Label(mainframe, text="Telefone:").grid(column=1, row=5, sticky=W)

        self.login = StringVar()
        login_entry = ttk.Entry(mainframe, width=15, textvariable=self.login)
        login_entry.grid(column=2, row=6, sticky=(W, E))
        ttk.Label(mainframe, text="Login:").grid(column=1, row=6, sticky=W)

        self.password = StringVar()
        password_entry = ttk.Entry(mainframe, width=15, textvariable=self.password)
        password_entry.grid(column=2, row=7, sticky=(W, E))
        ttk.Label(mainframe, text="Senha:").grid(column=1, row=7, sticky=W)

        ttk.Button(mainframe, text="Registrar", command=self.register).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text="Atualizar", command=self.update).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text="Deletar", command=self.delete).grid(column=3, row=8, sticky=W)

        self.msg = ttk.Label(mainframe, text="Bem vindo!")
        self.msg.grid(column=1, columnspan=3, row=9)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def consult(self):
        """
        Consult a participant.
        """
        try:
            participant = self.database.data[int(self.id.get())]
            self.name.set(participant.name)
            self.email.set(participant.email)
            self.address.set(participant.address)
            self.phone.set(participant.phone)
            self.login.set(participant.login)
            self.password.set(participant.password)
            self.msg["text"] = "Participante encontrado!"
        except:
            self.msg["text"] = "Erro 404: Participante não encontrado!"
    
    def register(self):
        """
        Register a participant.
        """
        try:
            name = self.name.get()
            email = self.email.get()
            address = self.address.get()
            phone = self.phone.get()
            login = self.login.get()
            password = self.password.get()
            self.database.register_user(name, email, login, password, address, phone)
            self.msg["text"] = "Participante registrado!"
        except:
            self.msg["text"] = "Erro: Participante não registrado!"

    def update(self):
        """
        Update an user's data.
        """
        try:
            name = self.name.get()
            email = self.email.get()
            address = self.address.get()
            phone = self.phone.get()
            login = self.login.get()
            password = self.password.get()
            self.database.data[int(self.id.get())] = Participant(name, email, login, password, address, phone)
            self.msg["text"] = "Dados do Participante atualizados!"
        except:
            self.msg["text"] = "Erro 404: Participante não encontrado!"

    def delete(self):
        """
        Deletes user from database.
        """
        try:
            self.database.del_user(int(self.id.get()))
            self.msg["text"] = "Participante deletado!"
        except:
            self.msg["text"] = "Erro 404: Participante não encontrado!"

if __name__ == "__main__":
    root = Tk()
    ParticipantGUI(root)
    root.mainloop()