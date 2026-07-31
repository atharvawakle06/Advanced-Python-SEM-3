# Fibonacci Assignment using OOP (Recursion + Dynamic Programming)

class Fibonacci:
    def __init__(self, n):
        self.n = n

    # Recursive Method
    def recursive(self, n=None):
        if n is None:
            n = self.n

        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)

    # Dynamic Programming (Iterative Method)
    def dynamic(self):
        n = self.n

        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return b

    # Display full Fibonacci sequence
    def display_sequence(self):
        sequence = []
        a, b = 0, 1

        for i in range(self.n):
            sequence.append(a)
            a, b = b, a + b

        return sequence


# Main Program
def main():
    print("=== Fibonacci Calculator ===")

    # Take input
    n = int(input("Enter value of n: "))

    fib = Fibonacci(n)

    print("\nChoose Method:")
    print("1. Recursive")
    print("2. Dynamic Programming")

    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        result = fib.recursive()
        print(f"\nFibonacci number at position {n} (Recursive): {result}")

    elif choice == 2:
        result = fib.dynamic()
        print(f"\nFibonacci number at position {n} (Dynamic): {result}")

    else:
        print("Invalid choice!")

    # Display full sequence
    print("\nFibonacci Sequence:")
    print(fib.display_sequence())


# Run program
if __name__ == "__main__":
    main()