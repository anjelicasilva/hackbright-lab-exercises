import random

"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax)
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'Christmas melon':
            base_price = base_price * 1.5
        if order_type == 'international' and self.qty < 10:
            flat_fee = 3
            base_price = base_price + flat_fee
        total = (1 + self.tax) * self.qty * base_price

    def get_base_price(self):
        base_price = random.randrange(5,10)

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
#     There will be no tax on government orders.
# The GovernmentMelonOrder class should include:
# a variable passed_inspection which is False until a successful inspection occurs
# a method mark_inspection(passed) that takes a Boolean input, passed, and updates whether or not the melon has passed inspection. This method should update the attribute passed_inspection.

    def __init__(self):
        super().__init__(self, species, qty)
        self.species = species
        self.qty = qty
        self.order_type = 'government'
        self.tax = 0.0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(self, species, qty, 'domestic', 0.08)

    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(self, species, qty, 'international', 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
