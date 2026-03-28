i_amo=int(input("Enter initial balance:"))
mode=input("Enter mode of transaction(deposit/withdrawal):")
t_amo=int(input("Enter transaction amount:"))
if mode=="deposit":
    if t_amo<1000:
        print("Transaction not possible..")
    else:
        up_bal=i_amo+t_amo
        print("The Updated Balance =",up_bal)
else:
    if t_amo<i_amo:
        up_bal=i_amo-t_amo
        if up_bal<1000:
            print("Transaction not possible..")
        else:
            print("The Updated Balance =",up_bal)
    else:
        print("Transaction not possible..")
