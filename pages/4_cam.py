import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Draw center square
        h, w, _ = img.shape
        square_size = min(h, w) // 3
        top_left = (w // 2 - square_size // 2, h // 2 - square_size // 2)
        bottom_right = (top_left[0] + square_size, top_left[1] + square_size)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        return img

st.title("📷 Live Camera with Center Square Overlay")
st.caption("Accessible from mobile. Streamed through browser.")

webrtc_streamer(key="live", video_transformer_factory=VideoTransformer)
