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


# lem pemersatu -----------------------------------------------------------------------------

selected = option_menu(
        menu_title="Menu",
        options=["About", "Skills", "Projects", "Contact"],
        icons=["person-circle", "code-slash", "person-workspace", "telephone"],
        menu_icon="cast",
        orientation="horizontal",
)

if selected == "About":
    about()
elif selected == "Skills":
    skills()
elif selected == "Projects":
    projects()
elif selected == "Contact":
    contact()
else:
    pass
