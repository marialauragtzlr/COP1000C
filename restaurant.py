"""
Maria Laura Gutierrez
06/08/25

Program Summary:
    This program prompts the user for the cost of a meal (food and drinks),
    and displays a bill with tax, tip, and the total amount to pay.

IPO Chart:
    Input:
        The user will input the cost of food and the cost of drinks.

    Process:
        The cost of the meal, 7.5% tax, 18% tip, and the total amount
        to pay will be calculated.

    Output:
        The cost of the meal, 7.5% tax, 18% tip, and the total amount
        to pay will be formatted and displayed.
"""
def validateFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nInvalid input. Please enter an amount.\n")

def main():

    print('Restaurant Bill Generator ...\n')
    cost_food = validateFloat(f"{'Please enter cost of food:':31}")
    cost_drinks = validateFloat(f"{'"':^6}{'"':^6}{' cost of drinks:':19}")

    cost_meal = cost_food + cost_drinks
    tax_amount = cost_meal * 0.075
    tip_amount = (cost_meal + tax_amount) * 0.18

    total = cost_meal + tax_amount + tip_amount

    print("\nRestaurant Bill")
    print("-" * 34)
    print("")

    print(f"{'Cost of Meal:':16} $ {cost_meal:>12.2f}")
    print(f"{'Tax Amount:':16} $ {tax_amount:>12.2f}")
    print(f"{'Tip Amount:':16} $ {tip_amount:>12.2f}")

    print(f"{'-' * 17:>34}")
    print(f"{'Total:':16} $ {total:12.2f}")

if __name__ == "__main__":
    main()