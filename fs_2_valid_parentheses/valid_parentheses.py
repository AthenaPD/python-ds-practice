def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    
    pleft = pright = 0
    for p in parens:
        if p == "(":
            pleft += 1
        else:
            pright += 1

        if pleft < pright:
            return False
        
    if pleft != pright:
        return False
    
    return True
