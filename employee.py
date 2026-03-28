n=int(input("Enter a number:"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
[25bcs139@mepcolinux py1]$cat emp.py
e_sal=int(input("Enter employee salary:"))
n=int(input("Enter no of days of absent:"))
if n<=2:
    print("No deduction")
else:
    ded=e_sal-((n-2)*500)
    print("Final salary after deduction:",ded)
