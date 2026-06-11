import streamlit as st
import qrcode
from io import BytesIO

st.title("QRコード生成アプリ")

text = st.text_input("URLや文字を入力")

if text:
    img = qrcode.make(text)
    buf = BytesIO()
    img.save(buf)
    st.image(buf.getvalue())
