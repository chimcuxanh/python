import time
a = 1
b = 2
c = 3

answer =  input("What you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    time.sleep(a)
    answer = input("You reach a crossroands, would you like to left or right?")

    if answer == "left":
        time.sleep(b)
        answer = input("gap quai vat muon chay hay danh")
        if answer == "danh":
            time.sleep(c)
            print("con cho ngu , thua roi")
        else:
            time.sleep(c)
            print("hay lam , chay di")
    elif answer == "right":
        time.sleep(b)
        print("do la 1 cau chuyen dai , lam deo muon ke nua dau ")
    else:
        print(" m nhap sai con me m r, nhap lai di ")

elif answer == "no":
    print("that to bad")

else:
    print("nhap sai roi con cho ak nhap lai di  ")