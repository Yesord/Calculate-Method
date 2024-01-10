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
        x1 = x - f(x)/df(x,f)
        print(x1)
        if abs(x1-x) < acc:
            return x1, iter
        x = x1



def f(x):
    
    return x**3+4*x**2-10


if __name__ == "__main__":
    ret = newton_iterate(1, f, 1e-5, 100)
    print(ret[0], ret[1])