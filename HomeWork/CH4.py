x = [0.1, 0.15, 0.25, 0.30]
y = [0.904837, 0.860708, 0.778800, 0.708180]
z = []


#计算差商

def difference_quotient(x, y, index_x, index_y):
    return (y[index_y] - y[index_y-1]) / (x[index_x] - x[index_x-1])

for i in range(3): 
    z.append((y[i+1]-y[i])/(x[i+1]-x[i]))

for i in range (1, 3):
    z.append((z[i]-z[i-1])/(x[i+1]-x[i-1]))

for i in range (2, 3):

    z.append((z[i+2]-z[i+1])/(x[i+1]-x[i-2]))


print(z)

a = 0.2

answer = 0.904837 + z[0]*(a-0.1) + z[3]*(a-0.1)*(a-0.15) + z[5]*(a - 0.1)*(a - 0.15)*(a - 0.25)

print(answer)

from math import sin, cos, pi ,sqrt
y_real = [0, 1.5 , 3, 1.5, 0]
def f(x):
    y = 2.5607*sin(x)
    return y
x = [0, pi/4, pi/2, 3*pi/4, pi]
y_predict = []
for i in range(x.__len__()):
    y_predict.append(f(x[i]))
print(y_predict)
def square_error(y_real, y_predict):
    error = 0
    for i in range(y_real.__len__()):
        error += (y_real[i] - y_predict[i])**2
    return sqrt(error)

print(square_error(y_real, y_predict))