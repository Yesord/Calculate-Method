################################################################
# 四阶龙格-库塔法
# a,b: 区间
# y0: 初值
# f: 函数
# h: 步长
# 返回值: x,y
################################################################

def Runge_Kutta_Solution(a,b,y0,f,h):
    x = a
    y = y0
    n = (b-a)/h
    for i in range(int(n)):
        k1 = h*f(x,y)
        k2 = h*f(x+h/2,y+k1/2)
        k3 = h*f(x+h/2,y+k2/2)
        k4 = h*f(x+h,y+k3)
        y = y + (k1+2*k2+2*k3+k4)/6
        x = x + h
    return y

def f(x,y):
    return y-2*x/y

def h(x):
    import math
    return math.sqrt(2*x+1)

def test():
    a1 = Runge_Kutta_Solution(0,1,1,f,0.1)
    a2 = Runge_Kutta_Solution(0,1,1,f,0.01)
    a3 = h(1)
    print(f"Runge_Kutta_Solution (h=0.1): {a1} error: {abs(a3-a1)}")
    print(f"Runge_Kutta_Solution (h=0.01): {a2} error: {abs(a3-a2)}")
    print(f"real anwser:h(x)=sqrt(2*x+1) h(1)={a3}")

if __name__ == "__main__":
    test()