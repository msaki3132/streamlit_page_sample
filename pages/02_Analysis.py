import streamlit as st

st.set_page_config(page_title="詳細分析", page_icon="🔍")

st.title("🔍 詳細分析ページ")

st.write("ここでは詳細な数値をチェックできます。")

# インタラクティブな操作例
number = st.slider("分析のしきい値を選択", 0, 100, 50)
st.write(f"現在の設定値: {number}")

if number > 80:
    st.warning("数値が高すぎます！")
else:
    st.success("正常な範囲内です。")
