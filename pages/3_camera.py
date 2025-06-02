import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
import cv2

# Optional: your OpenCV logic here
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

st.title("Camera Access Page")

if "camera_on" not in st.session_state:
    st.session_state["camera_on"] = False

if st.button("Start Camera"):
    st.session_state["camera_on"] = True

if st.button("Stop Camera"):
    st.session_state["camera_on"] = False

if st.session_state["camera_on"]:
    webrtc_streamer(
        key="camera",
        mode=WebRtcMode.SENDRECV,
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": True, "audio": False},
    )
else:
    st.info("Camera is off. Click 'Start Camera' to begin.")
