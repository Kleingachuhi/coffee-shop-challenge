# ☕ coffee-shop-challenge
 --> 
# Coffee Shop System

This is a Python implementation of a Coffee Shop system. It allows customers to place orders for coffee, and the system manages relationships between customers, orders, and coffees.

## Classes

### Customer

The `Customer` class represents a customer at the coffee shop. Each customer has a name and a list of orders they’ve placed.

#### Key Methods:

* `__init__(self, name)` – Initializes a customer with a name.
* `name` – A property with validation to ensure the name is a string between 1 and 15 characters.
* `orders()` – Returns a list of the customer’s orders.
* `coffees()` – Returns a list of coffee names from the customer’s orders.
* `create_order(coffee, price)` – Allows the customer to create an order for a specific coffee with a price.
* `add_order_to_orders_list(order)` – Adds an order to the customer’s list of orders.

### Coffee

The `Coffee` class represents a coffee available in the shop. Each coffee has a name, and the system tracks orders associated with that coffee.

#### Key Methods:

* `__init__(self, name)` – Initializes a coffee with a name.
* `name` – A property with validation for a string with at least 3 characters, and the coffee name is immutable after it’s set.
* `orders()` – Returns a list of orders for that coffee.
* `customers()` – Returns a list of customers who ordered that coffee.
* `num_orders()` – Returns the number of orders for that coffee.
* `average_price()` – Returns the average price of orders for that coffee.

### Order

The `Order` class represents an order placed by a customer for a specific coffee. Each order includes the customer, the coffee, and the price.

#### Key Methods:

* `__init__(self, customer, coffee, price)` – Initializes an order with a customer, coffee, and price.
* `price` – A property that ensures the price is a float between 1.0 and 10.0 and is immutable after being set.
* `customer` – A property that returns the customer associated with the order.
* `coffee` – A property that returns the coffee associated with the order.

## How to Use

1. **Create Coffee:**
   Create coffee objects to represent the available coffee options.

2. **Create Customer:**
   Create customers who can place orders.

3. **Create Order:**
   A customer can place an order by selecting a coffee and specifying a price.

4. **View Orders:**
   You can view the orders associated with a customer or a coffee.

5. **Other Functionalities:**

   * The price of an order is immutable after it’s set.
   * You can calculate the average price of orders for a specific coffee.