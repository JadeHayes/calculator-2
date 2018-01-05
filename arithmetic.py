"""Math functions for calculator."""


def add(nums):
    """Return the sum of the inputs."""
    answer = 0
    for each in nums:
        answer += each
    return answer


def subtract(nums):
    """Subtracted these numbers"""
    answer = nums[0]
    for each in nums[1:]:
        answer -= each
    return answer


def multiply(nums):
    """Multiply the inputs together."""
    answer = nums[0]
    for each in nums[1:]:
        answer *= each
    return answer


def divide(nums):
    """Divide the first input by the second and return the result."""
    answer = nums[0]
    for each in nums[1:]:
        answer /= each
    return answer


def square(nums):
    """Return the square of the input."""
    answer = nums[0] ** 2
    for each in nums[1:]:
        answer *= (each ** 2)
    return answer


def cube(nums):
    """Return the cube of the input."""
    answer = nums[0] ** 3
    for each in nums[1:]:
        answer *= (each ** 3)
    return answer


def power(nums):
    """Raise num1 to the power of num and return the value."""
    answer = nums[0]
    for each in nums[1:]:
        answer = answer ** each
    return answer


def mod(nums):
    """Return the remainder of num / num2."""
    answer = nums[0]
    for each in nums[1:]:
        answer = answer % each
    return answer
