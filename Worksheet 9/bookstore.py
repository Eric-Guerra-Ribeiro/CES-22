import register
import product
import person
import order

class BookStore:
    """
    Class for managing a Book Store.
    """
    def __init__(self) -> None:
        self.client_register = register.RegisterPerson()
        self.writer_register = register.RegisterPerson()
        self.book_register = register.RegisterBook(self.writer_register)
        self.order_register = register.RegisterOrder(self.client_register)
        print("Welcome to the Book Store:")
        self.customer_service()
    
    def customer_service(self):
        """
        Handles the services for the costumers.
        """
        print()
        print("What would you like to do?")
        print("Press 1 add to register")
        print("Press 2 modify register")
        print("Press 3 to find in register")
        print("Press 4 delete from register")
        print("Press 5 to print register")
        print("Press 6 to exit the Book Store")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.add_to_register()
        elif pressed == "2":
            self.modify_register()
        elif pressed == "3":
            self.find_in_register()
        elif pressed == "4":
            self.del_from_register()
        elif pressed == "5":
            self.print_register()
        elif pressed == "6":
            print("Thank you! Come back soon.")
            return
        else:
            print("Invalid key, try again, please")
        self.customer_service()

    def add_to_register(self):
        """
        Adds new entry to the register.
        """
        print()
        print("What kind of new entry to add?")
        print("Press 1 for books")
        print("Press 2 for clients")
        print("Press 3 for orders")
        print("Press 4 to go back")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.add_new_book()
        elif pressed == "2":
            self.add_new_client()
        elif pressed == "3":
            self.add_new_order()
        elif pressed == "4":
            self.customer_service()
        else:
            print("Invalid key, try again, please.")
            self.add_to_register()

    def add_new_book(self):
        """
        Creates new book and adds it to register.
        """
        print()
        print("Creating new book, fill down the information bellow:")
        title = input("Book title? ")
        writer_name = input("Book writer? ")
        genre = input("Book genre? ")
        edition = input("Book edition? ")
        publisher = input("Book publisher? ")
        sell_price = float(input("Book sell price? "))
        buy_price = float(input("Book buy price? "))
        writer = self.writer_register.find_element(writer_name)
        if writer is None:
            writer = person.Writer(writer_name)
            self.writer_register.add_element(writer)
        book = product.Book(title, writer, genre, edition, publisher, sell_price, buy_price)
        self.book_register.add_element(book)

    def add_new_client(self):
        """
        Creates a new client and adds it the to the register.
        """
        print()
        print("Creating new client, fill down the information bellow:")
        name = input("Client name? ")
        client = person.Client(name)
        self.client_register.add_element(client)
    
    def add_new_order(self):
        """
        Creates a new order and adds it to the register,
        """
        print()
        print("Creating new order, fill down the information bellow")
        client_name = input("Client? ")
        n_books = input("How many books in the order? ")
        try:
            n_books = int(n_books)
        except:
            print("Invalid number.")
            return
        order_list = []
        for i in range(n_books):
            book_name = input(f"{i+1}-th Book name? ")
            book_qnty = input(f"{i+1}-th Book quantity? ")
            book = self.book_register.find_element(book_name)
            order_list.append({"product": book, "qnty":book_qnty})
        client = self.client_register.find_element(client_name)
        if client is None:
            client = self.client_register.add_element(person.Client(client_name))
        new_order = order.OrderProduct(client, order_list)
        self.order_register.add_element(new_order)


    def modify_register(self):
        """
        Modifies entry in register.
        """
        print()
        print("What kind of entry to modify?")
        print("Press 1 for books")
        print("Press 2 for clients")
        print("Press 3 for orders")
        print("Press 4 to go back")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.modify_book()
        elif pressed == "2":
            self.modify_client()
        elif pressed == "3":
            self.modify_order()
        elif pressed == "4":
            self.customer_service()
        else:
            print("Invalid key, try again, please.")
            self.modify_register()

    def modify_book(self):
        """
        Modifies book in register.
        """
        print()
        book_name = input("What's the name of the book to be modified? ")
        book = self.book_register.find_element(book_name)
        if book is None:
            print("Book not in register.")
            return
        sell_price = input("New sell price? ")
        buy_price = input("New buy price? ")
        book.modify_atribute("sell_price", sell_price)
        book.modify_atribute("buy_price", buy_price)
    
    def modify_client(self):
        """
        Modifies client in register.
        """
        print()
        client_name = input("What's the name of the client to be modified? ")
        client = self.client_register.find_element(client_name)
        if client is None:
            print("Client not in register.")
            return
        new_name = input("New client name? ")
        client.modify_atribute("name", new_name)

    def modify_order(self):
        """
        Modifies order in register.
        """
        print()
        order_id = input("What's the id of the order to be modified? ")
        try:
            order_id = int(order_id)
        except:
            print("Order not in register.")
            return
        order = self.order_register.find_element(order_id)
        if order is None:
            print("Order not in register.")
            return
        book_name = input("What's the name of the book in the order? ")
        book = self.book_register.find_element(book_name)
        if book is None:
            print("Book not in register.")
            return
        new_qnty = input("Change to buy how many units? ")
        try:
            new_qnty = int(new_qnty)
        except:
            print("Not valid amount.")
            return
        order.modify_order_item(product=book, new_qnty=new_qnty)
            

    def find_in_register(self):
        """
        Finds entry in register.
        """
        print()
        print("What kind of entry to find?")
        print("Press 1 for books by title")
        print("Press 2 for books by writer")
        print("Press 3 for clients")
        print("Press 4 for orders")
        print("Press 5 to go back")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.find_book()
        elif pressed == "2":
            self.find_book_writer()
        elif pressed == "3":
            self.find_client()
        elif pressed == "4":
            self.find_order()
        elif pressed == "5":
            self.customer_service()
        else:
            print("Invalid key, try again, please.")
            self.find_in_register()

    def find_book(self):
        """
        Finds if book is in the register.
        """
        print()
        book_name = input("What's the book name? ")
        book = self.book_register.find_element(book_name)
        if book is None:
            print("Book not in register.")
            return
        print("Book in register.")
    
    def find_book_writer(self):
        """
        Finds all books in the register written by writer.
        """
        print()
        writer_name = input("What's the writer name? ")
        published_titles = self.book_register.find_books_writer(writer_name)
        if len(published_titles) > 0:
            print("[", end="")
            for i in range(len(published_titles) - 1):
                print(f"{published_titles[i]}, ", end="")
            print(f"{published_titles[-1]}]")
        else:
            print("[]")

    def find_client(self):
        """
        Finds if client is in the register.
        """
        print()
        client_name = input("What's the client name? ")
        client = self.client_register.find_element(client_name)
        if client is None:
            print("Client not in register.")
            return
        print("Client in register.")
    
    def find_order(self):
        """
        Finds if order is in the register.
        """
        print()
        order_id = input("What's the order id? ")
        order = self.order_register.find_element(order_id)
        if order is None:
            print("Order not in register.")
            return
        print("Order in register.")

    def del_from_register(self):
        """
        Deletes entry in register.
        """
        print()
        print("What kind of entry to delete?")
        print("Press 1 for books")
        print("Press 2 for clients")
        print("Press 3 for orders")
        print("Press 4 to go back")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.del_book()
        elif pressed == "2":
            self.del_client()
        elif pressed == "3":
            self.del_order()
        elif pressed == "4":
            self.customer_service()
        else:
            print("Invalid key, try again, please.")
            self.del_from_register()

    def del_book(self):
        """
        Delete book from register.
        """
        print()
        book_name = input("What's the book name? ")
        book = self.book_register.find_element(book_name)
        if book is None:
            print("Book not in register")
            return
        self.book_register.del_element(book)

    def del_client(self):
        """
        Delete client from register.
        """
        print()
        client_name = input("What's the client's name? ")
        client = self.client_register.find_element(client_name)
        if client is None:
            print("Client not in register")
            return
        self.client_register.del_element(client)

    def del_order(self):
        """
        Delete book from register.
        """
        print()
        order_id = input("What's the order id? ")
        order = self.order_register.find_element(order_id)
        if order is None:
            print("Order not in register")
            return
        self.order_register.del_element(order)

    def print_register(self):
        """
        Prints all entries in register.
        """
        print()
        print("What kind of register to print?")
        print("Press 1 for book register")
        print("Press 2 for client register")
        print("Press 3 for order register")
        print("Press 4 for writer register")
        print("Press 5 to go back")
        pressed = input("Please press the desired key: ")
        if pressed == "1":
            self.book_register.print_register()
        elif pressed == "2":
            self.client_register.print_register()
        elif pressed == "3":
            self.order_register.print_register()
        elif pressed == "4":
            self.writer_register.print_register()
        elif pressed == "5":
            self.customer_service()
        else:
            print("Invalid key, try again, please.")
            self.del_from_register()
