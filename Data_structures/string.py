# 1. Write a program to count the number of upper and lower case letters in a String.

text = "Hello World! Welcome to Python."

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


# 2. Write a program that will check whether a given string is Palindrome or not.

text = "madam"

clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')


# 3. Given a string, return a new string made of n copies of the first 2 chars of the 
# original string where n is the length of the string. The string length will be >=2. 
# If input is "Wipro" then output should be "WiWiWiWiWi". 

text = "Wipro"

first_two = text[:2]
result = first_two * len(text)
print("Output:", result)


# 4. Given a string, if the first or last character is 'x', return the string without 
# those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".

text = "xHix"

if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]

print("Output:", text)


# 5. Given a string and an integer n, return a string made of n repetitions of the last n 
# characters of the string. You may assume that n is between 0 and the length of the string 
# inclusive. 
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.

text = "Wipro"
n = 3

last_n_chars = text[-n:]
result = last_n_chars * n

print("Output:", result)
