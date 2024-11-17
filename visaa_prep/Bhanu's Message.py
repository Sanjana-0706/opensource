s=input()
if (s[0]=='+' and s[1:3].isdigit() and s[3]==" " and len(s)==14 and s[4:].isdigit() and sum(int(digit) for digit in s[4:])>0):
    print("Correct")
else:
    print("Incorrect")
