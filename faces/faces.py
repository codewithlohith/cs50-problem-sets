def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(","🙁")
    print(text)

def main():
    inp = input("Enter text: ")
    convert(inp)

main()
