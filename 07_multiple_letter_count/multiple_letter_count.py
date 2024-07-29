def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> freq_dict = multiple_letter_count('yay')
        >>> {'y': 2, 'a': 1} == freq_dict
        True

        >>> freq_dict = multiple_letter_count('Yay')
        >>> {'y': 1, 'Y': 1, 'a': 1} == freq_dict
        True
    """

    return {lett: phrase.count(lett) for lett in set(list(phrase))}
