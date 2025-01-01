import random
import string

# Function to generate random passwords


def generate_passwords(length, amount):
    pool = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    passwords = []
    for _ in range(amount):
        password = ''.join(random.choice(pool) for _ in range(length))
        passwords.append(password)
    return passwords

# Radix Sort Function


def radix_sort(passwords, length):
    pool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    char_to_index = {char: index for index, char in enumerate(pool)}

    for position in range(length - 1, -1, -1):
        buckets = [[] for _ in range(62)]

        for password in passwords:
            char = password[position]
            index = char_to_index[char]
            buckets[index].append(password)

        passwords = []
        for bucket in buckets:
            passwords.extend(bucket)

    return passwords

# Main function to handle input and output


def main():
    # Combined input for length and amount
    length, amount = map(int, input(
        "Enter the length and amount of passwords (e.g., 16 1000): ").split())

    # Generate random passwords
    passwords = generate_passwords(length, amount)

    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

    # Sort the passwords using Radix Sort
    sorted_passwords = radix_sort(passwords, length)

    print("\nSorted Passwords:")
    for password in sorted_passwords:
        print(password)


if __name__ == "__main__":
    main()
