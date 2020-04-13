def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    dollarAmount = 0
    dollarAmount = (coins["pennies"] / 100) + (coins["nickels"] / 20) + (coins["dimes"] / 10) + (coins["quarters"] / 4)

    print(f"${dollarAmount}")

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
