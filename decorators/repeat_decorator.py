def repeat(num):
    """
    A decorator function that repeats the execution of the decorated function `num` times.

    Parameters:
    num (int): The number of times to repeat the decorated function.

    Returns:
    function: The wrapper function that is used as the decorated function.
    """
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for item in range(num):
                print(result)
            return result
        return wrapper
    return decorator_func

@repeat(5)
def say_hello(name):
	"""
	A function that returns 'Hello, ' + name + '!'
	"""
	res ="Hello, " + name + "!"
	return res

test = say_hello('Igor')
print(test)
