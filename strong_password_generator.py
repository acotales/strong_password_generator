"""
    strong_password_generator - Generates a strong password string of 12 to 32 characters

    :author: Anthony Cotales
    :email: acotales@protonmail.com
    :version: 1.1 (27-08-2022)
    :tribute: To my late mother's 40 days (T.T)
"""
import string
import random


def generate_password(length=14):
    """Create and return a suggested strong password string
    with a length of 12 to 32 characters"""

    def getsample() -> str:
        """Returns a string of 8 unique characters"""
        digits = random.sample(string.digits, 2)
        punctuation = random.sample(string.punctuation, 2)
        uppercased = random.sample(string.ascii_uppercase, 2)
        lowercased = random.sample(string.ascii_lowercase, 2)
        unique_string = digits + punctuation + uppercased + lowercased
        return str().join(set(unique_string))

    def strengthen(password):
        """The strength of a password is a function of
        length, complexity, and unpredictability."""

        def string_type(s):
            if s.isupper():
                s = "uppercase"
            elif s.islower():
                s = "lowercase"
            elif s.isnumeric():
                s = "numeric"
            elif not s.isalpha() and not s.isnumeric():
                s = "punctuation"
            elif s.isspace():
                s = "whitespace"
            return s

        # Using a while loop to arrange the characters in a nonconsecutive order
        while True:
            # Boolean list to determine if the string is in nonconsecutive order
            nonconsecutive = [
                string_type(password[i]) != string_type(password[i + 1])
                for i in range(len(password) - 1)
            ]
            # Break out of the loop when conditions are satisfied
            if all(nonconsecutive):
                break
            # If conditions are not met rearrange the order of characters
            password = str().join(random.sample(password, len(password)))
        # Return the strengthen password string
        return password

    # Required minimum of 12 and maximum 32 length of strong password string
    minimum, maximum = (12, 32)
    # Excluded confusing characters for password string
    excluded = "\"(),./:;<>'[\\]`{}~"
    # A single line of conditional statements place into a variable
    length = minimum if length < minimum else maximum if length > maximum else length

    # Accumulate strings from getsample() method 32 times (8*32=256)
    # and selecting characters that are not in the excluded list and no duplicates
    selection = str()

    for _ in range(maximum):
        sample = getsample()
        for n in sample:
            if n not in excluded and n not in selection:
                selection += n

    # Lastly return the selected string with the desired length
    return strengthen(selection[:length])
