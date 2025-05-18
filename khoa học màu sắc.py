import streamlit as st


st.set_page_config(
    page_title="KHOA HỌC MÀU SẮC",
    layout="wide"
)


st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }
    .member {
        text-align: center;
    }
    .right-align {
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)


col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col1:
    st.image("Logo_Trường_Đại_Học_Sư_Phạm_Kỹ_Thuật_TP_Hồ_Chí_Minh.png", width=200, caption="ĐH Sư phạm Kỹ thuật TP.HCM")

with col5:
    st.markdown("<div class='right-align'>", unsafe_allow_html=True)
    st.image("Logo_FGAM.png", width=200)
    st.markdown("<span style='font-size: 16px; font-family: Montserrat;'>Khoa In và Truyền thông</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; font-family: Montserrat; color: #FF5733;'>🎨 KHOA HỌC MÀU SẮC </h1>", unsafe_allow_html=True)
st.markdown("---")


st.markdown("<h2 style='text-align: center; font-family: Montserrat;'>👋 Chào mừng bạn đến với Project Khoa học màu sắc trên Streamlit của nhóm mình!</h2>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h3 style='text-align: center; font-family: Montserrat;'>👥 Thành viên nhóm</h3>", unsafe_allow_html=True)



col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])


with col2:
    st.markdown("<div style='text-align: center; font-family: Montserrat;'>", unsafe_allow_html=True)
    st.image("GMINH.jpg", width=150)
    st.markdown("**Gia Minh**<br>22158069", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center; font-family: Montserrat;'>", unsafe_allow_html=True)
    st.image("MTRAN.jpg", width=150)
    st.markdown("**Mỹ Trân**<br>22158099", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div style='text-align: center; font-family: Montserrat;'>", unsafe_allow_html=True)
    st.image("HUY.jpg", width=175)
    st.markdown("**Quốc Huy**<br>22158060", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
   