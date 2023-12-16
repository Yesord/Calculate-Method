import math
import matplotlib.pyplot as plt

##############################################################################################################
# name: Dichotomy_method
# function: 二分法
# parameter: f: 函数
#            a: 区间左端点
#            b: 区间右端点
#            tol: 精度要求
#            maxiter: 最大迭代次数
#            info: 是否输出迭代信息
#            plot: 是否输出迭代曲线
# return: x1: 迭代结果，如果无法判断是否有根则返回None
#         epoch: 迭代次数，如果无法判断是否有根则返回None
# date: 2023/11/21
# author: Yesord
# note 需要确定区间内有且仅有一个根
##############################################################################################################

def Dichotomy_method(f, a, b, tol, maxiter, info=False, plot=False): 
    x0 = a
    x1 = b
    if f(a) * f(b) > 0:
        print("Error: f({}) * f({}) > 0, we can't ensure that there is root in the interval [{}, {}]".format(a, b, a, b))
        # %操作符用于格式化字符串
        return None, None
    if plot:
        x_history = []
        epoch_history = []
    for epoch in range(maxiter):
        x1 = (a + b) / 2
        if f(x1) * f(a) < 0:
            b = x1
        else:
            a = x1
        if info:
            print("epoch = %d, x1 = %f" % (epoch, x1))
        if plot:# 绘制迭代过程
            plt.ion()
            plt.xlabel("epoch")
            plt.ylabel("x")
            plt.title("Dichotomy method")
            plt.plot(epoch_history, x_history, color='r', linestyle='-')
            plt.pause(0.1)
        if abs(x1 - x0) < tol:
            plt.ioff()
            plt.show()
            return x1, epoch
        epoch_history.append(epoch)
        x_history.append(x1)
        x0 = x1

def Dichotomy_method_convergence_judgment(f, a, b):
    if f(a) * f(b) > 0:
        print("Error: f(%f) * f(%f) > 0, we can't ensure that there is root in the interval [%f, %f]" % (a, b, a, b))
        # format()函数用于格式化字符串
        print("Dichotomy method isn't recommended.")

# 测试
if __name__ == "__main__": # __name__是当前模块名，当模块被直接运行时模块名为__main__。没有被直接运行时模块名为文件名
    print("\n*****************************************************************")
    print("Dichotomy method test start...")
    print("*****************************************************************\n")
    def f(x):
        y = 5*x**3 - 1.3*x - 0.7
        return y
    a = -1
    b = 1
    tol = 1e-5
    maxiter = 1000
    x, epoch = Dichotomy_method(f, a, b, tol, maxiter, info=True, plot=True)
    if x is None or epoch is None:
        print("Dichotomy_method did not return valid values.")
    else:
        print("\nx = %f, epoch = %d\n" % (x, epoch))
    print("\n*****************************************************************")
    print("Dichotomy method test end...")
    print("*****************************************************************\n")
