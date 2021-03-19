# **Pig Latin** - Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed 
# to the end of the word and an ay is affixed

def pig():

    end_word = "ay"
    word = input("Enter a word: ")

    if len(word)>0 and word.isalpha():
        word = word.lower()
        first = word[0]
        rest = word[1:]
        return f"{rest}-{first}{end_word}"
    else:
        return "wrong input"

if __name__=="__main__":
    print(pig())
