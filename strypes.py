import sys


def addToCheck(y, x, val, data, toCheck1):
    '''
    input   Coordinates (y,x) 
            Seek value (val)
            The matrix (data)
            List with previous fields to-check (toCheck1)
    output  Returns a list [previous fields to-check + new, if any] (toCheck)
    '''
    toCheck = toCheck1
    if x > 0 and data[y][x-1][0] == val and not data[y][x-1][1]:
        toCheck.append(data[y][x-1])
    if x < len(data[0]) - 1 and data[y][x+1][0] == val and not data[y][x+1][1]:
        toCheck.append(data[y][x+1])
    if y > 0 and data[y-1][x][0] == val and not data[y-1][x][1]:
        toCheck.append(data[y-1][x])
    if y < len(data) - 1 and data[y+1][x][0] == val and not data[y+1][x-1][1]:
        toCheck.append(data[y+1][x])
    return toCheck


def run(val, max, data):
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x][1]:
                break

            count = 0
            if (data[y][x][0] == val):
                toCheck = []
                count = 1
                data[y][x][1] = True
                toCheck = addToCheck(y, x, val, data, toCheck)
                while(len(toCheck)):
                    checkCell = toCheck.pop(0)
                    if not data[checkCell[2]][checkCell[3]][1] and\
                            data[checkCell[2]][checkCell[3]][0] == val:
                        count += 1
                        data[checkCell[2]][checkCell[3]][1] = True
                        toCheck = addToCheck(checkCell[2], checkCell[3],
                                             val, data, toCheck)
            if(max < count):
                max = count
    return max


def matrix(mtrx, rows, cols):
    '''
    input   The matrix (mtrx)
            Size of the matrix (rows, cols)
    output  Returns t
    '''
    matrix = [[[mtrx[i+j]] for i in range(rows)]
              for j in range(0, cols*cols, cols)]
    for y in range(rows):
        for x in range(cols):
            matrix[y][x].append(False)
            matrix[y][x].append(y)
            matrix[y][x].append(x)
    return matrix


if __name__ == "__main__":

    for k in range(1, len(sys.argv)):
        with open(sys.argv[k], "rt") as f:
            mtrx = f.read().split()
            f.close()
            rows = int(mtrx[0])
            cols = int(mtrx[1])
            mtrx.pop(0)
            mtrx.pop(0)

            max = 0
            max = run('R', max, matrix(mtrx, rows, cols))
            max = run('B', max, matrix(mtrx, rows, cols))
            max = run('G', max, matrix(mtrx, rows, cols))

            print(max)
