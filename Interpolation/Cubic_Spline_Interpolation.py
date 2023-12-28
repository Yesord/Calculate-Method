import numpy as np
import matplotlib.pyplot as plt


######################################################################################################
# 三次样条插值
# data_points_x: 数据点的x坐标
# data_points_y: 数据点的y坐标
# test_points_x: 测试点的x坐标
######################################################################################################

def cubic_spline_interpolation(data_points_x, data_points_y, test_points_x):
    # 计算每个区间的系数
    def calculate_coefficients(data_points_x, data_points_y):
        num_data_points = len(data_points_x)
        intervals = np.zeros(num_data_points - 1)
        for i in range(num_data_points - 1):
            intervals[i] = data_points_x[i + 1] - data_points_x[i]
        # 构造系数矩阵
        coefficient_matrix = np.zeros((num_data_points, num_data_points))
        coefficient_matrix[0, 0] = 1
        coefficient_matrix[num_data_points - 1, num_data_points - 1] = 1
        for i in range(1, num_data_points - 1):
            coefficient_matrix[i, i - 1] = intervals[i - 1]
            coefficient_matrix[i, i] = 2 * (intervals[i - 1] + intervals[i])
            coefficient_matrix[i, i + 1] = intervals[i]
        # 构造右端向量
        right_vector = np.zeros(num_data_points)
        for i in range(1, num_data_points - 1):
            right_vector[i] = 3 * ((data_points_y[i + 1] - data_points_y[i]) / intervals[i] - (data_points_y[i] - data_points_y[i - 1]) / intervals[i - 1])
        # 解线性方程组
        c_coefficients = np.linalg.solve(coefficient_matrix, right_vector)
        # 计算d和b
        d_coefficients = np.zeros(num_data_points - 1)
        b_coefficients = np.zeros(num_data_points - 1)
        for i in range(num_data_points - 1):
            d_coefficients[i] = (c_coefficients[i + 1] - c_coefficients[i]) / (3 * intervals[i])
            b_coefficients[i] = (data_points_y[i + 1] - data_points_y[i]) / intervals[i] - intervals[i] * (2 * c_coefficients[i] + c_coefficients[i + 1]) / 3
        return b_coefficients, c_coefficients, d_coefficients

    # 计算每个区间的系数
    b_coefficients, c_coefficients, d_coefficients = calculate_coefficients(data_points_x, data_points_y)
    # 计算插值结果
    num_data_points = len(data_points_x)
    num_test_points = len(test_points_x)
    test_points_y = np.zeros(num_test_points)
    for i in range(num_test_points):
        for j in range(num_data_points - 1):
            if test_points_x[i] >= data_points_x[j] and test_points_x[i] <= data_points_x[j + 1]: # 判断测试点是否在当前区间内
                test_points_y[i] = data_points_y[j] \
                      + b_coefficients[j] * (test_points_x[i] - data_points_x[j]) \
                          + c_coefficients[j] * (test_points_x[i] - data_points_x[j]) ** 2 \
                              + d_coefficients[j] * (test_points_x[i] - data_points_x[j]) ** 3 
                # 计算插值结果 dx^3+cx^2+bx+a
    return test_points_y


if __name__ == '__main__':
    
    data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    data_y = np.array([110, 31, 12, 53, 34, 51, 11, 131])
    test_points_x = np.linspace(0, 7, 100) # 生成0到5之间的100个点
    test_points_y = cubic_spline_interpolation(data_x, data_y, test_points_x)

    plt.figure(figsize=(8, 6))
    plt.subplot(211)
    plt.title('Before Cubic Spline Interpolation')
    plt.plot(data_x, data_y, 'bo')
    plt.ylabel('y')
    plt.subplot(212)
    plt.plot(test_points_x, test_points_y, 'r')
    plt.title('After Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()