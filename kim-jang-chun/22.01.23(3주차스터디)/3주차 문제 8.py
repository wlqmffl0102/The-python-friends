ph = input("phone number : ")

if ph[0]+ph[1]+ph[2] == "011":
    print("SKT")
elif ph[0]+ph[1]+ph[2] == "016":
    print("KT")
elif ph[0]+ph[1]+ph[2] == "019":
    print("LG")
elif ph[0]+ph[1]+ph[2] == "010":
    print("none")
else:
    print("error")
    