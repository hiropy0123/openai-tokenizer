import streamlit as st
import tiktoken

# タイトル
st.title("OpenAI トークン数計測アプリ")

# モデルの選択
model = st.selectbox("モデルを選択してください", ["GPT-4o", "GPT-4", "GPT-3.5"])

# モデルに基づくエンコーディングの設定
if model == "GPT-4o":
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4oもGPT-4と同じトークナイザーを使用
elif model == "GPT-4":
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4のトークナイザー
else:
    encoding = tiktoken.get_encoding("p50k_base")    # GPT-3.5のトークナイザー

# テキスト入力欄
user_text = st.text_area("トークン数を計測したいテキストを入力してください")

# トークン数の計算と表示
if user_text:
    tokens = encoding.encode(user_text)
    token_count = len(tokens)
    
    # 大きなフォントサイズでトークン数を表示
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>トークン数: {token_count}</h2>", unsafe_allow_html=True)
else:
    st.write("テキストを入力してください。")

# メモ
st.caption("トークン数の計測は、選択されたモデルに基づいて行われます。")