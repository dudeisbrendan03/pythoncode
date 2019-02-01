#imports
from random import randint

#names
v,b,br,n,m,be,an,oo,s,ss,t,w,c,d = "veda","brandon","bret","nitya","maggie","beau","angelina","oscar","siya","samay","troy","william","conrad","dristi"

print("WELCOME TO DA SHIP GENERATOR\nMADE WITH 100% TRUTH\n")


for y in range(0,5):
    num1,num2=input("Enter a name: "),input("\nEnter another name: ")

    x = randint(0, 100)
    num1.lower();num2.lower()
    num1 = num1.replace(" ","" );num2 = num2.replace(" ","" )

    
    if num1.lower() == v and num2.lower() != b or num1.lower() == m and num2.lower() != w or num1.lower() == s and num2.lower() != be or num1.lower() == d and num2.lower() != c:   x = randint(0, 100)#VedaOthers
    elif num2.lower() == v and num1.lower() != b or num2.lower() == m and num1.lower() != w or num2.lower() == s and num1.lower() != be or num2.lower() == d and num1.lower() != c: x = randint(0, 100)

    if num1.lower() == n and num2.lower() == br or num1.lower() == s and num2.lower() == be or num1.lower() == d and num2.lower() == c or num1.lower() == m and num2.lower() == w or num1.lower() == v and num2.lower() == b:   x = 100#NityaBret
    elif num2.lower() == n and num1.lower() == br or num2.lower() == s and num1.lower() == be or num2.lower() == d and num1.lower() == c or num2.lower() == m and num1.lower() == w or num2.lower() == v and num1.lower() == b: x = 100
            
    if num1.lower() == n and num2.lower() != br:   x = 0 #NityaOthers
    elif num2.lower() == n and num1.lower() != br:  x = 0

    #print ship
    print("{} and {} have a {}% chance of being together.".format(num1,num2,x))
