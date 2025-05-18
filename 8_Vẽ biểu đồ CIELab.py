import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🎨 Biểu đồ CIELab & Phân tích sự chuyển dịch màu")

st.markdown("Nhập thông số của hai màu trong không gian **CIELab**:")

st.sidebar.header("🎯 Màu Lab1")
L1 = st.sidebar.slider("L1*", 0.0, 100.0, 50.0)
a1 = st.sidebar.slider("a1*", -128.0, 127.0, 20.0)
b1 = st.sidebar.slider("b1*", -128.0, 127.0, 30.0)

st.sidebar.header("🎯 Màu Lab2")
L2 = st.sidebar.slider("L2*", 0.0, 100.0, 60.0)
a2 = st.sidebar.slider("a2*", -128.0, 127.0, 10.0)
b2 = st.sidebar.slider("b2*", -128.0, 127.0, 40.0)

delta_L = L2 - L1
delta_a = a2 - a1
delta_b = b2 - b1
delta_E = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)

fig, ax = plt.subplots(figsize=(7, 6))
ax.plot(a1, b1, 'ro', label='Lab1 (%.1f, %.1f, %.1f)' % (L1, a1, b1))
ax.plot(a2, b2, 'go', label='Lab2 (%.1f, %.1f, %.1f)' % (L2, a2, b2))
ax.arrow(a1, b1, delta_a, delta_b, head_width=2.0, head_length=3.0, fc='blue', ec='blue')

ax.set_xlabel('a* (xanh lá ←→ đỏ)')
ax.set_ylabel('b* (xanh dương ←→ vàng)')
ax.set_title("Biểu đồ CIELab (mặt phẳng a* – b*)")
ax.set_xlim(-128, 128)
ax.set_ylim(-128, 128)
ax.grid(True)
ax.set_aspect('equal')
ax.legend()

st.pyplot(fig)

st.subheader("🧾 Nhận xét sự chuyển dịch màu:")
st.write(f"🔹 ΔL* = **{delta_L:.2f}** → {'Sáng hơn 🌞' if delta_L > 0 else 'Tối hơn 🌚'}")
st.write(f"🔹 Δa* = **{delta_a:.2f}** → {'Ngả về đỏ ❤️' if delta_a > 0 else 'Ngả về xanh lá 💚'}")
st.write(f"🔹 Δb* = **{delta_b:.2f}** → {'Ngả về vàng 💛' if delta_b > 0 else 'Ngả về xanh dương 💙'}")
st.write(f"🔹 ΔE* = **{delta_E:.2f}** → Độ khác biệt màu tổng thể")
