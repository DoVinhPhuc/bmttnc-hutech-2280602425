#Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#kiểm tra xem số đó có phải chẵn hay không
if so % 2 ==0:
    print(so,"là số chẵn.")
else:
    print(so,"là số lẽ.")