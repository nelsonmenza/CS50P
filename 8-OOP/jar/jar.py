class Jar:
    def __init__(self, capacity=12):
        # Constructor for the Jar class. Initializes the jar's capacity and size.
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        else:
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        # Returns a string representation of the jar using emojis to indicate its size.
        return self.size * "🍪"

    def deposit(self, n):
        # Deposits cookies into the jar, updating size and capacity accordingly.
        if n <= self.capacity:
            self.size += n
            self.capacity -= n
            return self.size, self.capacity
        else:
            raise ValueError("Deposit amount exceeds capacity")

    def withdraw(self, n):
        # Withdraws cookies from the jar, updating size and capacity accordingly.
        if n <= self.size:
            self.capacity += n
            self.size -= n
            return self.size, self.capacity
        else:
            raise ValueError("Withdrawal amount exceeds current size")

    @property
    def capacity(self):
        # Getter for the capacity property.
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        # Setter for the capacity property. Validates and updates the capacity.
        if capacity >= 0:
            self.__capacity = capacity
        else:
            raise ValueError("Capacity cannot be negative")

    @property
    def size(self):
        # Getter for the size property.
        return self.__size

    @size.setter
    def size(self, size):
        # Setter for the size property.
        self.__size = size
