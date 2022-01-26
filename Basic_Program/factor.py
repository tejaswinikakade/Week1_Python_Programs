'''
@Author: Tejaswini Kakade
@Date: 24-01-2022
@Last Modified by: Tejaswini Kakade
@Last Modified time: 24-01-2022 17:15:00
@Title :Computes the prime factorization of N using brute force
'''
num=int(input("Enter Integer Value: "))

i=2
Number=num
while Number >1:
    if Number % i == 0:        
        print(i,end=" \n")    
        Number=int(Number/i)  
    else:
        i=i+1 