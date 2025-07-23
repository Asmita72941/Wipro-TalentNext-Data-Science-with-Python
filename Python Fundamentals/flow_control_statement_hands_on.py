# 1. Write a program to check if a given number is Positive, Negative, or Zero.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is positive.")
elif num%2 != 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")


# 2. Write a program to check if a given number is odd or even.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# 3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

val1 = num1%10
val2 = num2%10

if val1 == val2:
    print("true")
else:
    print("false")


# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1,10):
    print(i, end="\t")


# 5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

for i in range(23,57):
    if i%2 == 0:
        print(i)


# 6. Write a program to check if a given number is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# 7. Write a program to print prime numbers between 10 and 99.

for num in range(10, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')


# 8. Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

num = int(input("Enter a number: "))

sum_of_digits = 0
while num > 0:
    digit = num % 10         
    sum_of_digits += digit   
    num = num // 10          

print("Sum of digits:", sum_of_digits)


# 9. Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# O/P:4321

# Example:2
# I/P:1004
# O/P:4001

num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10              
    reversed_num = reversed_num * 10 + digit
    num = num // 10               

print("Reversed number:", reversed_num)


# 10. Write a program to find if the given number is palindrome or not

# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

