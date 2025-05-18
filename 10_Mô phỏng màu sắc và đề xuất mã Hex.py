import streamlit as st
from PIL import Image
import numpy as np
from colormath.color_objects import sRGBColor, CMYColor
from colormath.color_conversions import convert_color
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phân tích màu từ ảnh", layout="centered")
st.title("🎯 Phân tích màu từ ảnh & chuyển sang CMYK")

uploaded_file = st.file_uploader("📤 Tải lên ảnh chứa màu bạn muốn phân tích", type=["jpg", "jpeg", "png", "bmp", "tiff"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Ảnh đã tải lên", use_column_width=True)

        img_np = np.array(image)
        h, w, _ = img_np.shape
        center_crop = img_np[h//2-5:h//2+5, w//2-5:w//2+5]
        avg_color = center_crop.mean(axis=(0, 1))
        r, g, b = [int(x) for x in avg_color]

        # Chuyển sang CMY
        srgb = sRGBColor(r / 255, g / 255, b / 255)
        cmy = convert_color(srgb, CMYColor)
        c, m, y = cmy.cmy_c * 100, cmy.cmy_m * 100, cmy.cmy_y * 100

        # Ước tính K
        k = 100 - max(r, g, b) * 100 / 255

        hex_code = '#{:02X}{:02X}{:02X}'.format(r, g, b)

        st.subheader("🎨 Màu phân tích")
        color_patch = Image.new("RGB", (200, 100), (r, g, b))
        st.image(color_patch, caption="Màu trích xuất", use_column_width=False)

        st.markdown("### 🔍 Thông số màu:")
        st.write(f"**RGB:** ({r}, {g}, {b})")
        st.write(f"**CMYK:** C={c:.1f}%, M={m:.1f}%, Y={y:.1f}%, K={k:.1f}%")
        st.write(f"**Mã Hex (cho Illustrator):** `{hex_code}`")
        st.code(hex_code)

        # Biểu đồ phần trăm CMYK
        st.markdown("### 📊 Biểu đồ phần trăm CMYK")

        fig, ax = plt.subplots()
        ax.bar(['Cyan', 'Magenta', 'Yellow', 'Black'], [c, m, y, k],
               color=['cyan', 'magenta', 'yellow', 'black'])
        ax.set_ylabel('Phần trăm (%)')
        ax.set_ylim(0, 100)
        ax.set_title('Tỷ lệ các kênh màu CMYK')

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Lỗi khi xử lý ảnh: {e}")
else:
    st.info("📎 Vui lòng tải lên một ảnh màu đơn để bắt đầu.")
