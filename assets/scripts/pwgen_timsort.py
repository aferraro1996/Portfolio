import random
import string
import time
import multiprocessing

# Function to generate random passwords


def generate_passwords(length, amount):
    pool = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    passwords = []
    for _ in range(amount):
        password = ''.join(random.choice(pool) for _ in range(length))
        passwords.append(password)
    return passwords

# Parallel generation of passwords


def parallel_generate_passwords(length, amount, num_processes):
    # Divide the amount of passwords to generate across the number of processes
    chunk_size = amount // num_processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        result = pool.starmap(generate_passwords, [
                              (length, chunk_size)] * num_processes)
    # Flatten the list of results
    return [password for sublist in result for password in sublist]

# Sort the passwords (Timsort)


def timsort(passwords):
    # Sorting based on natural order
    return sorted(passwords, key=lambda x: (x, x))

# Main function to handle input and output


def main():
    # Input for length and amount
    length, amount = map(int, input(
        "Enter the length and amount of passwords (e.g., 16 1000): ").split())
    # Using the number of CPU cores available
    num_processes = multiprocessing.cpu_count()

    # Measure the time taken for multiple iterations for more stable results
    num_iterations = 10
    execution_times = []

    for _ in range(num_iterations):
        start_time = time.time()

        # Generate passwords in parallel
        passwords = parallel_generate_passwords(length, amount, num_processes)

        # Sort the passwords using Timsort
        sorted_passwords = timsort(passwords)

        end_time = time.time()
        execution_times.append(end_time - start_time)

    # Calculate the average execution time
    total_time = sum(execution_times)
    avg_time = total_time / num_iterations
    avg_time_per_password = avg_time / amount

    print(f"\nAverage Time for {num_iterations} runs: {avg_time:.4f} seconds")
    print(f"Approximate time per password: {
          avg_time_per_password:.8f} seconds")


if __name__ == "__main__":
    main()
