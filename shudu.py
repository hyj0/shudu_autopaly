# -*- coding: utf-8 -*-
# @time  : 2021/7/31  20:53
# @Author: nizi
# @Nizi  : $(NAME).py



shuduList = [
    [0, 2, 3], #第一行
    [2, 0, 1],
    [3, 1, 2],
]

# 如输入数独的 利用BeautifulSoup来解析网页
def LoadInput():
    pass
    # shuduList[0][1] = 8
    # shuduList[0][3] = 4

# 获取可填写列表
def GetPoss(x, y):
    pass

# 计算
def Resolve():
    pass

    # 扫描所有的0 记录位置（x， y）-->可填写列表[]
    for i in range(len(shuduList)):
        print(shuduList[i])
        hang = shuduList[i]
        for j in range(len(shuduList)):
            print(hang[j])
            num = hang[j]
            if num == 0:
                pList = GetPoss(i,j)

#     可填写列表[]：初始化为123456789， 然后按九宫格去除不能填写的， 按一行去除不能填写， 按一列去除不能填写的
#  得到 [(x, y, [n,n,...]), (x, y, [n,n,...])]
#     举例 [(0,0, [3,6]), (0,2,[3,6])]
# 循环组合 组合函数 3,3  3，6  6,3 6,6
#


if __name__ == '__main__':
    LoadInput()
    Resolve()

