import abc

from tkinter import *
from tkinter import ttk

def format_money(amount):
    """
    Formats an amount in money form ($X.XX)
    """
    return f"${amount:.2f}"

def format_transfer(amount):
    """
    Formats a transfer of a given amount.
    """
    if amount >= 0:
        return f"Transferência recebida: + {format_money(amount)}"
    return f"Transferência enviada: - {format_money(-amount)}"

class BankAccount:
    """
    Bank account with money.
    """
    def __init__(self, start_money) -> None:
        self.money = start_money
        self.extract = f"Saldo Anterior: {format_money(start_money)}\n"
    
    def transfer(self, amount):
        """
        Transfers money from/to account.
        """
        self.money += amount
        self.extract += f"{format_transfer(amount)}\n"


class BankGUI:
    """
    GUI for a Bank
    """
    def __init__(self, root):

        root.title("Banco")
        invoker = Invoker(self)
        self.history_operations = ""

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        saldo_button = ttk.Button(mainframe, text="Verificar Saldo", command=invoker.show_saldo)
        saldo_button.grid(column=1, row=1, sticky=W)

        ttk.Label(mainframe, text="Transferência:").grid(column=1, row=2, sticky=W)
        self.transfer = StringVar()
        self.transfer_entry = ttk.Entry(mainframe, width=15, textvariable=self.transfer)
        self.transfer_entry.grid(column=1, row=3, sticky=(W, E))
        transfer_button = ttk.Button(mainframe, text="Transferir", command=invoker.do_transfer)
        transfer_button.grid(column=1, row=4, sticky=W)

        extrato_button = ttk.Button(mainframe, text="Mostrar Extrato", command=invoker.show_extrato)
        extrato_button.grid(column=1, row=5, sticky=W)

        history_button = ttk.Button(mainframe, text="Mostrar Histórico", command=invoker.show_history)
        history_button.grid(column=1, row=6, sticky=W)

        self.info_title = ttk.Label(mainframe, text="Bem vindo!")
        self.info_title.grid(column=2, row=1)

        self.info = ttk.Label(mainframe, text="")
        self.info.grid(column=2, row=2, rowspan=5, sticky=N)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

class Command(abc.ABC):
    """
    Command design pattern.
    """
    def __init__(self, app : BankGUI, account : BankAccount) -> None:
        self.app = app
        self.account = account
    
    @abc.abstractmethod
    def execute(self):
        """
        Executes the button press
        """
        pass

class SaldoCommand(Command):
    """
    Command design pattern.
    """
    def execute(self):
        """
        Executes the button press
        """
        self.app.info_title["text"] = "Saldo:"
        self.app.info["text"] = format_money(self.account.money)
        

class TransferCommand(Command):
    """
    Command design pattern.
    """
    def execute(self):
        """
        Executes the button press
        """
        self.account.transfer(float(self.app.transfer_entry.get()))

class ExtratoCommand(Command):
    """
    Command design pattern.
    """
    def execute(self):
        """
        Executes the button press
        """
        self.app.info_title["text"] = "Extrato:"
        self.app.info["text"] = self.account.extract

class HistoryCommand(Command):
    """
    Command design pattern.
    """
    def execute(self):
        """
        Executes the button press
        """
        self.app.info_title["text"] = "Histórico:"
        self.app.info["text"] = self.app.history_operations

class Invoker:
    """
    Sender class.
    """
    def __init__(self, app : BankGUI) -> None:
        self.app = app
        self.account = BankAccount(1000)
        self.saldo = SaldoCommand(app, self.account)
        self.transfer = TransferCommand(app, self.account)
        self.extrato = ExtratoCommand(app, self.account)
        self.history = HistoryCommand(app, self.account)
    
    def show_saldo(self):
        """
        Shows the saldo in the GUI.
        """
        self.app.history_operations += f"Saldo verificado: {format_money(self.account.money)}\n"
        self.saldo.execute()
    
    def do_transfer(self):
        """
        Does the transfer.
        """
        self.app.history_operations += f"{format_transfer(float(self.app.transfer_entry.get()))}\n"
        self.transfer.execute()
    
    def show_extrato(self):
        """
        Shows the extrato in the GUI.
        """
        self.app.history_operations += "Extrato mostrado\n"
        self.extrato.execute()
    
    def show_history(self):
        self.app.history_operations += "Histórico mostrado\n"
        self.history.execute()

    
if __name__ == "__main__":
    root = Tk()
    BankGUI(root)
    root.mainloop()
