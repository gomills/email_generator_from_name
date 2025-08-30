import numpy as np

from src.generate_rd_email import generate_email  # type: ignore


def generate_x_emails(x: int):
    first_name = "Maria"
    last_name = "Carreras"

    for _ in range(x):
        email = generate_email(name=first_name, last_name=last_name)
        print(email)


def generate_emails_array_length_x(x: int):
    first_name = "Maria"
    last_name = "Carreras"
    return np.array([generate_email(name=first_name, last_name=last_name) for _ in range(x)])


def duplicates_proportion(emails_array: np.ndarray):
    counts = np.unique(emails_array, return_counts=True)[1]
    duplicates_count = np.sum(counts[counts > 1] - 1)
    return duplicates_count / len(emails_array)


if __name__ == "__main__":
    num_of_emails = 1000000
    # emails_array = generate_x_emails(50)
    emails_array = generate_emails_array_length_x(num_of_emails)
    duplicates_proportion_count = duplicates_proportion(emails_array)
    print(f"\n{duplicates_proportion_count:.2%} duplicates")
