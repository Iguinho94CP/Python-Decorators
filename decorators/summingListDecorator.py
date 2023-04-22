from functools import wraps

def sumlist(array):
	count = 0
	for item in range(len(array)):
		count += array[item]
	return count

def summingList(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		if not isinstance(result, (list, int)):
			raise TypeError('Result must be a list')
		if isinstance(result, list):
			return sumlist(result)
		return result
	return wrapper