from random import choices, random, randint, choice, sample

from src.settings import EmailGeneratorSettings


def generate_random_separator(email_gen_settings: EmailGeneratorSettings, heavy_randomizing: bool = True):
    """
    Generate a random separator based on the provided settings.
    If heavy_randomizing is False, which means we are applying almost no randomization,
    we always use a separator to avoid too common names.
    e.g., returns "_"
    """
    put_separator_prb = email_gen_settings.SYMBOL_AS_SEPARATOR_PRB
    separator_weights = email_gen_settings.SEPARATOR_WEIGHTS

    if random() < put_separator_prb or not heavy_randomizing:
        return choices([".", "_", "-"], weights=separator_weights)[0]
    else:
        return ""


def generate_random_domain(email_gen_settings: EmailGeneratorSettings):
    """
    Generate a random domain based on the provided settings.
    e.g., returns "gmail.com"
    """
    possible_domains = email_gen_settings.DOMAINS
    domain_weights = email_gen_settings.DOMAINS_WEIGHTS

    return choices(possible_domains, weights=domain_weights, k=1)[0]


def choose_mutations_to_apply(email_gen_settings: EmailGeneratorSettings):
    """
    Chooses a random number of mutations to apply from a list of mutation types.
    e.g., returns ["leetspeak", "append_digits"]
    """
    num_of_mutations_weights = email_gen_settings.NUM_OF_MUTATIONS_WEIGHTS
    mutation_types = ["random_symbol_insertion", "drop_vowels", "leetspeak", "preppend_digits", "append_digits"]
    num_mutations = choices([1, 2, 3], weights=num_of_mutations_weights)[0]
    return sample(mutation_types, min(num_mutations, len(mutation_types)))


def parse_last_name(last_name: str):
    """
    Parses the last name by selecting a part or combining parts with separators.
    e.g., "doe cari" -> "doe_cari"
    """
    last_name_list = last_name.split(" ")
    return choice([last_name_list[0], last_name_list[1], f"{choice(['', '_', '.'])}".join(last_name_list)])


def randomize_name_and_or_surname(name: str, last_name: str, email_gen_settings: EmailGeneratorSettings):
    """
    Randomly shortens either the name or the surname based on probability.
    e.g., "John", "Doe" -> "Jo", "Doe"
    """
    if random() < email_gen_settings.RANDOMIZE_NAME_VS_SURNAME_PRB:
        name = choice([name[0], name[: (len(name) // choice([2, 3])) + 1]])
    else:
        last_name = choice([last_name[0], last_name[: (len(last_name) // 2) + 1]])
    return name, last_name


def apply_random_symbol_insertion(
    email_str: str, mods_applied: int, mutations_to_apply: list[str], email_gen_settings: EmailGeneratorSettings
):
    """
    Inserts a random symbol or junk string into the email string at a random position.
    e.g., "john" -> "johxn"
    """
    apply_random_insertion_when_also_leet_prb = email_gen_settings.RD_INSERTION_AFTER_VW_OR_LEET

    if "leetspeak" in mutations_to_apply:
        if random() < apply_random_insertion_when_also_leet_prb:
            pos = randint(1, len(email_str))
            if random() < email_gen_settings.RD_INSERTION_PRB:
                junk = choice("0123456789abcdefghijklmnopqrstuvwxyz")
            else:
                junk = choice(["xx", "aa", "bb", "yy", "zz", "vv"])
            email_str = email_str[:pos] + junk + email_str[pos:]
            mods_applied += 1
    else:
        pos = randint(1, len(email_str))
        if random() < email_gen_settings.RD_INSERTION_PRB:
            junk = choice("0123456789abcdefghijklmnopqrstuvwxyz")
        else:
            junk = choice(["xx", "aa", "bb", "yy", "zz", "vv"])
        mods_applied += 1
        email_str = email_str[:pos] + junk + email_str[pos:]

    return email_str, mods_applied


def apply_vowel_drop(email_str: str, mods_applied: int):
    """
    Drops vowels from a random segment of the email string.
    e.g., "john" -> "jhn"
    """
    start = randint(0, len(email_str) - 1)
    end = randint(start + 1, len(email_str))
    segment = email_str[start:end]
    segment_no_vowels = "".join([c for c in segment if c not in "aeiou"])
    mods_applied += 1
    email_str = email_str[:start] + segment_no_vowels + email_str[end:]
    return email_str, mods_applied


def apply_leetspeak(email_str: str, mods_applied: int, email_gen_settings: EmailGeneratorSettings):
    """
    Applies leetspeak transformation to vowels in the email string.
    e.g., "john" -> "j0hn"
    """
    if len(email_str) > 5:
        # Convert string to list for easier character manipulation
        email_chars = list(email_str)
        # Calculate number of characters to convert (50% of total)
        chars_to_convert = choice([len(email_str) // 2, len(email_str) // 3])
        # Get random positions to apply leetspeak
        positions_to_convert = sample(range(len(email_str)), chars_to_convert)
        # Apply leetspeak only at the selected positions
        for pos in positions_to_convert:
            if email_chars[pos] in "aeiou":
                email_chars[pos] = email_chars[pos].translate(email_gen_settings.VOWELS_MAP)
        email_str = "".join(email_chars)
        mods_applied += 1
    else:
        mods_applied += 1
        email_str = email_str.translate(email_gen_settings.VOWELS_MAP)

    return email_str, mods_applied


def preppend_random_digit(mods_applied: int, email_gen_settings: EmailGeneratorSettings):
    """
    Prepends a random digit or digits to the email string based on probability.
    e.g., returns "1" (for "john" -> "1john")
    """
    if random() < email_gen_settings.DIGITS_AS_PREFIX_PRB:
        if random() < email_gen_settings.SINGLE_DIGIT_PREFIX_TYPE_PRB:
            random_prefixed_digit = str(randint(1, 9))
            mods_applied += 1
        else:
            random_prefixed_digit = "".join([str(randint(1, 9)) for _ in range(randint(1, 2))])
            mods_applied += 1
    else:
        random_prefixed_digit = ""

    return random_prefixed_digit, mods_applied


def append_random_digits(mods_applied: int, email_gen_settings: EmailGeneratorSettings, heavy_mod: bool = True):
    """
    Appends random digits, such as birth year or random numbers, to the email string.
    e.g., returns "1985" (for "john_doe" -> "john_doe1985")
    """
    if heavy_mod:
        append_type = choices(
            ["birth_year", "random_digits", "eighty_ninety"], weights=email_gen_settings.APPENDED_DIGITS_WEIGHTS, k=1
        )[0]
    else:
        append_type = choice(["birth_year", "random_digits"])

    if append_type == "birth_year":
        random_appended_digits = str(randint(1900, 2025))
        mods_applied += 1
    elif append_type == "random_digits":
        random_appended_digits = "".join([str(randint(0, 9)) for _ in range(randint(1, 3))])
        mods_applied += 1
    else:  # eighty_ninety
        random_appended_digits = str(randint(80, 99))
        mods_applied += 1

    return random_appended_digits, mods_applied


def duplicate_random_letter(name: str, last_name: str):
    """
    Duplicates a random letter in either the name or the surname.
    e.g., "John", "Doe" -> "Johhn", "Doe"
    """
    if random() < 0.5:
        letter_to_duplicate_index = choice(range(len(name)))
        name = name[:letter_to_duplicate_index] + name[letter_to_duplicate_index] + name[letter_to_duplicate_index:]
    else:
        letter_to_duplicate_index = choice(range(len(last_name)))
        last_name = (
            last_name[:letter_to_duplicate_index] + last_name[letter_to_duplicate_index] + last_name[letter_to_duplicate_index:]
        )
    return name, last_name
