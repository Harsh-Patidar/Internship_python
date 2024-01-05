import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    params = {'apikey': api_key}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        return data['rates'].get(target_currency)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount in the base currency: "))
            base_currency = input("Enter the base currency code (e.g., USD): ").upper()
            target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

            exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

            if exchange_rate is not None:
                converted_amount = convert_currency(amount, exchange_rate)
                print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
                print(f"Exchange Rate: 1 {base_currency} = {exchange_rate:.4f} {target_currency}")
            else:
                print("Invalid currency codes. Please check and try again.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

        again = input("Do you want to convert another currency? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
