# -*- coding: utf-8 -*-
# @time  : 2021/7/31  20:53
# @Author: nizi
# @Nizi  : $(NAME).py

import copy
import time

shuduList = [
[0, 0, 0, 0, 0, 0, 1, 0, 0] ,
[3, 0, 0, 2, 0, 0, 0, 0, 0] ,
[0, 1, 0, 0, 9, 3, 0, 6, 5] ,
[0, 0, 6, 0, 0, 0, 5, 1, 2] ,
[4, 0, 0, 0, 0, 0, 0, 0, 9] ,
[7, 2, 5, 0, 0, 0, 8, 0, 0] ,
[2, 4, 0, 7, 3, 0, 0, 8, 0] ,
[0, 0, 0, 0, 0, 2, 0, 0, 4] ,
[0, 0, 8, 0, 0, 0, 0, 0, 0] ,
]

# 如输入数独的 利用BeautifulSoup来解析网页
def LoadInput():
    pass
    # shuduList[0][1] = 8
    # shuduList[0][3] = 4

# 获取可填写列表
def GetPoss(x, y):
    retList =  []
    for i in range(len(shuduList)):
        retList.append(i+1)
    # todo:处理九宫格
    edA = int(x/3) * 3
    edB = int(y/3) * 3
    # print("xx", x, y, edA, edB)
    for i in range(edA, edA+3):
        for j in range(edB, edB+3):
            # print("aaa", i, j)
            if shuduList[i][j] != 0:
                if shuduList[i][j] in retList:
                    retList.remove(shuduList[i][j])

    #处理行
    pHang = shuduList[x]
    for i in range(len(pHang)):
        if pHang[i] != 0:
            if pHang[i] in retList:
                retList.remove(pHang[i])

    #处理列
    for i in range(len(shuduList)):
        if shuduList[i][y] != 0:
            if shuduList[i][y] in retList:
                retList.remove(shuduList[i][y])
    return retList


# 排列组合 例如输入calcList[(x, y, [n,n,...]), (x, y, [n,n,...])]，返回组合
def CalcComb(calcList, index, retList, rIndex, collectList):
    if index >= len(calcList):
        cpList = copy.deepcopy(retList)
        # print(cpList)
        collectList.append(cpList)
        return

    x, y, possiList = calcList[index]
    for num in possiList:
        if False:
            retList.append([(x, y, num)])
            CalcComb(calcList,index+1, retList, rIndex, collectList)
            rIndex += 1
        else:
            shuduList[x][y] = num
            ret = JudgeShudu()
            if not ret:
                shuduList[x][y] = 0
                continue
            retList.append((x, y, num))
            CalcComb(calcList, index+1, retList, rIndex, collectList)
            shuduList[x][y] = 0
            retList.pop()

#判断数独是否已正确
def JudgeShudu():
    # todo:处理九宫格
    for edA in range(0,9,3):
        for edB in range(0,9,3):
            numList = []
            for i in range(edA, edA+3):
                for j in range(edB, edB+3):
                    num = shuduList[i][j]
                    if num == 0:
                        # 不判断0
                        continue
                    if num in numList:
                        # 如果已经有了，说明重复了
                        return False
                    else:
                        numList.append(num)
    #处理行
    for i in range(len(shuduList)):
        numList = []
        for j in range(len(shuduList)):
            num = shuduList[i][j]
            if num == 0:
                continue
            if num in numList:
                # 如果已经有了，说明重复了
                return False
            else:
                numList.append(num)
    #处理列
    for i in range(len(shuduList)):
        numList = []
        for j in range(len(shuduList)):
            num = shuduList[j][i]
            if num == 0:
                continue
            if num in numList:
                # 如果已经有了，说明重复了
                return False
            else:
                numList.append(num)

    return True

# 计算
def Resolve():
    pass
    calcList = [] # 计算列表[(x, y, [n,n,...]), (x, y, [n,n,...])]
    # 扫描所有的0 记录位置（x， y）-->可填写列表[]
    for i in range(len(shuduList)):
        print(shuduList[i])
        hang = shuduList[i]
        for j in range(len(shuduList)):
            # print(hang[j])
            num = hang[j]
            if num == 0:
                pList = GetPoss(i,j)
                calcList.append((i, j, pList))

#     可填写列表[]：初始化为123456789， 然后按九宫格去除不能填写的， 按一行去除不能填写， 按一列去除不能填写的
#  得到 calcList[(x, y, [n,n,...]), (x, y, [n,n,...])]
#     举例 [(0,0, [3,6]), (0,2,[3,6])]
    print('calcList', calcList)
    loopCount = 1
    for i in calcList:
        loopCount *= len(i[2])
    print("loopCount", loopCount)
# 循环组合 组合函数 3,3  3，6  6,3 6,6
#
    stepList = []
    collectList = []
    CalcComb(calcList, 0, stepList, 0, collectList)
    for i in collectList:
        print('stepList', i)

#   循环执行collectList，即放到shuduList中尝试
    for sList in collectList:
        for x, y, num in sList:
            shuduList[x][y] = num
        #判断数独是否已正确
        ret = JudgeShudu()
        if ret == True:
            print("OK sList=", sList)
            for l in shuduList:
                print(l)
            return True, sList

    return False, None

if __name__ == '__main__':
    LoadInput()
    start = time.time()
    ret, sList = Resolve()
    if ret:
        print("ok")
    else:
        print("false")

    end = time.time()
    print("time", end-start)
