from ebookstore import EBook, Customer, ShoppingCart, Order, Invoice, EBookStore

# Initialize the e-book store
store = EBookStore()

# Create e-books
ebook1 = EBook("Python Basics", "John Doe", "2021-06-01", "Programming", 29.99)
ebook2 = EBook("Advanced Python", "Jane Smith", "2022-02-15", "Programming", 49.99)

# Add e-books to the store catalog
store.add_ebook(ebook1)
store.add_ebook(ebook2)

# Display the e-books in the store
print("E-Books available in the store:")
print(ebook1)
print(ebook2)
print()

# Create a customer
customer = Customer("Alice Brown", "alice@example.com", "loyalty")
store.add_customer(customer)

# Customer adds e-books to their shopping cart
customer.shopping_cart.add_ebook(ebook1)
customer.shopping_cart.add_ebook(ebook2)

# Display shopping cart details
print("Shopping Cart:")
print(customer.shopping_cart)
print()

# Create an order from shopping cart items
order = Order(customer.shopping_cart._ShoppingCart__items, customer)  # Accessing private items for demonstration
customer.add_order(order)

# Display order details
print("Order Details:")
print(order)
print()

# Generate and print an invoice for the order
invoice = Invoice(order)
print("Invoice:")
print(invoice)
print()
