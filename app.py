import streamlit as st
from moviepy.editor import *
from yt_dlp import YoutubeDL

st.title('Youtube to Mp3')

URL = st.text_input('YouTube Url')

if st.button('Download Audio'):

    with st.spinner("Please wait..."):

        video_info = YoutubeDL().extract_info(url=URL, download=False)
        audio_downloader = YoutubeDL({'format': 'mp4'})
        filename_video = f"{video_info['title']} [{video_info['id']}].mp4"
        filename_audio = f"{video_info['title']}.mp3"

        audio_downloader.extract_info(URL)

        video = VideoFileClip(filename_video)

        video.audio.write_audiofile(filename_audio)

        st.success(filename_audio)

        with open(filename_audio, "rb") as file:
            btn = st.download_button(
                label="Download",
                data=file,
                file_name=filename_audio,
                mime="mp3"
            )