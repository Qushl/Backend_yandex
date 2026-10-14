class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} ({self.price:.2f} руб.; в наличии: {self.stock})"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)


class Order:
    def __init__(self, customer, items, discount_percent=0, tax_rate=0):
        if not items:
            raise ValueError("Корзина пустая")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100")
        self.customer = customer
        self.items = dict(items)
        self.discount_percent = discount_percent
        self.tax_rate = tax_rate
        self.processed = False

    @property
    def subtotal(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    @property
    def discount_amount(self):
        return self.subtotal * self.discount_percent / 100

    @property
    def tax_amount(self):
        return (self.subtotal - self.discount_amount) * self.tax_rate

    @property
    def total(self):
        return self.subtotal - self.discount_amount + self.tax_amount

    def process(self):
        if self.processed:
            print("Заказ уже оформлен")
            return
        for product, quantity in self.items.items():
            if product.stock < quantity:
                raise ValueError("Недостаточно товара на складе")
        for product, quantity in self.items.items():
            product.stock -= quantity
        self.processed = True
        self.customer.add_order(self)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")
        current_quantity = self.items.get(product, 0)
        if current_quantity + quantity > product.stock:
            raise ValueError("Недостаточно товара на складе")
        self.items[product] = current_quantity + quantity

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        if product not in self.items:
            return
        if quantity == 0:
            self.remove_product(product)
        elif quantity > 0 and quantity <= product.stock:
            self.items[product] = quantity
        else:
            raise ValueError("Неверное количество товара")

    def checkout(self, customer, discount_percent=0, tax_rate=0):
        order = Order(customer, self.items, discount_percent, tax_rate)
        order.process()
        self.items.clear()
        return order


if __name__ == "__main__":
    laptop = Product("Ноутбук", 80000, stock=4, category="Электроника")
    mouse = Product("Мышь", 2500, stock=10, category="Аксессуары")
    customer = Customer("Мария", "maria@example.com")
    cart = ShoppingCart()
    cart.add_product(laptop)
    cart.add_product(mouse, 2)

    order = cart.checkout(customer, discount_percent=10, tax_rate=0.2)
    print(f"Заказ покупателя {customer.name}: {order.total:.2f} руб.")
    print(f"Заказов в истории: {len(customer.order_history)}")
