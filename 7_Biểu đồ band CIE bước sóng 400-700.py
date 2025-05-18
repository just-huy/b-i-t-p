import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

cie_data = np.array([
    [0.1738, 0.0048, 400],
    [0.1736, 0.0046, 410],
    [0.1733, 0.0044, 420],
    [0.1728, 0.0042, 430],
    [0.1721, 0.0040, 440],
    [0.1712, 0.0038, 450],
    [0.1700, 0.0036, 460],
    [0.1686, 0.0034, 470],
    [0.1669, 0.0032, 480],
    [0.1649, 0.0030, 490],
    [0.1624, 0.0028, 500],
    [0.1595, 0.0026, 510],
    [0.1562, 0.0024, 520],
    [0.1524, 0.0022, 530],
    [0.1480, 0.0020, 540],
    [0.1430, 0.0018, 550],
    [0.1373, 0.0016, 560],
    [0.1310, 0.0014, 570],
    [0.1240, 0.0012, 580],
    [0.1163, 0.0010, 590],
    [0.1078, 0.0008, 600],
    [0.0986, 0.0006, 610],
    [0.0887, 0.0004, 620],
    [0.0782, 0.0002, 630],
    [0.0670, 0.0001, 640],
    [0.0551, 0.0000, 650],
    [0.0425, 0.0000, 660],
    [0.0292, 0.0000, 670],
    [0.0152, 0.0000, 680],
    [0.0006, 0.0000, 690],
    [0.0000, 0.0000, 700],
])

x = cie_data[:, 0]
y = cie_data[:, 1]
wavelengths = cie_data[:, 2]

fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(x, y, c=wavelengths, cmap='nipy_spectral', s=80, edgecolors='k')
ax.plot(x, y, color='black', linewidth=1)
ax.set_title("Biểu đồ sắc độ CIE 1931 (400–700 nm)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(0, 0.8)
ax.set_ylim(0, 0.9)
ax.grid(True)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Bước sóng (nm)")
plt.tight_layout()

st.pyplot(fig)
