import streamlit as st

st.set_page_config(page_title="設定", page_icon="⚙️")

st.title("⚙️ 設定画面")

st.write("アプリの動作環境をカスタマイズします。")

# 切り替えボタンの例
st.toggle("ダークモード（仮）")
st.toggle("通知を有効にする")

if st.button("全データをリセット"):
    st.session_state["user_data"] = "未入力"
    st.rerun() # ページを再読み込み
