from datetime import date
import sys
import inflect


def main():
    dob = input("Date of Birth: ")

    try:
        birth_date = get_date_of_birth(dob)
    except ValueError:
        sys.exit("Invalid Value")

    minutes = (date.today() - birth_date).days * 24 * 60

    p = inflect.engine()

    print(f"{p.number_to_words(minutes, andword = ' ').capitalize()} minutes")

def get_date_of_birth(dob):

    try:
        year,month,day = dob.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
