'''
@Author: Tejaswini Kakade
@Date: 24-01-2022
@Last Modified by: Tejaswini Kakade
@Last Modified time: 24-01-2022 16:00:00
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''


print ("Program For Replacing String User input with Template")

name = input("\nEnter Your Name: ")

if len(name)>=3:
    print ("\nHello",name ,end='\n' "How are you?")
else:
    print("Enter minimum Three as Input  ")
