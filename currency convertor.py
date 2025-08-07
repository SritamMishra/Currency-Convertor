usd_to_inr = 83.2
usd_to_eur = 0.91
usd_to_jpy = 151.1

def show_menu():
    print("=" * 40)
    print("💱  SIMPLE CURRENCY CONVERTER")
    print("=" * 40)
    print("Supported conversions:")
    print("1. USD to INR")
    print("2. USD to EUR")
    print("3. USD to JPY")
    print("4. INR to USD")
    print("5. EUR to USD")
    print("6. JPY to USD")
    print("7. Exit")
    print("=" * 40)

def convert(choice, amount):
    if choice == 1:
        return amount * usd_to_inr, "INR"
    elif choice == 2:
        return amount * usd_to_eur, "EUR"
    elif choice == 3:
        return amount * usd_to_jpy, "JPY"
    elif choice == 4:
        return amount / usd_to_inr, "USD"
    elif choice == 5:
        return amount / usd_to_eur, "USD"
    elif choice == 6:
        return amount / usd_to_jpy, "USD"
    else:
        return None

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-7): "))
            if choice == 7:
                print("👋 Thank you for using the converter!")
                break
            if choice < 1 or choice > 7:
                print("❌ Invalid choice. Try again.\n")
                continue

            amount = float(input("Enter amount to convert: "))
            result, currency = convert(choice, amount)

            if result is not None:
                print("✅ Converted amount: {result: } {currency}\n")
            else:
                print("❌ Conversion failed.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")










