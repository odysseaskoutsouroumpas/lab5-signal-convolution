import numpy as np
import matplotlib.pyplot as plt

# Δημιουργία δύο τετραγωνικών παλμών
n = np.arange(-10, 11)  # Δείκτες χρόνου
x = np.where((n >= -5) & (n <= 5), 1, 0)  # Τετραγωνικός παλμός
h = np.where((n >= -5) & (n <= 5), 1, 0)  # Δεύτερος τετραγωνικός παλμός

# Συνέλιξη σημάτων
y = np.convolve(x, h, mode='full')
n_conv = np.arange(2 * len(n) - 1) - (len(n) - 1)  # Δείκτες συνέλιξης

# Σχεδίαση αποτελέσματος
plt.figure()
plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Πρώτος τετραγωνικός παλμός")

plt.subplot(3, 1, 2)
plt.stem(n, h)
plt.title("Δεύτερος τετραγωνικός παλμός")

plt.subplot(3, 1, 3)
plt.stem(n_conv, y)
plt.title("Αποτέλεσμα συνέλιξης (τριγωνικό σήμα)")

plt.tight_layout()
plt.show()
