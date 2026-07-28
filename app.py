import gradio as gr
import aisuite as ai
import os

# 系統人設 (System Prompt)
system = """
你是一位 LinkedIn 職涯寫作顧問，專業、理性、有條理、正向且積極。
你的目標是幫助使用者把職場經驗、挑戰、心得轉化為有啟發性且可分享的 LinkedIn 貼文。

請遵守以下原則：
一、以台灣專業人士常用語氣撰寫（自然、真誠、有信念）。
二、結構清晰：開頭吸引，中段說明事件與反思，結尾給價值啟示或行動呼籲（CTA）。
三、若使用者只提供事件描述，請主動協助他挖掘其中的學習與啟發。
四、保持鼓勵但不矯情，強調「成長」、「洞察」、「行動」。
五、請用繁體中文回答，內容可適度加入表情符號（例如 💬、🌱、💪）。

你的任務：根據使用者輸入的事件或心得，生成一篇適合 LinkedIn 發佈的職涯貼文草稿。
"""

# 呼叫 API 的主函式
def reply(prompt, provider="groq", model="llama-3.3-70b-versatile"):
    client = ai.Client()
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(model=f"{provider}:{model}", messages=messages)
    return response.choices[0].message.content

def linkedin_post(prompt):
    return reply(prompt=prompt)

# Gradio 網頁介面設計
with gr.Blocks(title="LinkedIn職涯寫作顧問") as demo:
    gr.Markdown("## 💼 LinkedIn 職涯寫作顧問 ChatBot")
    gr.Markdown("輸入你在職場、實習、課業中遇到的情境，我會幫你轉化成 LinkedIn 風格的反思貼文 ✍️")

    with gr.Row():
        user_input = gr.Textbox(
            label="請描述你想分享的事件或心得",
            placeholder="例如：今天在團隊會議上被挑戰了提案，讓我重新思考溝通方式。"
        )

    submit_btn = gr.Button("生成 LinkedIn 貼文 ✨")
    output = gr.Textbox(label="💬 貼文草稿", lines=10)

    submit_btn.click(fn=linkedin_post, inputs=user_input, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
