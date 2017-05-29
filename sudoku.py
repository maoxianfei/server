# -*- coding:utf-8 -*-
import time

t0 = time.time()
fin1=''

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


def rowNum(p, sudoku):
    row = set(sudoku[p.y * 9:(p.y + 1) * 9])
    row.remove(0)
    return row  # set type


def colNum(p, sudoku):
    col = []
    length = len(sudoku)
    for i in range(p.x, length, 9):
        col.append(sudoku[i])
    col = set(col)
    col.remove(0)
    return col  # set type


def blockNum(p, sudoku):
    block_x = p.x // 3
    block_y = p.y // 3
    block = []
    start = block_y * 3 * 9 + block_x * 3
    for i in range(start, start + 3):
        block.append(sudoku[i])
    for i in range(start + 9, start + 9 + 3):
        block.append(sudoku[i])
    for i in range(start + 9 + 9, start + 9 + 9 + 3):
        block.append(sudoku[i])
    block = set(block)
    block.remove(0)
    return block  # set type


def initPoint(sudoku):
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def tryInsert(p,sudoku):
    availNum = p.available

    for v in availNum:
        p.value = v
        if check(p, sudoku):
            sudoku[p.y * 9 + p.x] = p.value
            if len(pointList) <= 0:
                t1 = time.time()
                useTime = t1 - t0
                a=showSudoku(sudoku)
                # print('\nuse Time: %f s' % (useTime))
                return a
            p2 = pointList.pop()
            tryInsert(p2, sudoku)
            sudoku[p2.y * 9 + p2.x] = 0
            sudoku[p.y * 9 + p.x] = 0
            p2.value = 0
            pointList.append(p2)
        else:
            pass


def check(p, sudoku):
    if p.value == 0:
        print('not assign value to point p!!')
        return False
    if p.value not in rowNum(p, sudoku) and p.value not in colNum(p, sudoku) and p.value not in blockNum(p, sudoku):
        return True
    else:
        return False


def showSudoku(sudoku):
    global fin1
    sum=''
    for j in range(9):
        for i in range(9):
            a= '%d ' %(sudoku[j * 9 + i])
            b=str(a)
            sum=sum+b
        b='\n'
        sum=sum+b
    # print "处理成功"
    fin1 = sum



# if __name__=='__main__':
def main(sudokustr):

    sudoku1 = [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 3, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ]
    sudoku2 = [
        8, 6, 0, 0, 0, 0, 0, 4, 0,
        0, 0, 3, 1, 2, 0, 0, 0, 0,
        4, 0, 0, 0, 0, 3, 0, 7, 0,
        7, 5, 6, 3, 0, 0, 0, 0, 0,
        3, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 9, 3, 5, 8,
        0, 4, 0, 2, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 7, 1, 8, 0, 0,
        0, 2, 0, 0, 0, 0, 0, 9, 5,
    ]
    sudoku3 = [
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ]
    #输入数独数据并将字符转换为列表
    # print sudoku3
    # print sudoku2
    # try:
    #     sudokustr=input('>>>\n')
    # except SyntaxError:
    #     result="语法错误，请使用英文的逗号。如： 英文：, 中文：，"
    #     return result
    global pointList
    sudoku=sudokustr.split(',')
    print sudoku
    sudokustr=map(int,sudoku)
    print sudokustr
    pointList = initPoint(sudokustr)
    # 打印出输入的数独列表
    # try:
    showSudoku(sudokustr)
    # except IndexError:
    #     print ""
    #     result="输入数据有错，不足81位"
    #     return result
    # print('\n')
    #需找数独解法
    # try:
    p = pointList.pop()
    tryInsert(p, sudokustr)
    # except IndexError:
    #     result='无法处理，输入数据不合理'
    #     return result
    # except Exception,e:
    #     result=Exception,e
    #     return result


if __name__=='__main__':
    sudoku3 = [
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1,
    ]
    sudoku2 = [
        8, 6, 0, 0, 0, 0, 0, 4, 0,
        0, 0, 3, 1, 2, 0, 0, 0, 0,
        4, 0, 0, 0, 0, 3, 0, 7, 0,
        7, 5, 6, 3, 0, 0, 0, 0, 0,
        3, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 9, 3, 5, 8,
        0, 4, 0, 2, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 7, 1, 8, 0, 0,
        0, 2, 0, 0, 0, 0, 0, 9, 5,
    ]
    # print sudoku3
    wix='8,6,0,0,0,0,0,4,0,0,0,3,1,2,0,0,0,0,4,0,0,0,0,3,0,7,0,7,5,6,3,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,9,3,5,8,0,4,0,2,0,0,0,0,0,0,0,0,0,7,1,8,0,0,0,2,0,0,0,0,0,9,5'
    result=main(wix)
    print fin1




