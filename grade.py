print("Entert 5 subject marks")
tot=0
for i in range (1,6):
    m=int(input("Enter mark:"))
    tot=tot+m
print("Aggregate(total)=",tot)
per=(tot/500)*100
print("Percentage of marks=",per)
if per>=90:
    print("rade:O")
elif per>=80:
    print("Grade:A+")
elif per>=70:
    print("Grade:A")
elif per>=60:
    print("Grade:B+")
elif per>=55:
    print("Grade:B")
elif per>=50:
    print("Grade:C")
else:
    print("invalid")
