# Maria King
# 10/26/25
# P3HW2 - payroll calculator

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid entry. Please enter a numeric value.")

def main():
    name = input("Enter employee name: ").strip()
    hours = get_positive_float("Enter number of hours worked this week: ")
    rate = get_positive_float("Enter employee's pay rate: ")

    OVERTIME_THRESHOLD = 40.0
    OVERTIME_MULTIPLIER = 1.5

    overtime_hours = max(0.0, hours - OVERTIME_THRESHOLD)
    regular_hours = min(hours, OVERTIME_THRESHOLD)

    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * rate * OVERTIME_MULTIPLIER
    gross_pay = regular_pay + overtime_pay

    # alignment variables so summary values line up in the same column
    label_width = 28
    value_width = 14
    line_fmt = f"{{:<{label_width}}}{{:>{value_width}}}"

    # print employee name above the payroll summary
    print(f"\nEmployee: {name}\n")

    print("Payroll Summary")
    print("-" * (label_width + value_width))
    print(line_fmt.format("Pay rate:", f"${rate:,.2f}"))
    print(line_fmt.format("Hours worked:", f"{hours:,.2f}"))
    print(line_fmt.format("Overtime hours:", f"{overtime_hours:,.2f}"))
    print(line_fmt.format("Pay for regular hours:", f"${regular_pay:,.2f}"))
    print(line_fmt.format("Overtime pay:", f"${overtime_pay:,.2f}"))
    print(line_fmt.format("Gross pay:", f"${gross_pay:,.2f}"))

if __name__ == "__main__":
    main()