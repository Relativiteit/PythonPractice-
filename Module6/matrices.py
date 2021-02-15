def sum_matrix(m):
    result = 0
    for row in m:
        for value in row:
            result += value
    return result

def contains(m,v):
    for row in m:
        for value in row:
            if value == v: #linear search
                return True
    return False
def mirrored(m):
    number_of_columns = len(m[0])

    for row in m:
        for i in range(0, number_of_columns):
            if row[i] == row[number_of_columns - i - 1]:
                return False



m = [[1,2,3],[4,5,6],[7,8,9]]
print(contains(m,8))
