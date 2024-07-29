import os

def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

        >>> read_file_list("abc")
        Traceback (most recent call last): 
        ... 
        NameError: File abc not found!

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    if os.path.exists(filename):
        with open(filename) as file:
            for line in file:
                print(f"- {line.strip()}")
    else:
        raise NameError(f"File {filename} not found!")
