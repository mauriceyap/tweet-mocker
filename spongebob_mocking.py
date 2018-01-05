from random import random

CONSECUTIVE_CASE_PROBABILITY = 0.35
SWAP_CASE_FIRST_LETTER_PROBABILITY = 0.5


def generate_spongebob_mocking(text):
    swap_case = lambda x: x.lower() if x.isupper() else x.upper()
    mocking_text = u''

    # Maybe change first letter
    while not text[0].isalpha():
        mocking_text += text[0]
        text = text[1:]
    mocking_text += (swap_case(text[0]) if random() < SWAP_CASE_FIRST_LETTER_PROBABILITY else text[0])
    is_previous_char_upper = mocking_text[0].isupper()
    text = text[1:]

    # Prevent three-in-a-row of the same case
    next_alpha_char_must_be_upper = False
    next_alpha_char_must_be_lower = False

    for c in text:
        # ignore non alpha characters
        if not c.isalpha():
            mocking_text += c
            continue

        if next_alpha_char_must_be_upper:
            c = c.upper()
        elif next_alpha_char_must_be_lower:
            c = c.lower()
        else:
            # Maybe change case, considering case of previous character
            is_c_same_case_as_previous = c.isupper() == is_previous_char_upper
            if random() > CONSECUTIVE_CASE_PROBABILITY:
                if is_c_same_case_as_previous:
                    c = swap_case(c)
            else:
                if not is_c_same_case_as_previous:
                    c = swap_case(c)

        # Prevent three-in-a-row of the same case
        next_alpha_char_must_be_lower = c.isupper() and is_previous_char_upper
        next_alpha_char_must_be_upper = c.islower() and not is_previous_char_upper

        is_previous_char_upper = c.isupper()
        mocking_text += c

    return mocking_text
