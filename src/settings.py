class EmailGeneratorSettings:
    # Name mutation probabilities
    RANDOMIZE_EITHER_SUR_OR_NAME_PRB = 0.4
    RANDOMIZE_NAME_VS_SURNAME_PRB = 0.55
    HEAVY_RANDOMIZING_PRB = 0.8

    # Email structure probabilities
    SYMBOL_AS_SEPARATOR_PRB = 0.65
    SEPARATOR_WEIGHTS = [0.4, 0.5, 0.1]  # [".", "_", "-"]
    DIGITS_AS_PREFIX_PRB = 0.6
    SINGLE_DIGIT_PREFIX_TYPE_PRB = 0.55
    DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "proton.me", "protonmail.com", "icloud.com"]
    DOMAINS_WEIGHTS = [0.598, 0.055, 0.048, 0.048, 0.012, 0.012, 0.227]

    # Random insertion probabilities
    RD_INSERTION_PRB = 0.55
    RD_INSERTION_AFTER_VW_OR_LEET = 0.3  # kept low to avoid bot-like emails

    # Mutation weights
    APPENDED_DIGITS_WEIGHTS = [0.6, 0.25, 0.15]  # birth_year (e.g 1999, 2004), random_digits (up to three digits), 80-99
    NUM_OF_MUTATIONS_WEIGHTS = [0.5, 0.35, 0.15]  # 1, 2, 3 (e.g, 2 mutations to apply)

    # Fallback probabilities (when no heavy mutations are applied)
    DUPLICATE_LETTER_WHEN_NO_HEAVY_PRB = 0.9
    APPEND_NUMBER_WHEN_NO_MOD_PRB = 0.9

    # Email constraints
    MAX_DIGITS_IN_EMAIL = 4
    MIN_DIGITS_IN_EMAIL = 0
    MIN_EMAIL_LENGTH = 8

    # Character mapping
    VOWELS_MAP = str.maketrans("aeiou", "12345")


SETTINGS = EmailGeneratorSettings()
