# 3. Напишіть програму, що визначає добуток двох квадратних
# матриць 3*3 (необхідно враховувати розмірність). Результати множення
# елементів занесіть до нової матриці та виведіть її на екран

# Importing modules
import numpy as np

array1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
array2 = np.array([[8, 9, 10], [11, 12, 13], [14, 15, 16]])

array3 = array1 * array2
print(array3)