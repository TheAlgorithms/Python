import logging
import tzlocal
from functools import wraps
from datetime import datetime


def log_entry_and_exit(func):
    '''Log starting time and finish time of funciton'''

    # Setiing local timezone
    local_tz = tzlocal.get_localzone()
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = datetime.now(tz=local_tz)
        logging.info(f"Function '{func.__name__}' started at {start_time}")
        return_value = func(*args,*kwargs)
        end_time = datetime.now(tz=local_tz)
        logging.info(f"Function '{func.__name__}' ended at {end_time}")
        return return_value

    return wrapper

"""
Example usage:
"""


# Function declaration
@log_entry_and_exit
def my_func(name):
    print(f"My name is {name}")

#Fucntion call
my_func("John Doe")
