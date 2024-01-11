######################################################################
#name:      复化辛普森公式
#input:     f:被积函数 
#           a:积分下限
#           b:积分上限 
#           n:等分数
#output:    sum:积分结果
#note:      复化辛普森公式代数精度为3
######################################################################
def simpson(f,a,b,n):
    h = (b - a) / n # n等分有n+1个点 
    x = a
    sum = 0
    for i in range(1,n): # 1到n-1  range(1,n) = [1,2,3,...,n-1] 等于n-1个数
        x = x + h
        if i%2 == 0:
            sum = sum + 2*f(x)
        else:
            sum = sum + 4*f(x)
    sum = (h/3)*(f(a)+f(b)+sum)
    return sum

def trapezoid(f,a,b,n):
    h = (b - a) / n
    x = a
    middle = 0
    for i in range(1, n):
        x = x + h
        middle = middle + f(x)
    sum = (h / 2) * (f(a)+f(b)+2*middle)
    return sum

def f(x):
    return x**2

def test():
    print(simpson(f,0,1,1000))
    print(trapezoid(f,0,1,1000))

if __name__ == "__main__":
    test()