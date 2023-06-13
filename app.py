from tabulate import tabulate

def calculate_budget(salary, housing_rent, savings, electricity_water):
    # Calculate the allocations based on the percentages
    tithes = salary * 0.1
    love_offering = salary * 0.03
    remaining = salary - tithes - love_offering - savings - housing_rent - electricity_water
    weekly_budget = 1000

    # Calculate the weekly budget from the remaining amount
    weekly_budget = remaining / 4

    # Create the budget breakdown table
    table_data = [
        ["Allocation", "Percentage", "Amount (in pesos)"],
        ["Tithes", "10%", tithes],
        ["Love Offering", "3%", love_offering],
        ["Savings", f"{int((savings / salary) * 100)}%", savings],
        ["Housing Rent", "-", housing_rent],
        ["Electricity and Water", "-", electricity_water],
        ["Remaining", "-", remaining],
        ["Weekly Budget", "-", weekly_budget]
    ]

    # Display the table
    table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
    print(table)

    # Calculate the total amount
    total_amount = sum(row[2] for row in table_data[1:-1])

    # Display the total
    print("Total: ", total_amount)

# Example usage
salary = float(input("Enter your monthly salary: "))
housing_rent = float(input("Enter your house rent: "))
electricity_water = float(input("Enter your electricity and water: "))
savings = salary * (float(input("Enter your savings by percent: ")) / 100)

calculate_budget(salary, housing_rent, savings, electricity_water)
