"""
Calculator module supporting basic arithmetic operations.
"""


class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return the division of a by b. Raises ValueError on zero division."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b