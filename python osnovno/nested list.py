def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)

def average(grades):
    '''
    (list of list of number) -> list of float
    
    Return a new list in which each item is the average
    of the grades in the inner list at the corresponding
    position of grades.
    
    >>>average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])

    '''

    averages = []

    for grades_list in grades:
        # calculate the average of grades_list and
        # appent it to averages.

        total = 0
        for mark in grades_list:
            total = total + mark
        
        averages.append(total / len(grades_list))

    return averages
