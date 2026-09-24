list1 = [1, 2, 3]
list2 = [4, 5, 6]

new_list = []
new_list.extend(list1)
new_list.extend(list2)
print("Combined List:", new_list)

matrix_A = [list1, list2]
print("\nMatrix A:", matrix_A)

matrix_B = [[6, 5, 4],
            [3, 2, 1]]

result_matrix = [[matrix_A[i][j] + matrix_B[i][j] for j in range(len(matrix_A[0]))]
                 for i in range(len(matrix_A))]

print("\nResult of Matrix Addition (A + B):")
for row in result_matrix:
    print(row)
