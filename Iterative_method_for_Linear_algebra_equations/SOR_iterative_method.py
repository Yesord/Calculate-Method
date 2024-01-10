import numpy as np
import math
import matplotlib.pyplot as plt

# SOR迭代法
##############################################################################################################
# name: SOR_iterative_method
# function: SOR迭代法
# parameter: A: 系数矩阵
#            b: 常数项
#            x0: 初始值
#            w: 松弛因子
#            tol: 精度要求
#            max_iter: 最大迭代次数
#            info: 是否输出迭代信息
#            plot: 是否输出迭代曲线,仅支持三元方程组
# return: x1: 迭代结果
#         epoch: 迭代次数
# date: 2023/11/20
# author: xrl
##############################################################################################################

def SOR_iterative_method(A, b, x0, w, tol, max_iter, info=False, plot=False):
    A = np.array(A) # 转换为numpy数组
    b = np.array(b) # 转换为numpy数组
    x0 = np.array(x0) # 转换为numpy数组
    n = len(A) # 方程组的阶数
    x1 = np.zeros(n) # 初始化x1
    epoch = 0 # 迭代次数
    if plot and n == 3:
        x1_history = []
        x2_history = []
        x3_history = []
        epoch_value = []

    for epoch in range(max_iter): # SOR迭代
        for i in range(n):
            x1[i] = b[i] 
            for j in range(n):
                if i != j: # 不是对角元素
                    x1[i] -= A[i][j] * x1[j] 
            x1[i] /= A[i][i]
            x1[i] = (1 - w) * x0[i] + w * x1[i]
        
        if info: # 输出迭代信息
            print("x^= ", x1) # 输出结果
            print("epoch= ", epoch) # 输出迭代次数

        if plot and n == 3: # 输出迭代曲线
            
            x1_history.append(x1[0])
            x2_history.append(x1[1])
            x3_history.append(x1[2])
            epoch_value.append(epoch)

            plt.ion() # 打开交互模式
            plt.xlabel("epoch") # 设置x轴标签
            plt.ylabel("x_iterative") # 设置y轴标签
            plt.title("SOR iterative method") # 设置标题

            line_x1, = plt.plot(epoch_value, x1_history, 'r.-') # 画x1图 r.-表示红色点线图
            line_x2, = plt.plot(epoch_value, x2_history, 'g.-') # 画x2图 g.-表示绿色点线图
            line_x3, = plt.plot(epoch_value, x3_history, 'b.-') # 画x3图 b.-表示蓝色点线图
            
            plt.pause(0.1)  
                
        if np.linalg.norm(x1 - x0) < tol: # 判断是否满足精度要求
            if plot:
                line_x1.set_label("x1") # 设置图例
                line_x2.set_label("x2") 
                line_x3.set_label("x3") 
                plt.legend() # 显示图例
                plt.ioff() # 关闭交互模式
                plt.show() # 显示图像
            break
        x0 = x1.copy() # 更新x0
        
    
    return x1, epoch # 返回结果

# 测试
def test():
    print("\n*****************************************************************")
    print("SOR iterative method test start...")
    print("*****************************************************************\n")
    x0 = [0, 0, 0] # 初始值
    A = [[4,3,0], [3,4,-1], [0,-1,4]] # 系数矩阵
    B = [16,20,-12] # 常数项
    w = 1.24 # 松弛因子
    tol = 1e-3 # 精度要求
    max_iter = 100 # 最大迭代次数
    x, epoch = SOR_iterative_method(A, B, x0, w, tol, max_iter,info=True, plot=True) # SOR迭代法
    print("*****************************************************************")
    print("SOR iterative method test end...")
    print("*****************************************************************\n")
    return x, epoch

if __name__ == "__main__":     
    test()