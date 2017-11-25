"""This is Chapter 16: Classes and functions

Learning Python programming using the book titled

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2017 Daniel Emaasit

License: http://creativecommons.org/licenses/by/4.0/
"""

class Time:
    """Represents the time of day.
    
    Attributes
    ----------
    
    hour, minute, second
    """
    
def print_time(t):
    """Prints the time in hour:minute:second format
    
    Parameters
    ----------
    
    t : Time
     t is a Time object
    
    Returns
    -------
    
    a printout of time
    """
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))    
    
def is_after(t1, t2):
    """Returns True is t1 is after t2; false otherwise
    
    Parameters
    ----------
    t1 : Time
    t2 : Time
    """
    return(t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second) 

def add_time(t1, t2):
    """Returns the sum t1 and t2
    
    Parameters
    ----------
    t1 : Time
    t2 : Time
    
    Returns
    -------
    sum : Time 
    """
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    while sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
        
    while sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

def time_to_int(time):
    """Computes the number of seconds since midnight
    
    Parameters
    ----------
    
    time : a Time object
    
    Returns
    -------
    
    seconds
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """Converts integer to Time object
    
    Parameters
    ----------
    
    seconds : Time
       integer seconds since midnight
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time2(t1, t2):
    """Returns a new Time object by adding t1 and t2
    
    Parameters
    ----------
    
    t1 : Time
    t2 : Time
    
    Returns
    -------
    
    a Time object
    """
    seconds = time_to_int(t1) + time_to_int(t2)
    new_time = int_to_time(seconds)
    return new_time

def validate_time(time):
    """Valid the Time objects
    
    Parameters
    ----------
    
    time : a Time object
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time3(t1, t2):
    """Return the sum of two Time objects
    
    Parameters
    ----------
    
    t1 : Time object
    t2 : Time object
    """
    assert validate_time(t1) and validate_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    new_time = int_to_time(seconds)
    return new_time