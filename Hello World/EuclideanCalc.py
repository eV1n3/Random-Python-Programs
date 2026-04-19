import sys

# Variable Assignment
data_set1_input = input("Input data set 1 (each number separated by a space and no commas): ")
data_set_tmp = data_set1_input.split()
data_set1 = [float(num) for num in data_set_tmp]

data_set2_input = input("Input data set 2 (each number separated by a space and no commas): ")
data_set_tmp = data_set2_input.split()
data_set2 = [float(num) for num in data_set_tmp]

# Making sure arrays are same size
if len(data_set1) != len(data_set2):
    print("Data sets must be equal length")
    sys.exit()

# (x1 - y1)^2 ...
euclidean_data_set = [num for num in range(len(data_set1))]
for idx in range(len(data_set1)):
    euclidean_data_set[idx] = data_set2[idx] - data_set1[idx]
    euclidean_data_set[idx] = euclidean_data_set[idx] ** 2

# Sum of euclidean_data_set
euclidean_data_set_sum = 0
for num in euclidean_data_set:
    euclidean_data_set_sum += num

# Sqrt of euclidean_data_set_sum
euclidean_distance = euclidean_data_set_sum ** 0.5

print("Euclidean Distance:", euclidean_distance)