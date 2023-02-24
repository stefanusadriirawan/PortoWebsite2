import streamlit as st
from streamlit_option_menu import option_menu
from flask import Flask, request, jsonify

app = Flask(__name__)

def my_python_function(data):
    # process the data and return a result
    return {'message': 'Hello, {}!'.format(data['name'])}


@app.route('/my-route', methods=['POST'])
def my_route():
    # handle request data
    data = request.get_json()

    # call Python functions
    result = my_python_function(data)

    # return response data
    return jsonify(result)


# navbar home -----------------------------------------------------------------------------
def about():
    # Defining the layout
    col1, col2 = st.columns(2)
    with col1:
        st.image("Potrait_photo.png", use_column_width=True)
    with col2:
        st.title("Stefanus Adri Irawan")
        st.subheader("Data Analyst")
        st.write("""
        I am an experienced web developer with expertise in Python, Flask, Django, and React. 
        I have worked on several projects for clients from various industries, including healthcare, finance, and e-commerce. 
        In my free time, I like to contribute to open-source projects and learn new technologies. 
        """)
    st.write("---")
    st.subheader("Services")
    st.write("""
            My expertise can be used to clean, analyse, interpret and visualize your data.
            """)
    st.write("---")
    st.subheader("Areas Of Interest")
    st.write("""
            Take a look at some of the things I love working on.
            """)
    st.write("---")
    st.subheader("Skills Expertise")
    st.write("""
            Blabla
            """)
    st.write("---")
    st.subheader("Course experience")
    st.write("""
            Blabla
            """)
    st.write("---")


# navbar projects -----------------------------------------------------------------------------
def project():
  # Adding a section for projects
    st.header("Project")
    st.write("""
    - [Project 1](https://github.com/project1)
    - [Project 2](https://github.com/project2)
    - [Project 3](https://github.com/project3)
    """)

# navbar contact -----------------------------------------------------------------------------



def contact():
    # Adding a section for contact information
    st.header("Reach me out!")

    button_email = """
    <style>
        #email-form {
            max-width: 600px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin-bottom: 8px;
            margin-left: -50px;
        }
        input[type="email"],
        input[type="text"],
        textarea {
            display: block;
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-bottom: 16px;
            margin-left: -50px;
            font-size: 16px;
        }
        button[type="submit"] {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 200px;
            margin-left: -50px;
        }
        button[type="submit"]:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        button[type="submit"]:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    
    <form id="email-form" action="/send-email.php" method="POST">
        <label for="email">Email address:</label> 
        <input type="email" id="email" name="email" required>
        <label for="subject">Subject:</label> 
        <input type="text" id="subject" name="subject" required>
        <label for="message">Message:</label> 
        <textarea id="message" name="message" required></textarea> 
        <button type="submit">Send Email</button>
    </form>

    
           """
    button_whatsapp = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 200px;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://wa.me/6281310803571" target="_blank">
        <button class="button">Whatsapp me</button>
    </a>
       """
    button_github = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://github.com/stefanusadriirawan" target="_blank">
        <button class="button">GitHub</button>
    </a>
       """
    button_medium = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://medium.com/@stefanusadriirawan" target="_blank">
        <button class="button">Medium</button>
    </a>
       """

    button_linkedin = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://www.linkedin.com/in/stefanus-adri-irawan-5753801b1" target="_blank">
        <button class="button">LinkedIn</button>
    </a>
       """

    button_youtube = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://www.youtube.com/channel/UC1_vrHzpugdLgZEsjmOUZbQ" target="_blank">
        <button class="button">YouTube</button>
    </a>
       """

    button_tiktok = """
    <style>
        .button {
            background-color: #fa4c4c;
            border: none;
            border-radius: 25px;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    
        .button:hover {
            background-color: #47527a;
            transition: 0.5s ease-out;
        }
        .button:not(:hover) {
            background-color: #fa4c4c;
            transition: background-color 0.15s ease-in;
        }
    </style>
    <a href="https://www.tiktok.com/@stefanusadriirawan" target="_blank">
        <button class="button">TikTok</button>
    </a>
       """

    st.markdown(button_email, unsafe_allow_html=True)
    st.markdown(button_whatsapp, unsafe_allow_html=True)
    st.markdown(button_github, unsafe_allow_html=True)
    st.markdown(button_medium, unsafe_allow_html=True)
    st.markdown(button_linkedin, unsafe_allow_html=True)
    st.markdown(button_youtube, unsafe_allow_html=True)
    st.markdown(button_tiktok, unsafe_allow_html=True)

# lem pemersatu -----------------------------------------------------------------------------

selected = option_menu(
        menu_title=None,
        options=["About", "Project", "Contact"],
        icons=["person-circle", "person-workspace", "telephone"],
        menu_icon="cast",
        orientation="horizontal",
)

if selected == "About":
    about()
elif selected == "Project":
    project()
elif selected == "Contact":
    contact()
else:
    pass
