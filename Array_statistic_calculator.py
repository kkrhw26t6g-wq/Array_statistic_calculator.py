def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    # Start assuming the first number is the maximum
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def calculate_minimum(numbers):
    # Start assuming the first number is the minimum
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main():
    count = int(input("How many numbers? "))

    # Check if N is a positive integer
    if count <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = []

    # Collect the numbers from the user
    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    print("\nResults:")
    print("Sum:     ", calculate_sum(numbers))
    print("Average: ", calculate_average(numbers))
    print("Maximum: ", calculate_maximum(numbers))
    print("Minimum: ", calculate_minimum(numbers))
main()





