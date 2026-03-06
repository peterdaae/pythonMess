# class
class CustomerAccount:
    MAX_RETRIES = 3           # constant

    def __init__(self, user_id, initial_balance=0):
        self.user_id = user_id        # instance attribute (snake_case)
        self._cache = {}              # "internal" attribute

    def deposit(self, amount):        # method (snake_case, verb)
        self.balance += amount

# module-level functions
def calculate_interest(balance, rate):
    return balance * rate

# collections use plural names
orders = [(1, "item1"), (2, "item2")]
error_codes = {404: "Not Found", 500: "Server Error"}