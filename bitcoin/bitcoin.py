#c4e0fbd9c91d148f8308bb2d988cd67b7d2fd3160bb7ff6b1939773c8e77a3ba

import sys
import requests

if (len(sys.argv) == 1):
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c4e0fbd9c91d148f8308bb2d988cd67b7d2fd3160bb7ff6b1939773c8e77a3ba")
except requests.RequestException:
    sys.exit()

o = response.json()


value = float(o["data"]["priceUsd"])

amount = value * num

print(f"${amount:,.4f}")
