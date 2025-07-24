'''
Tech Module: Functions/Modules/Packages
Project: 1
Write a Python functionthat accepts a hyphen-separated sequence of colors as input 
and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint:All the colors will be completely in either lower case or upper case.

Sample input1:green-red-yellow-black-white
Sample output1:black-green-red-white-yellow

Sample input2:PINK-BLUE-TAN-PURPLE
Sample output2:BLUE-PINK-PURPLE-TAN

'''

def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    return '-'.join(color_list)

print(sort_colors("green-red-yellow-black-white"))  
print(sort_colors("PINK-BLUE-TAN-PURPLE"))           



