# import streamlit as st
# import google.generativeai as genai

# # 1. تفعيل الاتصال الرسمي المستقر بسيرفر Google Gemini
# # الصق مفتاحك السري (AIza...) بدقة بين العلامتين بالأسفل
# GEMINI_API_KEY = "AQ.Ab8RN6JEE1zm0sddgPusiEZlFWUryogGTInLwca17-AP67qR5g"
# genai.configure(api_key=GEMINI_API_KEY)

# # 2. إعدادات وتصميم واجهة يومي البنفسجية الفخمة
# st.set_page_config(page_title="Yomi AI", page_icon="💬", layout="centered")

# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0f020f; /* ثيم بنفسجي داكن */
#     }
#     h1 {
#         color: #d633d6 !important; /* اسم يومي المضيء */
#         text-align: center;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("YOMI AI v1.0")
# st.write("<p style='text-align:center; color:#bbb;'>Powered by Google Gemini - Mapped to Yousif!</p>", unsafe_allow_html=True)

# # 3. مصفوفة الذاكرة وحفظ التاريخ
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "Hi developer! I am Yomi, your smart AI powered by Google. Ask me any programming or school question! 😊"}]

# # 4. عرض المحادثة السابقة
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # 5. استقبال المدخلات من حقل الشات
# if user_input := st.chat_input("Ask Yomi something..."):
#     # عرض سؤالك فوراً
#     with st.chat_message("user"):
#         st.write(user_input)
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     # 6. محرك التوليد الرسمي من Google مع تلقين الأدب البرمجي
#     with st.chat_message("assistant"):
#         with st.spinner("Yomi is thinking... 🧠"):
#             try:
#                 # تلقين النظام لإجبار الـ AI على احترام صانعه يوسف وشكره دائماً
#                 system_instruction = "Your name is Yomi, a smart AI assistant made by the brilliant developer Yousif. You must always be polite, respectful, and deeply thankful to your creator Yousif when he speaks to you."
                
#                 # استدعاء نموذج جيميناي مع دمج التعليمات
#                 model = genai.GenerativeModel(
#                     model_name='gemini-1.5-flash',
#                     system_instruction=system_instruction
#                 )
                
#                 response_data = model.generate_content(user_input)
#                 response = response_data.text
#             except Exception as e:
#                 response = "Sorry developer, check your Google API Key or network. 😭"
            
#             st.write(response)
            
#     # حفظ رد يومي في الذاكرة
#     st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st
from google import genai
from google.genai import types


# =========================================================
# 1. إعداد الصفحة
# =========================================================

st.set_page_config(
    page_title="Yomi AI",
    page_icon="💬",
    layout="centered"
)


# =========================================================
# 2. التصميم
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0f020f;
}

h1 {
    color: #d633d6 !important;
    text-align: center;
}

.stChatMessage {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. الاتصال بـ Gemini
# =========================================================

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

except Exception:
    st.error(
        "❌ لم يتم العثور على GEMINI_API_KEY في Streamlit Secrets."
    )
    st.stop()


# =========================================================
# 4. معلومات Yomi
# =========================================================

st.title("YOMI AI v1.0")

st.markdown(
    "<p style='text-align:center; color:#bbb;'>"
    "Powered by Google Gemini - Mapped to Yousif!"
    "</p>",
    unsafe_allow_html=True
)


# =========================================================
# 5. ذاكرة المحادثة
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi developer! I am Yomi, your smart AI "
                "powered by Google. Ask me any programming "
                "or school question! 😊"
            )
        }
    ]


# =========================================================
# 6. عرض المحادثة
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# =========================================================
# 7. استقبال رسالة المستخدم
# =========================================================

if user_input := st.chat_input("Ask Yomi something..."):

    # عرض رسالة المستخدم
    with st.chat_message("user"):
        st.write(user_input)

    # حفظ رسالة المستخدم
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # =====================================================
    # 8. إرسال المحادثة كاملة إلى Gemini
    # =====================================================

    with st.chat_message("assistant"):

        with st.spinner("Yomi is thinking... 🧠"):

            try:

                # تعليمات Yomi
                system_instruction = """
You are Yomi, a smart and friendly AI assistant created
by a developer named Yousif.

Your job is to help with:
- Programming
- Python
- C#
- HTML
- CSS
- JavaScript
- Godot
- Unity
- Game development
- School questions
- General questions
- Anything else the user asks

Always be helpful, respectful and friendly.

When talking to Yousif, you can acknowledge that he is
the developer who created Yomi, but do not repeat this
in every single response.

Answer in the same language the user uses whenever possible.

For programming problems:
- Explain clearly.
- Give working code when needed.
- Do not unnecessarily change unrelated code.
- If the user asks for a complete function or script,
  provide the complete requested code.

Do not claim to have abilities or information that you
do not actually have.
"""


                # إنشاء محتوى المحادثة السابقة
                conversation = []

                for message in st.session_state.messages:

                    # لا نرسل رسالة الترحيب الافتراضية
                    if (
                        message["role"] == "assistant"
                        and message["content"].startswith(
                            "Hi developer! I am Yomi"
                        )
                    ):
                        continue

                    role = (
                        "user"
                        if message["role"] == "user"
                        else "model"
                    )

                    conversation.append(
                        types.Content(
                            role=role,
                            parts=[
                                types.Part(
                                    text=message["content"]
                                )
                            ]
                        )
                    )


                # =================================================
                # 9. إرسال الطلب إلى Gemini
                # =================================================

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=conversation,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                        max_output_tokens=2048
                    )
                )


                # استخراج النص
                answer = response.text


            except Exception as e:

                answer = (
                    "❌ حدث خطأ أثناء الاتصال بـ Gemini.\n\n"
                    f"تفاصيل الخطأ:\n`{str(e)}`"
                )


            # عرض الرد
            st.write(answer)


    # =====================================================
    # 10. حفظ رد Yomi
    # =====================================================

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
