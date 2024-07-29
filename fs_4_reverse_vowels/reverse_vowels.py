def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = [lett for lett in s if lett.lower() in "aeiou"]
    vowels.reverse()

    s_reversed = list(s)

    i = 0
    for idx, char in enumerate(s_reversed):
        if char.lower() in "aeiou":
            s_reversed[idx] = vowels[i]
            i += 1

    return "".join(s_reversed)
