def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

# Example: Generate the first 10 Fibonacci numbers
result = generate_fibonacci(10)
print(result)
