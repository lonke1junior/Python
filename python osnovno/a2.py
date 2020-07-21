def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1)>get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    broj = 0
    for char in dna:
        if char == nucleotide :
            broj = broj + 1
    return broj

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna1.find(dna2)>=0:
        return True
    return False

def is_valid_sequence(dna):
    ''' (str) -> bool
    
    Return True if and oly if the DNA sequence is vaild.

    >>>is_vaild_sequence('ATGGCAT')
    True
    >>>is_vaild_sequence('ATGZAH')
    False    
    '''
    for char in dna:
        if char !='A' and char !='T' and char !='C' and char !='G':
            return False
    return True    

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index. 

    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    '''
    i=0
    result = ''
    for char in dna1:
        i=i+1
        if i == index:
            result = result + char + dna2
        else:
            result = result + char
    return result

def get_complement(dna):
    '''(str)->str

    Return the DNA complementary.

    >>>get_complement('ACGTACG')
    TGCATGC
    '''
    result = ''
    for char in dna:
        if char == 'A':
            result = result + 'T'
        if char == 'T':
            result = result + 'A'
        if char == 'G':
            result = result + 'C'
        if char == 'C':
            result = result + 'G'
    return result

def get_complementary_sequence(dna):
    '''(str)->str

    Return the DNA sequence that is complementary to the given
    DNA sequence.

    >>>get_complementary_sequence('AT')
    'TA'

    '''
    return get_complement(dna)













    

























