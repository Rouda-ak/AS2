class EBook:
    """Represents an EBook with details like title, author, publication date, genre, and price."""

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    @property
    def price(self):
        """Getter for price."""
        return self.__price

    def __str__(self):
        """Returns a string representation of the EBook."""
        return f"EBook(title={self.__title}, author={self.__author}, price={self.__price:.2f})"


class Customer:
    """Represents a customer with name, contact information, and membership status."""

    def __init__(self, name, contact_info, membership_status="regular"):
        self.__name = name
        self.__contact_info = contact_info
        self.__membership_status = membership_status
        self.__orders = []
        self.shopping_cart = ShoppingCart()

    def add_order(self, order):
        """Adds an order to the customer's list of orders."""
        self.__orders.append(order)

    @property
    def is_loyalty_member(self):
        """Checks if the customer is a loyalty program member."""
        return self.__membership_status == "loyalty"

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer(name={self.__name}, membership_status={self.__membership_status})"


class ShoppingCart:
    """Represents a shopping cart that holds e-books temporarily before purchase."""

    def __init__(self):
        self.__items = []

    def add_ebook(self, ebook):
        """Adds an e-book to the shopping cart."""
        if isinstance(ebook, EBook):
            self.__items.append(ebook)

    def remove_ebook(self, ebook):
        """Removes an e-book from the shopping cart."""
        if ebook in self.__items:
            self.__items.remove(ebook)

    def get_total(self):
        """Calculates the total price of items in the cart."""
        return sum(item.price for item in self.__items)

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        return f"ShoppingCart with {len(self.__items)} items, Total: {self.get_total():.2f}"


class Order:
    """Represents an order containing purchased e-books, along with total amount and discount information."""

    VAT_RATE = 0.08  # Value-added tax rate

    def __init__(self, purchased_ebooks, customer):
        self.__purchased_ebooks = purchased_ebooks  # List of e-books in the order
        self.__customer = customer  # Associated customer
        self.__total_amount = sum(ebook.price for ebook in purchased_ebooks)
        self.__discount_amount = 0
        self.apply_discounts()

    def apply_discounts(self):
        """Applies discounts based on loyalty status and quantity of e-books purchased."""
        if len(self.__purchased_ebooks) >= 5:
            self.__discount_amount += 0.20 * self.__total_amount
        if self.__customer.is_loyalty_member:
            self.__discount_amount += 0.10 * self.__total_amount

    def calculate_final_price(self):
        """Calculates the final price after discounts and VAT."""
        final_price = (self.__total_amount - self.__discount_amount) * (1 + Order.VAT_RATE)
        return final_price

    def __str__(self):
        """Returns a string representation of the order."""
        return f"Order(Total: {self.__total_amount:.2f}, Discount: {self.__discount_amount:.2f}, Final: {self.calculate_final_price():.2f})"


class Invoice:
    """Represents an invoice generated based on an order, with VAT and discount details."""

    def __init__(self, order):
        self.__order = order
        self.__vat_amount = Order.VAT_RATE * (order.calculate_final_price() - order._Order__discount_amount)
        self.__discount_amount = order._Order__discount_amount
        self.__final_amount = order.calculate_final_price()

    def generate(self):
        """Generates a formatted invoice."""
        return (f"--- Invoice ---\nOrder Total: {self.__order._Order__total_amount:.2f}\n"
                f"Discount Applied: {self.__discount_amount:.2f}\nVAT: {self.__vat_amount:.2f}\n"
                f"Final Amount Due: {self.__final_amount:.2f}")

    def __str__(self):
        """Returns a string representation of the invoice."""
        return self.generate()


class EBookStore:
    """Represents an e-book store that manages customers and a catalog of e-books."""

    def __init__(self):
        self.__ebooks_catalog = []  # List of e-books in the store
        self.__customer_accounts = []  # List of customers

    def add_ebook(self, ebook):
        """Adds an e-book to the store catalog."""
        if isinstance(ebook, EBook):
            self.__ebooks_catalog.append(ebook)

    def add_customer(self, customer):
        """Registers a new customer in the store."""
        if isinstance(customer, Customer):
            self.__customer_accounts.append(customer)

    def __str__(self):
        """Returns a string representation of the e-book store."""
        return (f"EBookStore with {len(self.__ebooks_catalog)} e-books and "
                f"{len(self.__customer_accounts)} customers")
