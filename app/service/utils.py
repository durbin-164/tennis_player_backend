import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start Time: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"End Time: {end_time}")
        print(f'{func.__name__} took {end_time-start_time:4f} seconds')
        return result
    return wrapper