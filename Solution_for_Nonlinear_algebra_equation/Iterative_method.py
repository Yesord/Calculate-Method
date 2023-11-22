import math
import matplotlib.pyplot as plt

##############################################################################################################
# name: iterative_method
# function: 迭代法
# parameter: g: 迭代函数
#            x0: 初始值
#            tol: 精度要求
#            maxiter: 最大迭代次数
#            info: 是否输出迭代信息
#            plot: 是否输出迭代曲线
# return: x1: 迭代结果
#         epoch: 迭代次数
# date: 2023/11/21
# author: Yesord
# note 需要人工计算得到迭代函数以及验证是否收敛
##############################################################################################################

# 迭代法
def iterative_method(g, x0, tol, maxiter, info=False, plot=False):
    if plot:
        x_history = []
        epoch_history = []
    for epoch in range(maxiter):
        x1 = g(x0)
        if info:
            print("epoch = %d, x1 = %f" % (epoch, x1))
        if plot:# 绘制迭代过程
            plt.ion()
            plt.xlabel("epoch")
            plt.ylabel("x")
            plt.title("Iterative method")
            plt.plot(epoch_history, x_history, color='r', linestyle='-')
            plt.pause(0.1)
        if abs(x1 - x0) < tol:
            plt.ioff()
            plt.show()
            return x1, epoch
        epoch_history.append(epoch)
        x_history.append(x1)
        x0 = x1




# 测试



if __name__ == "__main__": 
    print("\n*****************************************************************")
    print("Iterative method test start...")
    print("*****************************************************************\n")
    def g(x): # 迭代函数
        y = x - (x**3 - 2*x**2 + 3*x - 1)/(3*x**2 - 4*x + 3)
        return y
    x0 = float(input("Please input the initial value x0: "))
    tol = 1e-5
    maxiter = 1000
    x, epoch = iterative_method(g, x0, tol, maxiter, info=True, plot=True)
    print("\nx = %f, epoch = %d\n" % (x, epoch))
    print("*****************************************************************")
    print("Iterative method test end...")
    print("*****************************************************************\n")
    