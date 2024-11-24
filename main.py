def coloring(ls):
    """
    رنگ‌آمیزی سطح خارجی یک مکعب سه بعدی.

    Args:
        ls : یک لیست سه بعدی که مکعب را نمایش می‌دهد.
    """
    x_dim = len(ls)
    y_dim = len(ls[0])
    z_dim = len(ls[0][0])

    for x in range(x_dim):
        for y in range(y_dim):
            for z in range(z_dim):
                if (x == 0 or x == x_dim - 1 or
                        y == 0 or y == y_dim - 1 or
                        z == 0 or z == z_dim - 1):
                    ls[x][y][z] = 1
                else:
                    ls[x][y][z] = 0


matrix = [
    [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]],
    [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]],
    [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]]
]

coloring(matrix)

for i in range(len(matrix)):
    print("{}th layer:".format(i + 1))
    for j in matrix[i]:
        for k in j:
            print(k, end=' ')
        print()
