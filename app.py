import requests
import streamlit as st

# رابط نقطة النهاية (API Endpoint) الخاص بك من Ultralytics HUB
API_URL = "https://predict-6ab6dea323cca3b85a97a905-dproatj77a-no.a.run.app"

st.title("🚗 تطبيق عد السيارات بالذكاء الاصطناعي")
st.write(
    "قم برفع صورة أو فيديو لتحليله ومعرفة عدد السيارات الموجودة باستخدام نموذجك المنشور!"
)

# زر لرفع الملف
uploaded_file = st.file_uploader(
    "اختر صورة أو فيديو...", type=["jpg", "jpeg", "png", "mp4"]
)

if uploaded_file is not None:
  if uploaded_file.type.startswith("image"):
    st.image(
        uploaded_file, caption="الصورة المرفوعة", use_container_width=True
    )
  else:
    st.video(uploaded_file)

  if st.button("بدء التحليل والحساب"):
    with st.spinner("جاري إرسال الملف للنموذج وتحليل النتائج..."):
      try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
          result = response.json()
          st.success("تم التحليل بنجاح!")
          st.json(result)
        else:
          st.error(f"حدث خطأ في الاتصال بالـ API. الرمز: {response.status_code}")

      except Exception as e:
        st.error(f"حدث خطأ غير متوقع: {e}")
          
