def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
#su dung ham va in ket qua
input_string = input("moi nhap vao chuoi can dao nguoc: ")
print("chuoi dao nguoc la",dao_nguoc_chuoi(input_string))