# code for finding letters in messages and finding the length
# author: Harriet Fiagbor 5/1/21 10:20pm

message = input("Hey give me a message: ")

any(k in message for k in 'aeiou')
print("I found a vowel")

length = len(message)

print(" The message whole length is", length)