import numpy as np
from random import uniform as rand
from math import sqrt

n = 10
A = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        A[i][j] = round(rand(1, 10), 2)
        A[j][i] = A[i][j]
print('Эрмитова матрица: \n', A)

eigen_values, eigen_vectors = np.linalg.eig(A)
for i in range(n):
    eigen_values[i] = round(eigen_values[i], 2)
    for j in range(n):
        eigen_vectors[i][j] = round(eigen_vectors[i][j], 2)
print('Собственные векторы: \n', eigen_vectors)
print('Собственные значения: \n', eigen_values)

eigen_values_1, eigen_vectors_1 = np.linalg.eigh(A)
for i in range(n):
    eigen_values_1[i] = round(eigen_values_1[i], 2)
    for j in range(n):
        eigen_vectors_1[i][j] = round(eigen_vectors_1[i][j], 2)
print('Собственные векторы: \n', eigen_vectors_1)
print('Собственные значения: \n', eigen_values_1)

v = np.zeros(n)
for i in range(n):
    v[i] = round(rand(1, 10), 2)


def norm(vec):
    n = len(vec)
    r = 0
    for i in range(n):
        r += vec[i] ** 2
    return sqrt(r)


def normalize(vec, norm_vec):
    n = len(vec)
    for i in range(n):
        vec[i] = vec[i] / norm_vec
    return vec

K = 10
for i in range(K):
    v = np.dot(A, v)
    v = normalize(v, norm(v))
print(v)
print('Наибольшее собственное значение: \n', round((np.dot(A, v)[0] / v[0]), 2))
