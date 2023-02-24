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
        I am  a Data Analyst with expertise in logical and critical thinking, Python programming, SQL, Excel, AppScript, Google Sheets, and Tableau. I am interested in the fields of Data Analysis, Data Science, AI/ML Engineering, and Automation.
        """)
    st.write("---")
    st.header("Services")
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.image("1.png", width=120)
        st.subheader("Data Preparation")
        st.write("Performs data cleaning and transformation by identifying and correcting inaccuracies, inconsistencies, and errors in datasets, and converting raw data into a usable and understandable format.")
    with col2:
        st.image("2.png", width=120)
        st.subheader("Data Analysis")
        st.write("Provides data analysis services by using statistical methods to explore and draw insights from data, as well as developing predictive models to forecast future outcomes based on historical data.")
    with col3:
        st.image("3.png", width=120)
        st.subheader("Data Visualization")
        st.write("Offers data visualization services by creating visual representations of data, such as charts, graphs, and dashboards, as well as developing interactive and informative dashboards that provide a high-level view of key metrics and KPIs.")
    with col4:
        st.image("4.png", width=120)
        st.subheader("Data-Driven Solutions")
        st.write("Delivers data-driven solutions by developing and implementing business intelligence solutions based on data analysis and insights, as well as providing decision support to stakeholders by presenting data in a meaningful and actionable way.")



    st.write("---")
    st.header("Areas Of Interest")
    st.markdown("""
    <p>
        I have a strong interest in the field of <b>Data Science</b> and is continuously learning about new technologies and tools to improve my skills. I am also knowledgeable in <b>AI/ML Engineering</b>, which allows me to develop data-driven models and algorithms to solve complex business problems.
    </p>
    """, unsafe_allow_html=True)
    st.write("---")
    st.header("Skills Expertise")
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Skills:")
        st.write("Logical and critical thinking")
        st.progress(95)
        st.write("Analyzing data and extracting meaningful insights")
        st.progress(80)
        st.write("Python programming")
        st.progress(85)
        st.write("SQL")
        st.progress(80)
        st.write("Working with large datasets")
        st.progress(87)
        st.write("Performing complex data analysis tasks")
        st.progress(91)
        st.write("Data visualization")
        st.progress(85)
        st.write("Reporting")
        st.progress(100)
    with col2:
        st.subheader("Tools:")
        st.write("Excel")
        st.progress(95)
        st.write("AppScript")
        st.progress(87)
        st.write("Google Sheets")
        st.progress(91)
        st.write("Tableau")
        st.progress(85)
        st.write("PyCharm")
        st.progress(100)
        st.write("Jupyter Notebook")
        st.progress(85)
        st.write("VBA")
        st.progress(80)

    st.write("---")
    st.header("Course experience")
    st.error("Python programming for data science involves using Python as a tool for data manipulation, analysis, and visualization, typically using libraries such as NumPy, Pandas, Matplotlib, and Seaborn.")
    st.error("Data science course using SQL could involve analyzing customer behavior and purchasing patterns using transactional data from an e-commerce website.")
    st.error("Data science course using Machine Learning could involve developing a recommendation engine for a video streaming platform using collaborative filtering algorithms.")
    st.error("A real world case of a data science project using Data Visualization could involve creating an interactive dashboard to track and analyze the performance of marketing campaigns across different channels.")
    st.write("---")
    st.header("Project experience")
    st.error("Data science project using Predictive modeling could involve building a fraud detection model using supervised learning algorithms to identify and prevent fraudulent transactions in a financial institution.")
    st.error("Data science project using Data analysis could involve exploring and analyzing customer reviews and ratings of a product to identify trends, patterns, and areas for improvement.")
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
