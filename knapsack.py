# knapsack.py

# ---------------------------------------------------------
# TOP-DOWN APPROACH (Memoization)
# ---------------------------------------------------------

def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Create memoization table
    dp = [[-1 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    def solve(i, remaining_capacity):
        # Base case
        if i == 0 or remaining_capacity == 0:
            return 0

        # Return already calculated result
        if dp[i][remaining_capacity] != -1:
            return dp[i][remaining_capacity]

        # If current item is too heavy, don't select it
        if weights[i - 1] > remaining_capacity:
            dp[i][remaining_capacity] = solve(
                i - 1, remaining_capacity
            )

        else:
            # Option 1: Don't select the item
            exclude = solve(i - 1, remaining_capacity)

            # Option 2: Select the item
            include = values[i - 1] + solve(
                i - 1,
                remaining_capacity - weights[i - 1]
            )

            # Choose maximum value
            dp[i][remaining_capacity] = max(include, exclude)

        return dp[i][remaining_capacity]

    return solve(n, capacity)


# ---------------------------------------------------------
# BOTTOM-UP APPROACH (Tabulation)
# ---------------------------------------------------------

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with capacity w
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If item can fit
            if weights[i - 1] <= w:

                include = values[i - 1] + dp[
                    i - 1
                ][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            # If item cannot fit
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":

    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    top_down_result = knapsack_top_down(
        weights, values, capacity
    )

    bottom_up_result = knapsack_bottom_up(
        weights, values, capacity
    )

    print("Weights :", weights)
    print("Values  :", values)
    print("Capacity:", capacity)

    print("\nTop-Down Result   :", top_down_result)
    print("Bottom-Up Result :", bottom_up_result)