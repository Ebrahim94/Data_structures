#goal is to write a function to check if two strings are anagrams of one another
#the function should take in two inputs of type String and output a Boolean

def anagram(string1, string2):

    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    if sorted(string1) == sorted(string2):
        return 'This is an anagram'
    else:
        return 'This is not an anagram'
    



print(anagram('raat', 'taar'))