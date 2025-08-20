import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import io
from PIL import Image

st.set_page_config(page_title="SmartVision CARLA - YOLOv8", layout="centered")
st.title("SmartVision CARLA - YOLOv8 Demo")

model = YOLO("best.pt")

uploaded_file = st.file_uploader("Upload the image.", type=["jpg", "png"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    results = model(img)
    annotated_img = results[0].plot()
    st.image(annotated_img, caption="Diagnosis result", use_column_width=True)


    st.subheader("Diagnosis details:")
    for box in results[0].boxes:
        cls_id = int(box.cls)
        cls_name = results[0].names[cls_id]
        conf = box.conf.item()
        st.write(f"🔹Class: {cls_name} — Trust: {conf:.2f}")

    image_pil = Image.fromarray(annotated_img)
    buf = io.BytesIO()
    image_pil.save(buf, format="PNG")
    st.download_button("📥 Download output image", buf.getvalue(), file_name="output.png", mime="image/png")