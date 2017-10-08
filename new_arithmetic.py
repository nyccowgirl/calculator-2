"""Math functions for calculator."""


def add(nums):
    """Return the sum of the numbers in the list."""
    total = 0
    for num in nums:
        total += num
    return total


def subtract(nums):
    """Return the result of subtracting all numbers in the list."""
    total = 0
    for num in nums:
        total -= num
    return total    

def multiply(nums):
    """Multiply all numbers in the list together."""
    total = 0
    for num in nums:
        total *= num
    return total

def divide(nums):
    """Divide the first input by the second and so on and return the result."""
    total = float(nums[0])
    for num in nums[1:]:
        total /= num

    return total

def square(nums):
    """Return the square of the input(s)."""
    for i, num in enumerate(nums):
        nums[i] = num ** 2
    return nums

def cube(nums):
    """Return the cube of the input(s)."""
    for i, num in enumerate(nums):
        nums[i] = num ** 3
    return nums

def power(nums):
    """Raise total to the power of the next number, and return the value."""
    total = float(nums[0])
    for num in nums[1:]:
        total **= num
    return total

def mod(nums):
    """Return the remainder of each input divisible by the following input."""
    total = float(nums[0])
    for num in nums[1:]:
        total %= num
    return total

def add_mult(num1, num2, num3):
    """ Return the sum of two inputs, and multiplies it with a third input."""

    return (num1 + num2) * num3

def add_cubes(num1, num2):
    """ Return the sum of the cube of two inputs."""

    return (num1 ** 3) + (num2 ** 3)
