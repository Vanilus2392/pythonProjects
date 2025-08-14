def is_even(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
            result = is_even(number)
            print(f"The number {number} is {result}.")
        except ValueError:
            print("Please enter a valid integer.")
        user_input = input("Do you want to check another number? (yes/no): ")
        if user_input.lower() != 'yes':
            print("Exiting the program.")
            break

main()