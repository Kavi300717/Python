USD_TO_EUR = 0.93
USD_TO_GBP = 0.77
USD_TO_JPY = 150.11
USD_TO_INR = 85.66

def convert_currency(amount, target_currency):
    if target_currency == '1':
        converted_amount = amount * USD_TO_GBP
        print(f"Converted amount in EUR : {converted_amount:.2f}")
    elif target_currency == '2':
        converted_amount = amount * USD_TO_GBP
        print(f"Converted amount in GBP: {converted_amount:.2}")
    elif target_currency == '3':
        converted_amount = amount * USD_TO_JPY
        print(f"Converted amount in JPY: {converted_amount:.2f}")
    elif target_currency == '4':
        converted_amount = amount * USD_TO_INR
        print(f"Converted amount in INR: {converted_amount:.2f}")
    else:
        print("Invalid currency selection. Please choose 1, 2, 3,or 4.")

amount_in_usd = float(input("Enter the amount in USD: "))

print("Select target currency (1 for EUR, 2 for GBP, 3 for JPY, 4 for NR): ")
target_currency = input("Enter the number corresponding to the target currency.")

convert_currency(amount_in_usd, target_currency)
