def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # flipped_lett = [lett.lower() if lett == to_swap.upper() 
    #                 else (lett.upper() if lett == to_swap.lower() 
    #                       else lett) 
    #                 for lett in list(phrase)]
    
    flipped_lett = [lett.swapcase() if lett.lower() == to_swap.lower() else lett for lett in phrase]
    
    return "".join(flipped_lett)
