import os
import numpy as np
import matplotlib.pyplot as plt
# os.system("python  backtrack.py")      #python 命令 运行A文件


def paint1():
    print("       -----------------散点图----------------")
    print("       |                                    |")
    print("       |   可输入数字0-9选择文件               |")
    print("       |                                   |")
    print("       |   10.退出系统                       |")
    print("       |                                    |")
    print("       --------------------------------------")
    num = 0
    while num != 10:
        num = int(input("选择文件:"))
        match num:
            case 0: zhi("data/beibao0.in")
            case 1: zhi("data/beibao1.in")
            case 2: zhi("data/beibao2.in")
            case 3: zhi("data/beibao3.in")
            case 4: zhi("data/beibao4.in")
            case 5: zhi("data/beibao5.in")
            case 6: zhi("data/beibao6.in")
            case 7: zhi("data/beibao7.in")
            case 8: zhi("data/beibao8.in")
            case 9: zhi("data/beibao9.in")
            case 10: print("退出绘图界面!")

def zhi(str):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('重量')
    plt.ylabel('价值')
    plt.xlim(xmax=200, xmin=0)
    plt.ylim(ymax=150, ymin=0)
    daten = open(str, "r")
    lines = daten.readlines()
    list = []
    for i in lines:
        list.append(i.strip().split(' '))
    daten.close()
    # print(list)
    f = []
    w = []
    v = []
    x = []
    y = []
    for i in list:
        for b in i:
            f.append(b)
    # print(f)
    for i in range(len(f)):
        if i == 0:
            c = int(f[i])
        elif i == 1:
            n = int(f[i])
        elif i > 1 and i % 2 == 0:
            w.append(int(f[i]))
        elif i > 1 and i % 2 == 1:
            v.append(int(f[i]))
    vw(c,n,w,v,x,y)
    colors = 'red'  #  点的颜色
    area = np.pi * 2**2 # 点面积
    # for i in range(len(w)):
    plt.scatter(w, v, s=area, c=colors, alpha=0.1, label=' ')
    plt.legend()
    plt.yticks(())
    plt.title('散点图')
    str = str[5:]
    plt.savefig('./src/scatter_'+ str + '.png')  # 保存图片
    plt.show()


def vw(c,n,w,v,x,y):
    for i in range(n):
        x.append(v[i]/w[i])
        y.append(i+1)
    print("背包容量：", c, "物品个数：", n)
    for i in range(len(w)):
        print("重量:", w[i], "  价值:", v[i], "  性价比", x[i])
    sort(x, y)
    print("按单位价值排序得：", y)


def paint2():
    print("       -----------------柱状图----------------")
    print("       |                                    |")
    print("       |   可输入数字0-9选择文件               |")
    print("       |                                   |")
    print("       |   10.退出系统                       |")
    print("       |                                    |")
    print("       --------------------------------------")
    num = 0
    while num != 10:
        num = int(input("选择文件:"))
        match num:
            case 0: zhi1("data/beibao0.in")
            case 1: zhi1("data/beibao1.in")
            case 2: zhi1("data/beibao2.in")
            case 3: zhi1("data/beibao3.in")
            case 4: zhi1("data/beibao4.in")
            case 5: zhi1("data/beibao5.in")
            case 6: zhi1("data/beibao6.in")
            case 7: zhi1("data/beibao7.in")
            case 8: zhi1("data/beibao8.in")
            case 9: zhi1("data/beibao9.in")
            case 10: print("退出绘图界面!")


def zhi1(str):
    fig, ax = plt.subplots()
    daten = open(str, "r")
    lines = daten.readlines()
    list = []
    for i in lines:
        list.append(i.strip().split(' '))
    daten.close()
    # print(list)
    f = []
    w = []
    v = []
    x = []
    y = []
    for i in list:
        for b in i:
            f.append(b)
    # print(f)
    for i in range(len(f)):
        if i == 0:
            c = int(f[i])
        elif i == 1:
            n = int(f[i])
        elif i > 1 and i % 2 == 0:
            w.append(int(f[i]))
        elif i > 1 and i % 2 == 1:
            v.append(int(f[i]))
    vw(c, n, w, v, x, y)
    y_pos = np.arange(len(w))+1
    ax.barh(y_pos, y, color='b', align="center")
    str = str[5:]
    plt.savefig('./src/barch_' + str + '.png')  # 保存图片
    plt.show()

def sort(x,y):
    for i in range(len(x)):
        for m in range(i):
            if x[i] > x[m]:
                t = x[i]
                x[i] = x[m]
                x[m] = t
                t = y[i]
                y[i] = y[m]
                y[m] = t

s = 0
while s != 6:
    print("       ***************背包问题****************")
    print("       *                                   *")
    print("       *   1.动态规划法        2.贪心法       *")
    print("       *                                   *")
    print("       *   3.回溯法           4.绘制散点图    *")
    print("       *                                   *")
    print("       *   5.绘制柱状图        6.退出系统      *")
    print("       *************************************")
    s = int(input("选择算法:"))
    match s:
        case 1: os.system("python  DP.py")
        case 2: os.system("python  Greedy.py")
        case 3: os.system("python  backtrack.py")
        case 4: paint1()
        case 5: paint2()
        case 6: print("感谢使用，再见!")
