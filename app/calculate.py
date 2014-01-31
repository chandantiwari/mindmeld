
''' Myers-Briggs test evaluation in Python. Input 'choices' is flattened list of
answers containing -1,0,1 corresponding to leftmost, center, rightmost
selections of radio boxes on the questionaire.
'''
def calculate_mb(choices):

    new_choices = []
    
    ''' The MB questionare is divided into a 10 x 7 table (actually 10 x 14, but
    we use values to represent selections between A,B). The evaluation is
    performed on this table by summing up columns in a certain way. The code
    below simply creates the necessary indexes so that we can read a flattened
    questinaire in a way we can use the 'sum' operation properly.
    '''
    for i in range(1,8):
        new_choices.append([int(choices[j-1]) for j in range(i,71,7) ])

    #print new_choices
        
    # apparently setting a single character in a string using
    # the [] operator is not possible, so we start with a list, then 
    # go back to string when we are finished.
    res = list("XXXX")

    ei = sum(new_choices[0])
    if ei < 0: res[0] = 'E'
    else: res[0] = 'I'
    
    sn = sum(new_choices[1]) + sum(new_choices[2])
    if sn < 0: res[1] = 'S'
    else: res[1] = 'N'
    
    tf = sum(new_choices[3]) + sum(new_choices[4])
    if tf < 0: res[2] = 'T'
    else: res[2] = 'F'

    jp = sum(new_choices[5]) + sum(new_choices[6])
    if jp < 0: res[3] = 'J'
    else: res[3] = 'P'
    
    return str(''.join(res))

