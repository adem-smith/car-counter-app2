import numpy as np
from PIL import Image
import streamlit as st
from ultralytics import YOLO

st.title("🚗 تطبيق عد السيارات بالذكاء الاصطناعي")
st.write(
    "قم برفع صورة أو فيديو لتحليله ومعرفة عدد السيارات الموجودة باستخدام نموذجك!"
)


@st.cache_resource
def load_model():
  model = YOLO("best.pt")
  return model


try:
  model = load_model()
except Exception as e:
  st.warning(
      "ملاحظة: لم يتم العثور على ملف الموديل 'best.pt' بعد في المستودع. تأكد"
      " من رفع ملف الـ .pt مع الملفات."
  )

uploaded_file = st.file_uploader(
    "اختر صورة أو فيديو...", type=["jpg", "jpeg", "png", "mp4"]
)

if uploaded_file is not None:
  if uploaded_file.type.startswith("image"):
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="الصورة المرفوعة", use_container_width=True)

    if st.button("بدء التحليل والحساب"):
      with st.spinner("جاري تحليل الصورة بالذكاء الاصطناعي..."):
        results = model(image)
        res_plotted = results[0].plot()  # مصفوفة الألوان من ألترايليتكس

        # تحويل النتائج إلى صورة PIL لعرضها مباشرة بدون cv2
        res_image = Image.fromarray(res_plotted[..., ::-1])

        car_count = len(results[0].boxes)

        st.success(f"تم التحليل بنجاح! عدد السيارات المكتشفة: {car_count}")
        st.image(
            res_image,
            caption="الصورة بعد التحليل والتحديد",
            use_container_width=True,
        )

  else:
    st.video(uploaded_file)
      
