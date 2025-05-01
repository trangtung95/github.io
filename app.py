import streamlit as st

# Load danh sách email từ file
def load_emails():
    try:
        with open("emails.txt", "r") as f:
            emails = [line.strip().lower() for line in f if line.strip()]
        return emails
    except FileNotFoundError:
        return []

# Thiết lập giao diện
st.set_page_config(page_title="Tìm Email", page_icon="📧", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📧 Tìm Kiếm Email Trong Danh Sách")

emails = load_emails()

# Bố cục chia 2 cột
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔎 Nhập email để tìm")
    with st.form("email_form"):
        email_input = st.text_input("Email:", placeholder="nhập email tại đây...")
        submitted = st.form_submit_button("Tìm")

with col2:
    st.subheader("📋 Kết quả")
    if submitted:
        email_lower = email_input.strip().lower()
        if email_lower in emails:
            st.success(f"✅ Email tìm thấy: **{email_input.strip()}**")
        else:
            st.error("❌ Không tìm thấy email trong danh sách.")
    else:
        st.info("Kết quả sẽ hiển thị ở đây sau khi nhấn Tìm.")

