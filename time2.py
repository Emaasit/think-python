"""This is Chapter 17: Classes and methods

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
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        """Initializes a Time object
        
        Parameters
        ----------
        hour : int
        minute : int
        second : int or float
        
        Return
        ------
        Time object
        """
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        """Returns a string representation of a time object      
        """
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)
    
    def print_time(self):
        """Prints the time in hour:minute:second format
        
        Parameters
        ----------
    
       t : Time
       t is a Time object
    
       Returns
       -------
    
       a printout of time
       """
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)) 
        
        
    def time_to_int(self):
        """Computes the number of seconds since midnight
    
        Parameters
        ----------
    
        time : a Time object
    
        Returns
        -------
    
        seconds
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds 
    
    
    def increment(self, seconds):
        """Computes the number of seconds since midnight

        Parameters
        ----------

        seconds : int

        Returns
        -------

        a Time object
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        """Returns True is t1 is after t2; false otherwise
    
        Parameters
        ----------
        self : Time
        other : Time
        """
        return self.time_to_int() > other.time_to_int()
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def __add__(self, other):
        """Returns the sum of two Time objects or Time object and an integer
    
        Parameters
        ----------
        self : Time
        other : Time or int
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)

def int_to_time(seconds):
    """Converts integer to Time object

    Parameters
    ----------

    seconds : int
        integer seconds since midnight
    
    Returns
    -------
    
    time : a Time object
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time  

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()
    
if __name__ == "__main__":
    main()