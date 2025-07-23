import urllib.request
import urllib.parse
import json

def convert_currency(amount,from_currency,to_currency):
    base_url = "https://api.exchangerate.host/convert"
    query = f"?from={from_currency}&to={to_currency}&amount={amount}"
    url = base_url+query

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            result = json.loads(data)
            if result.get("success",False):
                converted_amount = result["result"]
                print(f"\nConvertednamount:{converted_amount:.2f}{to_currency}")
            else:
                print("Conversion failed. Please check your currency codes.")
    except Exception as e:
        print(f"Error fetching exchange rate:{e}")

def main():
    print("WECOME TO CURRENCY CONVERTER USING API(no external modules)")
    try:
        amount = float(input("Enter amount:"))
        from_currency = input("Convert from(e.g., USD):").strip().upper()
        to_currency = input("Convert to(e.g.,INR):").strip().upper()
        convert_currency(amount,from_currency,to_currency)
    except ValueError:
         print("Invalid amount.please enter a number.")
if __name__ == "__main__":
    main()
    
