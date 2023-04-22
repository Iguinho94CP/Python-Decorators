from functools import wraps

def sumlist(array):
    """Returns the sum of all the items in a list."""
    count = 0
    for item in range(len(array)):
        count += array[item]
    return count

def summingList(func):
    """
    Decorator that can be used to check if the result of the decorated function is a list, and if so,
    returns the sum of all the items in the list. If the result is not a list, it is returned as is.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (list, int)):
            raise TypeError('Result must be a list')
        if isinstance(result, list):
            return sumlist(result)
        return result
    return wrapper

@summingList
def myFunction(myList):
    return myList

print(myFunction([1, 2, 3]))  # Output: 6
print(myFunction(10))  # Raises TypeError: Result must be a list
