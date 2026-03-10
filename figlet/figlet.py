import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))

else:
    if (sys.argv[1] not in ['-f','--font']):
        sys.exit("Invalid Usage")

    if (sys.argv[2] not in figlet.getFonts()):
        sys.exit("Invalid Usage")

    figlet.setFont(font = sys.argv[2])

inp = input("Input: ")

print("Output: ", figlet.renderText(inp))
