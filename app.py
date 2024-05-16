from openai import OpenAI
import streamlit as st
import requests
from PIL import Image

# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("🫧 나에게 어울리는 AI 캐릭터 만들기 🫧")


options = st.multiselect(
    label= "당신을 표현하는 말은?",
    # options=["웃긴","재치있는","자상한","경청하는","점잖은","까불대는","요란스러운","말이많은","냉소적인","MBTI ISTJ","MBTI ENFP","MBTI ENTJ","MBTI INTP","조용한","신중한"],
    options=["자유로운 영혼","성격이 급함","모험가스러운","쿨함","따뜻한 감성을 지닌","성실함","온화함","통찰력이 뛰어난","다양함을 존중하는","분위기 메이커","열정적인","풍부한 상상력을 가진","현실적인","배려를 잘하는","협동적인","에너지가 넘치는","신중한","문제해결을 잘하는","인내심이 강함","긍정적인","리더쉽있는","논리적인","원칙주의적인"]
    )
  

if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
 
if st.button("캐릭터 생성하기"):
    if options:
      with st.spinner('캐릭터 생성중...'):
        prompt = ", ".join(options) + "의 특징을 잘 살려서 특징들을 가지고 있는 하나의 생물의 모습을 픽사 애니매이션처럼 그려줘. 최대한 내가 묘사한 것과 같게 만들어줘"
        
        st.session_state.messages.append({"content": prompt})
        
        client = OpenAI()
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"{prompt}",
            size="1024x1024",
            quality="standard",
            n=1,
        )   

        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt
    
    st.image(
        Image.open(requests.get(image_url, stream=True).raw),
        caption=f"{revised_prompt}",
        use_column_width=True,
    )

    st.session_state.messages.append({"role": "assistant", "content": [image_url, revised_prompt]})
