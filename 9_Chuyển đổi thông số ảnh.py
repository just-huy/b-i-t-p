import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Chuyển ảnh sang CMYK TIFF 300PPI", layout="centered")
st.title("🖼️ Chuyển đổi ảnh sang CMYK • TIFF • 300 PPI")

uploaded = st.file_uploader("📤 Tải lên ảnh bất kỳ", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "heic"])

if uploaded:
    try:
        img = Image.open(uploaded)

        st.image(img, caption="Ảnh gốc", use_column_width=True)
        dpi_goc = img.info.get("dpi", (72, 72))

        st.markdown("### ℹ️ Thông tin ảnh gốc")
        st.write(f"**Định dạng file:** {img.format}")
        st.write(f"**Kích thước:** {img.width} × {img.height} px")
        st.write(f"**Không gian màu:** `{img.mode}`")
        st.write(f"**Độ phân giải:** {dpi_goc[0]} × {dpi_goc[1]} PPI")

       
        img_cmyk = img.convert("CMYK")
        buffer = io.BytesIO()
        img_cmyk.save(buffer, format="TIFF", dpi=(300, 300))
        buffer.seek(0)

       
        img_out = Image.open(buffer)
        st.markdown("---")
        st.image(img_out, caption="Ảnh sau khi chuyển", use_column_width=True)

        st.markdown("### 🧾 Thông tin sau chuyển đổi")
        st.write("**Định dạng file:** .TIFF")
        st.write(f"**Kích thước:** {img_out.width} × {img_out.height} px")
        st.write(f"**Không gian màu:** `{img_out.mode}`")
        dpi_new = img_out.info.get("dpi", (300, 300))
        st.write(f"**Độ phân giải:** {dpi_new[0]} × {dpi_new[1]} PPI")

        st.download_button(
            label="📥 Lưu file .TIFF",
            data=buffer,
            file_name="converted_CMYK_300ppi.tiff",
            mime="image/tiff"
        )

    except Exception as e:
        st.error(f"🚫 Lỗi khi xử lý ảnh: {e}")
else:
    st.info("⬆️ Hãy chọn một hình ảnh để bắt đầu.")
