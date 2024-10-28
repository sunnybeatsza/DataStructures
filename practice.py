import random


def generate_random_list(length):
    """Generate a list of random numbers of a given length
     Examples: generate_random_list(5)
     Output: [81, 96, 77, 64, 49]
        >>>
    """
    return [random.randint(0, 100) for number in range(length)]

print(generate_random_list(5))

numbers = [1, 2, 3, 4, 5]

def find_average(numbers):
    """Find the average of a list of numbers
    Examples: find_average([1, 2, 3, 4, 5])
     Output: 3.0
    """
    
    return sum(numbers) / len(numbers)

print(find_average([1, 2, 3, 4, 5]))