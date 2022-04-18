import random
import matplotlib.pyplot as plt
import math

# 生成20个随机点
generated_random_points = []
for i in range(20):
    generated_random_points.append([random.uniform(0, 10), random.uniform(0, 10)])

# 用Plt画出所有生成的点
plt.figure(figsize=(10, 10))
plt.scatter([p[0] for p in generated_random_points], [p[1] for p in generated_random_points], s=10)

min_index = 0
n = len(generated_random_points)
for i in range(0, n):
    if generated_random_points[i][1] < generated_random_points[min_index][1]:
        min_index = i
    elif generated_random_points[i][1] == generated_random_points[min_index][1] and generated_random_points[i][0] < \
            generated_random_points[min_index][0]:
        min_index = i

bottom_point = generated_random_points.pop(min_index)

# 排序
result_len = len(generated_random_points)
for i in range(result_len):
    generated_random_points[i].append(
        math.atan2(generated_random_points[i][1] - bottom_point[1],
                   generated_random_points[i][0] - bottom_point[0]))

generated_random_points.sort(key=lambda x: x[2])

sorted_points_length = len(generated_random_points)

if sorted_points_length < 2:
    print("Error: 点过少")
    exit - 1

result = []
result.append(bottom_point)
result.append(generated_random_points[0])
result.append(generated_random_points[1])

for i in range(2, sorted_points_length):
    result_len = len(result)
    top = result[result_len - 1]
    next_top = result[result_len - 2]
    v1 = [generated_random_points[i][0] - next_top[0], generated_random_points[i][1] - next_top[1]]
    v2 = [top[0] - next_top[0], top[1] - next_top[1]]

    while v1[0] * v2[1] - v1[1] * v2[0] >= 0:
        result.pop()
        result_len = len(result)
        top = result[result_len - 1]
        next_top = result[result_len - 2]
        v1 = [generated_random_points[i][0] - next_top[0], generated_random_points[i][1] - next_top[1]]
        v2 = [top[0] - next_top[0], top[1] - next_top[1]]

    result.append(generated_random_points[i])

# 画出边界点，并且连线
plt.plot([p[0] for p in result], [p[1] for p in result], 'r-')
# 把最后一个和第一个连接
plt.plot([result[-1][0], result[0][0]], [result[-1][1], result[0][1]], 'r-')
plt.show()
