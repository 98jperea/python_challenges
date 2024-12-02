def currency_converter(amount, rate):
    return amount * rate

if __name__ == "__main__":
    print("Currency Converter")
    amount = float(input("Enter amount in EUR: "))
    rate = float(input("Enter conversion rate to USD: "))
    print(f"{amount} EUR is {currency_converter(amount, rate):.2f} USD.")