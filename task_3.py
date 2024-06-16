import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diaogonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diaogonalized_key_matrix, message_vector)
    return encrypted_vector


def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diaogonalized_key_matrix_inv = np.dot(np.dot(eigenvectors, np.diag(1 / eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(diaogonalized_key_matrix_inv, encrypted_vector)
    decrypted_message = ""
    for num in decrypted_vector:
        decrypted_char = chr(int(np.round(np.real(num))))
        decrypted_message += decrypted_char
    return decrypted_message


message = "Hello, world!"
print(f"Original message: {message}")
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
encrypted_message = encrypt_message(message, key_matrix)
print(f"Encrypt Message:", encrypted_message)
decrypted_message = decrypt_message(encrypted_message, key_matrix)
print("Decrypted Message:", decrypted_message)
