#print("Welcome to Gabriel's Function Cardio")

#num1 = int(raw_input("Give me side 1 length: "))
#num2 = int(raw_input("Give me side 2 length: "))
#num3 = int(raw_input("Give me side 3 length: "))

#def is_triangle(s1,s2,s3):
#    sum1 = s1 + s2 #test if greater than s3
#    sum2 = s2 + s3 #test if greater than s1
#    sum3 = s3 + s1 #test if greater than s2
#    if sum1 > s3 and sum2 > s1 and sum3 > s2:
#        print("You have a triangle")
#        return True #i have a triangle
#    else:
#        print("No triangle for you")
#        return False #not a triangle

#is_triangle(num1,num2,num3)

#LONGEST WORD
#print("Welcome to Gabriel's Longest Word")

#word1 = raw_input("Please give me a word: ")
#word2 = raw_input("Please give me another word: ")
#word3 = raw_input("One more word please: ")

#def longest_word(length1, length2, length3):
#    if len(length1) > len(length3) and len(length2):
#        longest = length1
#        print(length1 + "is the longest word")
#    elif len(length2) > len(length1) and len(length3):
#        longest = length2
#        print(length2 + "is the longest word")
#    elif len(length3) > len(length1) and len(length2):
#        longest = length3
#        print(length3 + "is the longest word")
#longest_word(word1,word2,word3)

#REVERSE STRING
print("Welcome to Gabriel's Reverse Strings")

word = raw_input("Please give me a word: ")
def reverse_string(x):
    return x [::-1]


print("this is your word backwards: " + reverse_string(word))
