import numpy as np

a = np.array([[2, 0, 1], [3, 5, 8], [6, 7, 9], [2, 4, 6], [2, 9, 5], [3, 6, 1], [1, 4, 7]])
# a = np.array([[2, 0], [3, 5], [6, 7], [2, 4], [2, 9]])
print(a)

x = a[:, 0]
print(x)

# b = np.zeros((5, 2))
# labels = np.array([1, 2, 0, 0, 2, 2, 1])

# s = np.zeros(3)
# c = 0

# # print("...", a[labels == 0][1][1])
# # print("axis 1__ ", np.min(a[labels == 2], axis=1), "___", np.mean(a[labels == 2], axis=1))
# # print("axis 0__ ", np.min(a[labels == 2], axis=0), "___", np.mean(a[labels == 2], axis=0))
# # # print(a[2][0])

# total_sum = 0
# mean_total_sum = 0
# for j in range(3):
#     print("j = ", j)
#     total_sum += np.sum(np.min((a[labels == j])**2, axis=1)) # Квадратичное отклонение
#     # mean_total_sum += np.sum((a[labels == 0])**2, axis = 0)
#     mean_total_sum += np.sum(np.min((a[labels == j])**2, axis=1)) / len(a[labels == j])
#     print ("total_sum", total_sum)
#     print ("mean_total_sum", mean_total_sum)

# print ("total_sum", total_sum)
# print ("mean_total_sum", mean_total_sum)


# for j in range(3):
#     b[j] = np.mean(a[labels == j], axis=1)
#     # print(a[labels == j])
# # print("j=",j, "  b",  b)
# print("b", b)

# for j in range(3):
#     # s[j] = np.sum(np.min(a[labels == j], axis=1))
#     c += np.sum(np.min(a[labels == j], axis=1)) 
#     # print(s)
# print(c)


# -----------------------------------------

