def convert_to_minutes(num_hours):
    ''' (int)->int
    Return the number of minutes there are in sum_hours hours.
    >>> convert_to_minutes(2)
    120
    '''
    result = num_hours * 60
    return result

def convert_to_sec(num_hours):
    ''' (int)->int
    Return the number of minutes there are in sum_hours hours.
    >>> convert_to_minutes(1)
    3600
    '''
    result = num_hours * 3600
    return result

def minsec(num_hours):
    ''' (int)->int
    Return the number of minutes there are in sum_hours hours.
    >>> convert_to_minutes(1)
    3660
    '''
    result = num_hours * 60
    return convert_to_minutes(num_hours)+convert_to_sec(num_hours)
