'''
   Input -> interger
   output ->add_sum(interger)
   Example -> add_sum(5) : 15
'''
def add_sum(n):
    if(type(n) != int ): raise TypeError

    '''use the legendary formulae to calculate the answer
       n(n + 1) / 2
    '''
    return ((n * (n + 1)) / 2)
