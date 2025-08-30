from random import random

from src.settings import SETTINGS  # type: ignore
from src.random_choices import (
    randomize_name_and_or_surname,
    apply_random_symbol_insertion,
    generate_random_separator,
    choose_mutations_to_apply,
    duplicate_random_letter,
    generate_random_domain,
    preppend_random_digit,
    append_random_digits,
    apply_vowel_drop,
    parse_last_name,
    apply_leetspeak,
)  # type: ignore


def generate_email(name: str, last_name: str):
    """
    Generate a random email address based on the provided name and last name.
    All random modifications are marked with the counter (x/10) in the comments.
    """
    name = name.lower()
    last_name = last_name.lower()

    # (1/10) Decide on name-surname separator ("", ".", "_" or "-")
    separator = generate_random_separator(SETTINGS)

    # Generate random domain (e.g., gmail.com, yahoo.com, protonmail.com etc.)
    random_domain = generate_random_domain(SETTINGS)

    # Initialize loop variables
    random_email = "x"
    random_email_username = "x"
    num_of_digits_in_email_counter = 0

    while (len(random_email_username) < SETTINGS.MIN_EMAIL_LENGTH) or (
        SETTINGS.MIN_DIGITS_IN_EMAIL < num_of_digits_in_email_counter > SETTINGS.MAX_DIGITS_IN_EMAIL
    ):
        # (2/10) Randomly select which mutations to apply
        mutations_to_apply = choose_mutations_to_apply(SETTINGS)
        mutations_applied_counter = 0

        # (3/10) Parse last_name and keep either first, last or join'em with separator
        if " " in last_name:
            last_name = parse_last_name(last_name)

        # (4/10) Decide whether to heavily randomize or not
        if random() < SETTINGS.HEAVY_RANDOMIZING_PRB:
            # (5/10) Randomize name
            if random() < SETTINGS.RANDOMIZE_EITHER_SUR_OR_NAME_PRB:
                name, last_name = randomize_name_and_or_surname(name, last_name, SETTINGS)
                mutations_applied_counter += 1

            # From here on randomizations are applied in the email username
            email_str = f"{name}{separator}{last_name}"

            # (6/10) Introduce random digit or letter
            if "random_symbol_insertion" in mutations_to_apply:
                email_str, mutations_applied_counter = apply_random_symbol_insertion(
                    email_str, mutations_applied_counter, mutations_to_apply, SETTINGS
                )

            # (7/10) Drop vowels in a random range
            if "drop_vowels" in mutations_to_apply:
                email_str, mutations_applied_counter = apply_vowel_drop(email_str, mutations_applied_counter)

            # (8/10) Translate vowels to numbers
            if "leetspeak" in mutations_to_apply:
                email_str, mutations_applied_counter = apply_leetspeak(email_str, mutations_applied_counter, SETTINGS)

            # (9/10) Preppend random digit. Skip if leetspeak was applied because results would be too bot-like
            if "preppend_digits" in mutations_to_apply and "leetspeak" not in mutations_to_apply:
                random_prefixed_digit, mutations_applied_counter = preppend_random_digit(mutations_applied_counter, SETTINGS)
            else:
                random_prefixed_digit = ""

            # (10/10) Append random digits
            if "append_digits" in mutations_to_apply or mutations_applied_counter == 0:
                random_appended_digits, mutations_applied_counter = append_random_digits(mutations_applied_counter, SETTINGS)
            else:
                random_appended_digits = ""

            random_email = f"{random_prefixed_digit}{email_str}{random_appended_digits}@{random_domain}"

        else:
            separator = generate_random_separator(SETTINGS, heavy_randomizing=False)

            # (2/3) Randomly duplicate single letter
            if random() < SETTINGS.DUPLICATE_LETTER_WHEN_NO_HEAVY_PRB:
                name, last_name = duplicate_random_letter(name, last_name)

            # (3/3) Randomly append number to last name
            if random() < SETTINGS.APPEND_NUMBER_WHEN_NO_MOD_PRB:
                random_appended_digits, _ = append_random_digits(0, SETTINGS, False)
                last_name = last_name + random_appended_digits

            random_email = f"{name}{separator}{last_name}@{random_domain}"  # this last_name may have digits appended from (3/3)

        random_email_username = random_email[: random_email.find("@")]

        num_of_digits_in_email_counter = sum(c.isdigit() for c in random_email_username)

    return random_email
