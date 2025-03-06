input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]  # Chuyển từng phần tử thành số nguyên
rowNum, colNum = dimensions
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# Điền giá trị vào danh sách
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In kết quả
print(multilist)
