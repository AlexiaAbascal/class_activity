import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import av

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Get image dimensions
        height, width, _ = img.shape

        # Define square size and position (centered)
        square_size = min(height, width) // 3
        top_left = (width // 2 - square_size // 2, height // 2 - square_size // 2)
        bottom_right = (top_left[0] + square_size, top_left[1] + square_size)

        # Draw rectangle (green)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        return img

st.title("📷 Live Camera with Center Square Overlay")
st.caption("Accessible from phone. You will see yourself with a square in the center.")

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
