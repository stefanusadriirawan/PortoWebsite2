import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
        menu_title="Menu",
        options=["Home", "About", "Skills", "Projects", "Contact"],
        icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],

)

if selected == "Home":
    st.write("Home")
elif selected == "About":
    st.write("About")
elif selected == "Skills":
    st.write("Skills")
elif selected == "Projects":
    st.write("Projects")
elif selected == "Contact":
    st.write("Contact")


# options=["Home", "About", "Skills", "Projects", "Contact"],
# icons=["house", "person-circle", "code-slash", "person-workspace", "telephone"],

# navbar home -----------------------------------------------------------------------------
def home():
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


# navbar about -----------------------------------------------------------------------------
def about():
    st.title("About Page")
    st.write("This is my portfolio website. I'm a Python developer and love creating cool things with Streamlit!")

# navbar skills -----------------------------------------------------------------------------
def skills():
# Adding a section for skills
    st.header("Skills")
    st.write("""
    - Python
    - Flask
    - Django
    - React
    - HTML/CSS
    """)
# navbar projects -----------------------------------------------------------------------------
def projects():
  # Adding a section for projects
    st.header("Projects")
    st.write("""
    - [Project 1](https://github.com/project1)
    - [Project 2](https://github.com/project2)
    - [Project 3](https://github.com/project3)
    """)

# navbar contact -----------------------------------------------------------------------------
def contact():
   # Adding a section for contact information
    st.header("Contact")
    st.write("""
    - Email: john.doe@email.com
    - Phone: +1-123-456-7890
    - LinkedIn: 
    """)

    image_url = 'github.png'
    link_url = 'https://github.com/stefanusadriirawan'

    # Display the image
    st.image(image_url, use_column_width=True)

    # Add a hyperlink to the image
    st.markdown(f'<a href="{link_url}">Click here to go to the website</a>', unsafe_allow_html=True)
# lem pemersatu -----------------------------------------------------------------------------



with st.container():
    with st.expander("Main Menu"):
        home_button = st.button("Home", key="home")
        about_button = st.button("About", key="about")
        skills_button = st.button("Skills", key="skills")
        projects_button = st.button("Projects", key="projects")
        contact_button = st.button("Contact", key="contact")

# Get the current query parameters
params = st.experimental_get_query_params()


# Check if the page parameter is not set or set to "home"
if "page" not in params:
    home_button = True
else:
    home_button = False

if home_button:
    st.experimental_set_query_params(page="home")
    home()
elif about_button:
    st.experimental_set_query_params(page="about")
    about()
elif skills_button:
    st.experimental_set_query_params(page="skills")
    skills()
elif projects_button:
    st.experimental_set_query_params(page="projects")
    projects()
elif contact_button:
    st.experimental_set_query_params(page="contact")
    contact()
else:
    st.experimental_set_query_params(page="home")
    home()



