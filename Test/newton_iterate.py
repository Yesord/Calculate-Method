import math


def df(x,f):
    return (f(x)-f(x-1e-6))/1e-6

def newton_iterate(x, f, acc, max_iter):
    # x: 初始值
    # f: 函数
    # acc: 精度
    # max_iter: 最大迭代次数
    # 返回值: 迭代结果
    # 请在此处添加代码:
    for iter in range(max_iter):
        x = x - f(x)/df(x,f)
        if abs(x) < acc:
            break
    return x



def f(x):
    
    return math.pow(x,3) - 2*math.pow(x,2) + 3*x - 4


if __name__ == "__main__":
    ret = newton_iterate(2, f, 1e-6, 100)
    print(ret)