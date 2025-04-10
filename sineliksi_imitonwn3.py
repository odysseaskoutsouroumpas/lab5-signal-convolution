import numpy as np
import matplotlib.pyplot as plt

# Δημιουργία δύο ημιτόνων με ίδια συχνότητα
n = np.arange(-20, 21)  # Δείκτες χρόνου
x = np.sin(0.5 * np.pi * n)  # Πρώτο ημίτονο
h = np.sin(0.5 * np.pi * n)  # Δεύτερο ημίτονο (ίδια συχνότητα)

# Συνέλιξη
y = np.convolve(x, h, mode='full')
n_conv = np.arange(2 * len(n) - 1) - (len(n) - 1)

# Σχεδίαση
plt.figure()
plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Πρώτο ημίτονο")

plt.subplot(3, 1, 2)
plt.stem(n, h)
plt.title("Δεύτερο ημίτονο (ίδια συχνότητα)")

plt.subplot(3, 1, 3)
plt.stem(n_conv, y) 
plt.title("Αποτέλεσμα συνέλιξης")

plt.tight_layout()
plt.show()

# Δοκιμή με διαφορετικές συχνότητες
h_diff = np.sin(0.25 * np.pi * n)  # Διαφορετική συχνότητα

# Συνέλιξη
y_diff = np.convolve(x, h_diff, mode='full')

# Σχεδίαση
plt.figure()
plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Πρώτο ημίτονο")

plt.subplot(3, 1, 2)
plt.stem(n, h_diff)
plt.title("Δεύτερο ημίτονο (διαφορετική συχνότητα)")

plt.subplot(3, 1, 3)
plt.stem(n_conv, y_diff)
plt.title("Αποτέλεσμα συνέλιξης")

plt.tight_layout()
plt.show()
