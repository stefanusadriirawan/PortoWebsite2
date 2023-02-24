import streamlit as st
from streamlit_option_menu import option_menu

github = '''
           <style>
                .button-wrapper {
                    display: flex;
                    flex-direction: row;
                    justify-content: center;
                    align-items: center;
                    width: 100px;
                    height: 50px;
                    border-radius: 10px;
                    background-color: #FFFFFF;
                    box-shadow: 0px 0px 10px #888888;
                    cursor: pointer;
                    transition: background-color 0.5s ease;
                }
                .button-wrapper:hover {
                    background-color: #87CEFA;
                }
                .button-text {
                    margin-left: 3px;
                    font-size: 20px;
                    font-weight: bold;
                    color: #000000;
                }
            </style>
            <a href="https://github.com/stefanusadriirawan" style="text-decoration:none;">
                <div class="button-wrapper">
                    <span class="button-text">Github</span>
                </div>
            </a>
        '''
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
    st.header("Contact")
    st.write("""
    - Email: john.doe@email.com
    - Phone: +1-123-456-7890
    - LinkedIn: 
    """)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.markdown(github, unsafe_allow_html=True)
    with col2:
        st.markdown(github, unsafe_allow_html=True)
    with col3:
        st.markdown(github, unsafe_allow_html=True)
    with col4:
        st.markdown(github, unsafe_allow_html=True)
    with col5:
        st.markdown(github, unsafe_allow_html=True)






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
