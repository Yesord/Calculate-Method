import math
import matplotlib.pyplot as plt

##############################################################################################################
# name: Newton_method
# function: 牛顿法
# parameter: f: 函数
#            df: f的导函数
#            x0: 初始值
#            tol: 精度要求
#            maxiter: 最大迭代次数
#            info: 是否输出迭代信息
#            plot: 是否输出迭代曲线
# return: x1: 迭代结果
#         epoch: 迭代次数
# date: 2023/11/21
# author: Yesord
# note 需要人工计算得到导函数以及验证是否收敛
##############################################################################################################

def Newton_method(f, df, x0, tol, maxiter, info=False, plot=False):
    if df == None:# 如果df没有定义，则使用数值微分
        df = lambda f, x: (f(x+1e-6) - f(x-1e-6)) / (2e-6) # lambda x: df(f, x)是一个匿名函数，等价于def df(x): return df(f, x)
    if plot:
        x_history = []
        epoch_history = []
    for epoch in range(maxiter):
        x1 = x0 - f(x0)/df(f, x0)
        if info:
            print("epoch = %d, x1 = %f" % (epoch, x1))
        if plot:# 绘制迭代过程
            plt.ion()
            plt.xlabel("epoch")
            plt.ylabel("x")
            plt.title("Newton method")
            plt.plot(epoch_history, x_history, color='r', linestyle='-')
            plt.pause(0.1)
        if abs(x1 - x0) < tol: # 精度达到要求输出结果
            plt.ioff()
            plt.show()
            return x1, epoch
        epoch_history.append(epoch) 
        x_history.append(x1)
        x0 = x1

# 收敛性判断
def Newton_method_convergence_judgment(f, df, x0):
    if df(f, x0) == 0:
        print("Error: df(%f) = 0, Newton method isn't recommended." % x0)


# 测试
if __name__ == "__main__": 
    f = lambda x: math.pow(x,3) - 2*math.pow(x,2) + 3*x - 4 # sample function
    df = lambda f, x: (f(x+1e-6) - f(x-1e-6)) / (2e-6) # lambda f,x :用于定义匿名函数，冒号前面的x表示函数参数，冒号后面的x表示函数返回值
    print("\n*****************************************************************")
    print("Newton method test start...")
    print("*****************************************************************\n")
    print("test function: f(x) = x**3 - 2*x**2 + 3*x - 4")
    #输出x0初值并将其转换成浮点数
    x0 = float(input("Please input the initial value x0: ")) 
    tol = 1e-6 # 精度要求
    maxiter = 100 # 最大迭代次数
    x, epoch = Newton_method(f, df, x0, tol, maxiter, info=True, plot=True) # Netwon method
    print("x = %f, epoch = %d" % (x, epoch))
    Newton_method_convergence_judgment(f, df, x0) # 收敛性判断
    print("\n*****************************************************************")
    print("Newton method test done!")
    print("*****************************************************************\n")
