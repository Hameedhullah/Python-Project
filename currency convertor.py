def convert_to_inr(dollar):
    conversion_rate = 83.06
    inr = dollar * conversion_rate
    return inr

def main():
    print("This program converts US Dollar to Indian Rupee")
    print()

    try:
        dollar = float(input("Enter the amount in US Dollars: "))
        inr = convert_to_inr(dollar)
        print('That is', inr, 'Rupee')
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
