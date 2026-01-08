import os

# Jenkins parameters are stored in os.environ
user_input = os.getenv("MY_NUMBER")

if user_input:
    try:
        num = int(user_input)
        print(f"Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number.")
else:
    print("No input provided by Jenkins parameter!")