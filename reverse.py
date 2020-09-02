def reverse(str):
    rev=''
    i=len(str)-1
    while i>=0:
        rev+=str[i]
        i-=1
    return rev
str=input("Enter the string to reverse")
print("The reversed string is",reverse(str))
