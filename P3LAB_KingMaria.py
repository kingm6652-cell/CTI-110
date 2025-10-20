# Maria King
# 10/19/25
# P3LAB
# Description: This program calculates the change for a given amount in dollars.

def make_change(amount_dollars: float):
    """Return (dollars, quarters, dimes, nickels, pennies) for amount_dollars."""
    if amount_dollars < 0:
        raise ValueError("Amount must be non-negative.")
   
    cents = int(round(amount_dollars * 100))


    dollars = cents // 100
    cents -= dollars * 100

    quarters = cents // 25
    cents -= quarters * 25

    dimes = cents // 10
    cents -= dimes * 10

    nickels = cents // 5
    cents -= nickels * 5

    pennies = cents

    return dollars, quarters, dimes, nickels, pennies


def _coin_name(singular: str, plural: str, count: int) -> str:
    return singular if count == 1 else plural

def main():
    s = input("Enter amount in dollars (e.g. 1.37): ").strip()
    try:
        amt = float(s)
    except ValueError:
        print("Invalid input. Please enter a numeric amount like 1.37")
        return

    if amt < 0:
        print("Amount must be non-negative.")
        return

    dollars, quarters, dimes, nickels, pennies = make_change(amt)

    print(f"Amount: ${amt:.2f}")

    if dollars:
        print(f"{dollars} {_coin_name('dollar','dollars',dollars)}")
    if quarters:
        print(f"{quarters} {_coin_name('quarter','quarters',quarters)}")
    if dimes:
        print(f"{dimes} {_coin_name('dime','dimes',dimes)}")
    if nickels:
        print(f"{nickels} {_coin_name('nickel','nickels',nickels)}")
    if pennies:
        # singular 'penny', plural 'pennies'
        print(f"{pennies} {_coin_name('penny','pennies',pennies)}")




