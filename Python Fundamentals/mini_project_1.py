'''
Tech Module: Python Fundamentals
Project: 1

Create a python program that asks the user how far they want to travel. 
If they want to travel less than three miles tell them to ride Bicycle. If 
they want to travel more than three miles, but less than three hundred miles, 
tell them to ride Motor-Cycle. If they want to travel three hundred miles or 
more tell them to driver Super-Car.
Sample :
How far would you like to travel in miles? 2500
Output : I suggest Super-Car to your destination
'''

miles = int(input("How far would you like to travel in miles?"))

if miles < 3:
    print("I suggest Bicycle to your destination.")
elif 3 <= miles < 300:
    print("I suggest Motor-Cycle to your destination.")
elif miles >= 300:
    print("I suggest Super-Car to your destination")


'''
project: 2
Let's assume you are planning to use your Python skills to build a PBLApp for 
Mobile.You decide to host your application on servers running in the cloud. You 
pick a hosting provider that charges $0.51 per hour. You will launch your service
using one server and want to know how much it will cost to operate per day, per week, per month.

Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?
'''

cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_week * 4
days_with_budget = 918 / cost_per_day

print(f"Cost to operate one server per day: {cost_per_day}")
print(f"Cost to operate one server per week: {cost_per_week}")
print(f"Cost to operate one server per month: {cost_per_month}")
print(f"Days I can operate one server with $918: {days_with_budget} days")

