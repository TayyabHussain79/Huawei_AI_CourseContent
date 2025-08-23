import streamlit as st
from backend import roman_to_pashto

st.set_page_config(page_title="Roman Pashto to Native Pashto Converter", layout="centered")

st.image("pashto.jpg", use_container_width=True)

st.title("📝 Roman Pashto --> Native Pashto Converter")

# User input
roman_text = st.text_area("Enter Roman Pashto text:", placeholder="Sanga ye?")

if st.button("Convert"):
    if roman_text.strip():
        with st.spinner("Converting... Sirf Tamasha Kawa Janana 😜"):
            pashto_text = roman_to_pashto(roman_text)
        st.success("✅ Converted Text:")
        
        st.code(pashto_text, language="pashto")
    else:
        st.warning("⚠️ Please enter some text to convert.")

st.markdown("Built with **Google Generative AI + Streamlit** by Tayyab Shoukat")