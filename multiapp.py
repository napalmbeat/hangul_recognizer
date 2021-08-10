"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import codecs
import streamlit.components.v1 as components

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def st_calculator(calc_html, width=700, height=500):
        calc_file = codecs.open(calc_html, 'r')
        page = calc_file.read()
        components.html(page, width=width, height=height, scrolling=False)

    def run(self):
        import streamlit.components.v1 as components
        # bootstrap 4 collapse example

        html_str = """
        <style>
body {
  background-color: #222222;
  background: repeating-linear-gradient(
      45deg,
      #2b2b2b 0%,
      #2b2b2b 10%,
      #222222 0%,
      #222222 50%
    )
    0 / 15px 15px;
}

#container {
  width: 500px;
  margin: auto;
}

/*Neon*/
p {
  text-align: center;
  font-size: 2em;
  margin: 20px 0 20px 0;
}

a {
  text-decoration: none;
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;
  transition: all 0.5s;
}

p:nth-child(1) a {
  color: #fff;
  font-family: Monoton;
  -webkit-animation: neon1 1.5s ease-in-out infinite alternate;
  -moz-animation: neon1 1.5s ease-in-out infinite alternate;
  animation: neon1 1.5s ease-in-out infinite alternate;
}

p:nth-child(1) a:hover {
  color: #ff1177;
  -webkit-animation: none;
  -moz-animation: none;
  animation: none;
}

p:nth-child(6) a:hover {
  -webkit-animation: neon6 1.5s ease-in-out infinite alternate;
  -moz-animation: neon6 1.5s ease-in-out infinite alternate;
  animation: neon6 1.5s ease-in-out infinite alternate;
}

p a:hover {
  color: #ffffff;
}
/*glow for webkit*/

@-webkit-keyframes neon1 {
  from {
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #ff1177,
      0 0 70px #ff1177, 0 0 80px #ff1177, 0 0 100px #ff1177, 0 0 150px #ff1177;
  }
  to {
    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #ff1177,
      0 0 35px #ff1177, 0 0 40px #ff1177, 0 0 50px #ff1177, 0 0 75px #ff1177;
  }
}
/*glow for mozilla*/

@-moz-keyframes neon1 {
  from {
    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #ff1177,
      0 0 35.5px #ff1177, 0 0 40px #ff1177, 0 0 50px #ff1177, 0 0 75px #ff1177;
  }
  to {
    text-shadow: 0 0 2.5px #fff, 0 0 5px #fff, 0 0 7.5px #fff, 0 0 10px #ff1177,
      0 0 17.5px #ff1177, 0 0 20px #ff1177, 0 0 25px #ff1177, 0 0 37.5px #ff1177;
  }
}
/*glow*/

@keyframes neon1 {
  from {
    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #ff1177,
      0 0 35px #ff1177, 0 0 40px #ff1177, 0 0 50px #ff1177, 0 0 75px #ff1177;
  }
  to {
    text-shadow: 0 0 2.5px #fff, 0 0 5px #fff, 0 0 7.5px #fff, 0 0 10px #ff1177,
      0 0 17.5px #ff1177, 0 0 20px #ff1177, 0 0 25px #ff1177, 0 0 37.5px #ff1177;
  }
}
/*REEEEEEEEEEESPONSIVE*/

@media (max-width: 650px) {
  #container {
    width: 100%;
  }
  p {
    font-size: 3.5em;
  }
}
</style>
<div id="container">

  <p><a>
      This app<br>visualizes poor handwriting recognition and results
    </a></p>
</div>
        """
        components.html(html_str,height=200)

        #st.markdown(html_str, unsafe_allow_html=True)
        # app = st.sidebar.radio(


        app = st.selectbox(
            ' 👇Navigation 👇',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()