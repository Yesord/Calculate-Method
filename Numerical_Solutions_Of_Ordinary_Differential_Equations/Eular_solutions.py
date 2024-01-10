
################################################################
# name:     欧拉法
# function: 求解微分方程初值问题
#           形如 y'=f(x,y), y(x0)=y0
# input:    a,b: 区间
#           y0: 初值
#           f: 函数
#           h: 步长
# output:   x,y
# note:     1. 证明方式: 泰勒展开、数值积分（等效为左值积分）、数值微分
#           2. 欧拉法的精度为O(h)
#           3. 欧拉法的稳定性为O(h)
#           4. 欧拉法的收敛性为O(h)
#           5. 欧拉法的截断误差为O(h^2)->一阶欧拉方法
#           6. 欧拉法的截断误差主要来源于对f(x,y)的线性化
#           7. 使用隐式迭代法可以提高精度，手算常以直代曲，能显化就显化
################################################################

def Eular_Solution(a,b,y0,f,h):
    x = a
    y = y0
    n = (b-a)/h
    for i in range(int(n)):
        y = y + h*f(x,y)
        x = x + h
    return x,y 
    
################################################################
# 改进欧拉法
# input:   a,b: 区间
#          y0: 初值
#          g: 函数
#          h: 步长
# output:  x,y
# note:    1. 改进欧拉法的精度为O(h^2)
#          2. 改进欧拉法的误差为O(h^3) -> 二阶欧拉方法
#          3. 预估-校正本质通过低阶公式预估，高阶公式校正，因此误差为高阶公式的误差
################################################################

def Improved_Eular_Solution(a,b,y0,g,h):
    x = a
    y = y0
    n = (b-a)/h
    for i in range(int(n)):
        y1 = y + h*(g(x,y)) #预估公式 ： 一阶欧拉法
        y = y + h/2*(g(x,y)+g(x+h,y1)) #校正公式 ： 梯形公式
        x = x + h
    return y




################################################################
# 亚当斯-巴什福德预估-校正法
# a,b: 区间
# y0: 初值
# f: 函数
# h: 步长
# 返回值: x,y
################################################################
def Adams_Bashforth_Solution(a,b,y0,f,h):
    x = a
    y = y0
    n = (b-a)/h
    for i in range(int(n)):
        y = y + h*(3*f(x,y)-f(x-h,y-h*f(x-h,y-h*f(x-h,y))))/2
        x = x + h
    return y


def f(x,y):
    return y-2*x/y

def g(x,y):
    return y-2*x/y

def h(x):
    import math
    return math.sqrt(2*x+1)

def test():
    x, y = Eular_Solution(0,1,1,f,0.01)
    a = Improved_Eular_Solution(0,1,1,g,0.01)
    a1 = Adams_Bashforth_Solution(0,1,1,f,0.01)
    a2 = h(1)
    print("*****************************************************************")
    print("Eular_Solution test start...")
    print("*****************************************************************\n")
    print(f"y'=y-2*x/y, y(0)=1, h=0.01, x in [0,1]")
    print(f"Eular_Solution: {y} error: {abs(y-a2)}")
    print(f"Improved_Eular_Solution: {a} error: {abs(a-a2)}")
    print(f"Adams_Bashforth_Solution: {a1} error: {abs(a1-a2)}")
    print(f"real anwser:h(x)=sqrt(2*x+1) h(1)={a2}")
    print("\n*****************************************************************")
    print("Eular_Solution test end...")
    print("*****************************************************************")

if __name__ == "__main__":
    test()