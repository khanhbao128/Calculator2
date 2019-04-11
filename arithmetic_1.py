"""Math functions for calculator."""




def add(nums):
    """Return the sum of a list of inputs."""
    total = 0
    for num in nums:
        total = total + num
    return total


def subtract(nums):
    """Return the second number subtracted from the first."""
    total = nums[0]
    for i in range(1, len(nums)):
        total = total - nums[i]
    return total


def multiply(nums):
    """Multiply the inputs together."""
    total = 1
    for num in nums:
        total = total * num
    return total


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
