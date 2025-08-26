import os #Standard libaries
import streamlit as st #alise
from dotenv import load_dotenv
load_dotenv()
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


prompt = """You are Youtube video summarizer. You will be taking the transcript text and summarizing the 
entire video and providing the important summary in points within 250 words. Your task is to provide a 
succinct summary of the transcript text extracted from a YouTube video.

**Title:** [Title of the YouTube Video]
**Transcript Text:** [Please provide the summary of the text given here:]

**Instructions:**
1. Carefully read through the transcript text to understand the main ideas and topics discussed in the video.
2. Summarize the content by highlighting the most significant points, key takeaways, and noteworthy information.
3. Focus on clarity, conciseness, and relevance in your summary. Ensure that your summary captures the essence of the video content.
4. Aim for a well-structured summary that is easy to follow and provides value to the reader.

**Summary:** [Your summary of the YouTube video content will be provided here.]

Feel free to use bullet points or paragraphs to organize your summary effectively.
Ready to summarize? Let's get started!
"""

# extract transcript details from a YouTube video URL
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        print(video_id)

        ytt_api = YouTubeTranscriptApi()
        transcript_data = ytt_api.fetch(video_id)

        transcript = ""
        for snippet in transcript_data:
            transcript += " " + snippet.text
        return transcript.strip()

    except TranscriptsDisabled:
        st.error("Subtitles are disabled for this video.")
        st.stop()

    except Exception as e:
        raise e


# generate detailed content using Google's Gemini model based on provided transcript text and a prompt.
def generate_gemini_content(transcript_text, prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt + transcript_text
    )
    return response.text


# Streamlit interface
header = """
<div style="background-color: #EDF3FA; padding: 2px; text-align: center;">
    <h1 style="color: #333;">YouTube Video Transcript Summarizer</h1>
</div>
"""
st.markdown(header, unsafe_allow_html=True)

# Content
youtube_link = st.text_input("Enter YouTube Video Link:")
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

# Footer
footer = """
<div style="position: fixed; bottom: 0; width: 100%; background-color: #EDF3FA; padding: 10px; text-align: center;">
      Created with ❤️ by Tayyab Shoukat
</div>
"""
st.markdown(footer, unsafe_allow_html=True)