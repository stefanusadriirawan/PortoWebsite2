import streamlit as st
from streamlit_option_menu import option_menu
from flask import Flask, request, jsonify
from PIL import Image

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
        Stefanus Adri Irawan is a Data Analyst with expertise in logical and critical thinking, Python programming, SQL, Excel, AppScript, Google Sheets, and Tableau. He is interested in the fields of Data Analysis, Data Science, AI/ML Engineering, and Automation.
        """)
    st.write("---")
    st.subheader("Services")
    st.write("""
            As a Data Analyst, Stefanus provides services such as data cleaning, transformation, analysis, and visualization. He also develops and implements data-driven solutions to improve business performance and decision-making processes.
            """)
    st.write("---")
    st.subheader("Areas Of Interest")
    st.write("""
            Stefanus has a strong interest in the field of Data Science and is continuously learning about new technologies and tools to improve his skills. He is also knowledgeable in AI/ML Engineering, which allows him to develop data-driven models and algorithms to solve complex business problems.
            """)
    st.write("---")
    st.subheader("Skills Expertise")
    st.write("""
            Stefanus is highly skilled in logical and critical thinking, which enables him to analyze data and extract meaningful insights. He is also proficient in Python programming and SQL, which allows him to work with large datasets and perform complex data analysis tasks. Additionally, he is experienced in using Excel, AppScript, Google Sheets, and Tableau for data visualization and reporting.
            """)
    st.write("---")
    st.subheader("Course experience")
    st.write("""
            Stefanus has completed several courses related to Data Analysis and Data Science, including courses in Python programming, SQL, Machine Learning, and Data Visualization. He also has hands-on experience working on various projects, including predictive modeling, data visualization, and data analysis.
            """)
    st.write("---")


# navbar projects -----------------------------------------------------------------------------
def project():
  # Adding a section for projects
    st.header("Project")
    st.markdown("""
    <br>
    <br>
    
    """, unsafe_allow_html=True)
    # List of image URLs
  # Define the images you want to display


    images = [
        ('Deteksi asam lambung', '1.png', 'https://www.linkedin.com/in/stefanus-adri-irawan-5753801b1/'),
        ('Potong usus jadi sate', '2.png', 'https://github.com/stefanusadriirawan'),
        ('Mamen', '3.png', 'https://www.tiktok.com/@stefanusadriirawan'),
        ('UHheuehe', '4.png', 'https://www.youtube.com/channel/UC1_vrHzpugdLgZEsjmOUZbQ'),
        ('Mulut anjai', '5.png', 'https://medium.com/@stefanusadriirawan'),
        ('Kek jamur gatau', '6.png', 'https://www.flaticon.com/packs/digestive-system-4'),
    ]

    # Display the images in a gallery
    col1, col2, col3 = st.columns(3)
    for i, image in enumerate(images):
        with eval(f"col{i % 3 + 1}"):
            img = Image.open(image[1])
            st.image(img, caption=image[0], use_column_width=True)

            # Add a button or link to make the image clickable
            st.markdown(f"""
                    <style>
                            .button{i+1} {{
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
                                width: 210px;
                            }}
    
                            .button{i+1}:hover {{
                                background-color: #47527a;
                                transition: 0.5s ease-out;
                            }}
                            .button{i+1}:not(:hover) {{
                                background-color: #fa4c4c;
                                transition: background-color 0.15s ease-in;
                            }}
                    </style>
                    <a href="{image[2]}" target="_blank">
                        <button class="button{i+1}">Go to project no. {i+1}</button>
                    </a>
                    <br>
                    <br>
                    <br>
                    <br>
                       """, unsafe_allow_html=True)


# navbar contact -----------------------------------------------------------------------------



def contact():
    # Adding a section for contact information

    button_email = """
    
            <style>
              h2 {
                font-size: 60px;
                font-weight: bold;
              }
              
              h1 {
                font-size: 36px;
              }
              
              p {
                font-size: 20px;
              }     
            </style>
            <h2>
                Reach me out!
            </h2>
                
            <h1>
                We can have a nice conversation, here is my email and social media account:
            </h1>
           
            
            <p>
               stefanusadriirawan@gmail.com
            </p>
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
