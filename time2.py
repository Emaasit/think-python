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
        