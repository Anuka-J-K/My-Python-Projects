import requests
import sys

sys.stdout.reconfigure(encoding='utf-8') # this is for the terminal to display the sinhala characters correctly. Also, it is used to display the emoji's 

print("🌍 Currency Converter is running...\n")

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    lkr_rate = data['rates']['LKR']
    lkr_to_usd = 1 / lkr_rate
    date = data['date']
    
    print("✅ Successfully Connected!")
    print(f"📅 Date: {date}")
    print(f"💵 1 USD = {lkr_rate:.2f} LKR")

    amount = float(input("Enter amount in USD: "))
    converted_amount = amount * lkr_rate
    print(f"{amount} USD = {converted_amount} LKR")
    

except Exception as e:
    print("❌ An error occurred.")
    print(f"Error: {e}")

"""
    sys used to reconfigure the encoding of the terminal.
    if we dont use this, the terminal will not display the sinhala characters correctly.
    and also used to display the emoji's 
    reconfigure() function is used to reconfigure the encoding of the terminal. 
    It takes one argument, encoding, which is the new encoding to use. In this case, we are using 'utf-8' encoding.
    "utf-8" is a variable that is used to store the encoding of the terminal.
    encoding means, the language code that is used to display the characters in the terminal.
    for example, "utf-8" is used to display the sinhala characters correctly.
    and "ascii" is used to display the english characters correctly.

    other functions of "sys" module:
    sys.exit() - used to exit the program.
    sys.stdin - used to get the input from the user.
    sys.stdout - used to display the output to the user.
    sys.stderr - used to display the error messages to the user.
    sys.argv - used to get the command line arguments.
    sys.version - used to get the version of python.
    sys.platform - used to get the platform of python.
    sys.path - used to get the path of the python interpreter.
    sys.modules - used to get the modules of the python interpreter.

    functions of sys.stdout:
    reconfigure() - used to reconfigure the encoding of the terminal.
    write() - used to write the output to the terminal.
    flush() - used to flush the output to the terminal.

    functions of sys.stdin:
    read() - used to read the input from the user.
    readline() - used to read the input from the user.
    readlines() - used to read the input from the user.
    

    
    """
