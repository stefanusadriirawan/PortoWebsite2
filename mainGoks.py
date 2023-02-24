import streamlit as st
from streamlit_option_menu import option_menu

# options=["Home", "About", "Skills", "Projects", "Contact"],
# icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],

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


    button_clicked = False

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
    
    <button class="button" type="submit">Github</button>
       """
    button_githuasdb = """
           <button onclick="window.location.href='https://github.com/stefanusadriirawan'" style="background-color: #333333; border-radius: 4px; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin-right: 10px;">Github</button>
       """

    button_medium = """
           <button onclick="window.location.href='https://medium.com/@stefanusadriirawan'" style="background-color: #00ab6c; border-radius: 4px; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin-right: 10px;">Medium</button>
       """

    button_linkedin = """
           <button onclick="window.location.href='https://www.linkedin.com/in/stefanus-adri-irawan-5753801b1'" style="background-color: #0077B5; border-radius: 4px; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin-right: 10px;">LinkedIn</button>
       """

    button_youtube = """
           <button onclick="window.location.href='https://www.youtube.com/channel/UC1_vrHzpugdLgZEsjmOUZbQ'" style="background-color: #FF0000; border-radius: 4px; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin-right: 10px;">Youtube</button>
       """

    button_tiktok = """
           <button onclick="window.location.href='https://www.tiktok.com/@stefanusadriirawan'" style="background-color: #000000; border-radius: 4px; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin-right: 10px;">TikTok</button>
       """




    if button_clicked:
        st.write("Button clicked!")

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
