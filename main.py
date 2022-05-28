# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(s1, s2):

    if sorted(s1) == sorted(s2):
        print('True')
    else:
        print('False')


s1 = "hello"
s2 = "check"


find_anagram(s1, s2)

s1 = 'elbow'
s2 = 'below'
find_anagram(s1, s2)



