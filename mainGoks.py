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
    st.header("Get In Touch With Me!")
    contact_form= """
    <style>
    /* Style inputs with type="text", select elements and textareas */
    input[type=text], input[type=email], textarea {
      width: 100%; /* Full width */
      padding: 12px; /* Some padding */ 
      border: 1px solid #ccc; /* Gray border */
      border-radius: 4px; /* Rounded borders */
      box-sizing: border-box; /* Make sure that padding and width stays in place */
      margin-top: 6px; /* Add a top margin */
      margin-bottom: 16px; /* Bottom margin */
      resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
    }
    
    /* Style the submit button with a specific background color etc */
    button[type=submit] {
      background-color: #fa4c4c;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.5s; /* Add a transition effect with a duration of 0.5s */
    }
    
    /* When moving the mouse over the submit button, add a darker green color */
    button[type=submit]:hover {
      background-color: #47527a;
    }
    </style>

    <form action="https://formsubmit.co/stefanusadriirawan@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Insert Name"></textarea>
    <input type="email" name="email" placeholder="Insert Email"></textarea>
    <textarea name="message" placeholder="Details of your problem"></textarea>
    <button type="submit">Send</button>
    </form>
    <br>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Add a button to trigger the redirect


    if st.button("Whatsapp"):
        st.markdown('''
                          <meta http-equiv="refresh" content="0;url=https://wa.me/6281310803571">
                          ''', unsafe_allow_html=True)
    elif st.button("Github"):
        st.markdown('''
                           <meta http-equiv="refresh" content="0;url=https://github.com/stefanusadriirawan">
                           ''', unsafe_allow_html=True)
    elif st.button("Medium"):
        st.markdown('''
                               <meta http-equiv="refresh" content="0;url=https://medium.com/@stefanusadriirawan">
                               ''', unsafe_allow_html=True)
    elif st.button("Linked in"):
        st.markdown('''
                                   <meta http-equiv="refresh" content="0;url=https://www.linkedin.com/in/stefanus-adri-irawan-5753801b1">
                                   ''', unsafe_allow_html=True)
    elif st.button("Youtube"):
        st.markdown('''
                                   <meta http-equiv="refresh" content="0;url=https://www.youtube.com/channel/UC1_vrHzpugdLgZEsjmOUZbQ">
                                   ''', unsafe_allow_html=True)
    elif st.button("TikTok"):
        st.markdown('''
                                   <meta http-equiv="refresh" content="0;url=https://www.tiktok.com/@stefanusadriirawan">
                                   ''', unsafe_allow_html=True)
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
