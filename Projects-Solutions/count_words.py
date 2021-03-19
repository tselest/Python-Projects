# Count Words in a String - Counts the number of individual words in a string.


def count():
    string = input("Please enter a string: ")

    if string.replace(" ","").isnumeric()==True:
        return "NOT A STRING"
    elif all(isinstance(item, str) for item in string):
        return f"Given string has {len(string.split())} words"
    else:
        return "error"

if __name__ == "__main__":
    print(count())
