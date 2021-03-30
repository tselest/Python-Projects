# Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found. 
from collections import Counter

sentence = input("Enter a string: ").lower().replace(" ","")
while sentence.isalpha():
    vowels = 'aeiou'

    count = [i for i in sentence if i in vowels]
    per = Counter(count)
    print(f"Total vowel count: {count}\nDict vowel {per}")
    break

