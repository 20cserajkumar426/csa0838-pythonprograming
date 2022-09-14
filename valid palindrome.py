sr=input("enter the string")
s=''.join(filter(str.isalpha,sr))
s=s.lower()
if(s == s[::-1]):
    print("True")
else:
    print("False")
