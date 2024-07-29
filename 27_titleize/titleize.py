def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    word_list = phrase.split(" ")

    capitalized = [word[0].upper() + word[1:].lower() for word in word_list]

    return " ".join(capitalized)
