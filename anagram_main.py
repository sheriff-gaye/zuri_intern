


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if sorted (word)== sorted(anagram):
        print("True")
    
    else:
        print("False")

#calling function with samples
find_anagram('heart','earth')
find_anagram("left",'felt')
find_anagram("hello","ello")

