def budget():
    # Initialize the budget
    total_budget = float(input("Enter your total budget for the month: "))
    remaining_budget = total_budget
    expenses = {}

    while True:
        # Input daily expenses
        category = input("Enter the category of the expense (or 'no' to quit): ")
        if category.lower() == 'no':
            break
        amount = float(input(f"Enter the amount spent on {category}: "))

        # Update expenses
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        # Update remaining budget
        remaining_budget -= amount

        # Display totals
        print(f"Total spent so far: Rupees {total_budget - remaining_budget:.2f}")
        print(f"Remaining budget: Rupees {remaining_budget:.2f}")

        # Warning if budget exceeded
        if remaining_budget < 0:
            print("Warning: You have exceeded your budget!")

    # Display breakdown of expenses by category
    print("\nExpense Breakdown by Category:")
    for category, amount in expenses.items():
        print(f"{category}: Rupees {amount:.2f}")

if __name__ == "__main__":
    budget()