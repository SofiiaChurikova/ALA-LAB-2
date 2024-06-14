import numpy


def eigen_values_vectors(object):
    # Перевірка чи квадратні матриці
    if object.shape[0] != object.shape[1]:
        print("Enter a square matrix!")
    # Знаходимо власні значення і власні вектори
    # Вектори нормалізовані
    eigenvalues, eigenvectors = numpy.linalg.eig(object)
    # Перевірка Av = λv
    for i in range(len(eigenvectors)):
        Av = numpy.dot(object, eigenvectors[:, i])
        λv = eigenvalues[i] * eigenvectors[:, i]
        if numpy.allclose(Av, λv):
            print(f"Eigenvector {i + 1}: Av = λv")
        else:
            print(f"Eigenvector {i + 1}: Av != λv")
    return eigenvalues, eigenvectors


matrix = numpy.array([[2, 10],
                      [1, 1]])
eigenvalues, eigenvectors = eigen_values_vectors(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
