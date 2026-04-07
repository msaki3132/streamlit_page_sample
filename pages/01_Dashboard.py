import streamlit as st

st.title("📊 ダッシュボード")
st.write("ここはダッシュボードページです。")

# ページ固有の処理をここに書く
data = [10, 20, 30]
st.line_chart(data)
