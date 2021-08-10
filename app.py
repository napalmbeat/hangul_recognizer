import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, ocr, word # import your app modules here
from PIL import Image
import tensorflow as tf
import streamlit.components.v1 as components



physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

app = MultiApp()

image = Image.open('logo.png')
st.image(image, width=700)


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Hangul syllable recognizer 초기형", ocr.app)
app.add_app("Hangul syllable recognizer 완성형", model.app)
app.add_app("Hangul word recognizer", word.app)
#app.add_app("Hangul recognizer in image", data.app)


# The main app
app.run()
