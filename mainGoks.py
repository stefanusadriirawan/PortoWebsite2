import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser

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

def open_link(url):
    webbrowser.open_new_tab(url)


def contact():
   # Adding a section for contact information
    st.header("Contact")
    st.write("""
    - Email: john.doe@email.com
    - Phone: +1-123-456-7890
    - LinkedIn: 
    """)

    #st.markdown(github, unsafe_allow_html=True)


    github = 'https://github.com/stefanusadriirawan'
    medium = 'https://medium.com/@stefanusadriirawan'
    linked_in = 'https://www.linkedin.com/in/stefanus-adri-irawan-5753801b1/'
    youtube = 'https://www.youtube.com/channel/UC1_vrHzpugdLgZEsjmOUZbQ'
    tiktok = 'https://www.tiktok.com/@stefanusadriirawan'

    urls = [github, medium, linked_in, youtube, tiktok]

    selected2 = option_menu(
            menu_title="Social media",
            options=["Github", "Medium", "Linked in", "Youtube", "TikTok"],
            icons=["github", "medium", "linkedin", "youtube", "tiktok"],
            menu_icon="cast",
            orientation="vertical",
    )


    if selected2 == "Github":
        open_link(urls[0])
    elif selected2 == "Medium":
        open_link(urls[1])
    elif selected2 == "Linked in":
        open_link(urls[2])
    elif selected2 == "Youtube":
        open_link(urls[3])
    elif selected2 == "TikTok":
        open_link(urls[4])
    else:
        pass


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
