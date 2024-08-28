matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpos_mtrix = []


for i in range (len(matrix)) :
    matrix_row = []
    for row in matrix:
        matrix_row.append(row[i])
    transpos_mtrix.append(matrix_row)
for row in matrix:
    print(row)

print(" ")
for row in transpos_mtrix:
    print(row)
    