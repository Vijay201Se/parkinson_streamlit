import streamlit as st
import numpy as np
import pandas as pd
import cv2
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_space import space
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="Parkinson Detector",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Parkinson's disease is a progressive neurological disorder affecting movement. Symptoms include "
                 "tremors, stiffness, and slowed movement. As it advances, it may cause difficulty with balance, "
                 "speech, and writing. Although the exact cause is unknown, it's associated with the loss of "
                 "dopamine-producing cells in the brain."
    }
)

def load_css(file_name = "C:\\Users\\Administrator\\Downloads\\streamlit code\\styles.css"):
    with open(file_name) as f:
        css = f'<style>{f.read()}</style>'
    return css
css = load_css()
st.markdown(css, unsafe_allow_html=True)

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="menu",  # required
                options=["Home", "Detection", "Recommendation", "Contact"],  # required
                icons=["house", "search", "star", "telephone"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Detection", "Recommendation", "Contact"],  # required
            icons=["house", "search", "star", "telephone"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="menu",  # required
                options=["Home", "Detection", "Recommendation", "Contact"],  # required
                icons=["house", "search", "star", "telephone"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 4:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Detection", "Recommendation", "Contact"],  # required
            icons=["house", "search", "star", "telephone"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa","width": "300px"},
                "icon": {"color": "orange", "font-size": "5px"},
                "nav-link": {
                    "font-size": "5px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)


def recommendation():
    st.title("⭐ Recommendation Information")
    space()
    tab1, tab2 = st.tabs(["Therapy", "Specialty Hospitals"])

    with tab1:
        with st.container():
            c1, _, c2 = st.columns([1.5, 0.1, 0.5])
            with c1:
                space()
                st.markdown(
            """<p style='font-size: 20px; text-align:justify'> Self-management is an important aspect of controlling Parkinson's disease. Here are four realistic 
            and relevant points detailing therapies and remedies that can be handled by individuals to help manage 
            Parkinson's disease: <br></p>

<p style='font-size: 19px; text-align:justify'> <span style='background-color: #3b5aa3; padding: 5px; border-radius: 50px;'>Regular Exercise:</span> Engaging in regular physical activity and exercise routines can significantly benefit individuals 
with Parkinson's disease. Activities such as walking, swimming, cycling, or yoga can help improve mobility, 
flexibility, and balance. Exercise has been shown to alleviate symptoms, enhance motor function, and contribute to 
overall well-being. Additionally, it may help in reducing the risk of falls and improving cardiovascular health. <br></p>

<p style='font-size: 19px; text-align:justify'><span style='background-color: #3b5aa3; padding: 5px; border-radius: 50px;'>Medication Adherence:</span> Adhering to the prescribed medication regimen is crucial for managing Parkinson's disease. 
Patients should ensure they take their medications at the right time and in the correct dosage as prescribed by their 
healthcare provider. Consistent adherence can help in controlling symptoms, maintaining stability, and mitigating 
fluctuations in motor function associated with the condition. <br></p>

<p style='font-size: 19px; text-align:justify'><span style='background-color: #3b5aa3; padding: 5px; border-radius: 50px;'>Nutritional Support:</span> A balanced and nutritious diet plays a vital role in supporting overall health for individuals 
with Parkinson's disease. Consuming a diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats 
can aid in managing symptoms and promoting well-being. Additionally, ensuring adequate hydration and moderating 
intake of certain substances, such as caffeine and alcohol, can help minimize potential adverse effects on symptoms. <br></p>

<p style='font-size: 19px; text-align:justify'><span style='background-color: #3b5aa3; padding: 5px; border-radius: 50px;'>Mind-Body Therapies:</span> Incorporating mind-body therapies such as meditation, mindfulness, and relaxation techniques can 
contribute to reducing stress and anxiety, which are commonly experienced by individuals with Parkinson's disease. 
These practices can help in promoting emotional well-being, enhancing mental clarity, and managing non-motor 
symptoms. Engaging in activities that foster a sense of calm and relaxation can have a positive impact on both 
physical and emotional health.</p> """,
                    unsafe_allow_html=True
                )
            with c2:
                st.image("recommendation.png", width=200)

    with tab2:
        # Define the data for the table
        data = [
            ["1", "All India Institute of Medical Sciences (AIIMS), New Delhi", "Ansari Nagar, New Delhi, Delhi 110029",
             "+91-11-2658 8500"],
            ["2", "Sree Chitra Tirunal Institute for Medical Sciences and Technology, Thiruvananthapuram",
             "Kowdiar, Thiruvananthapuram, Kerala 695011", "+91-471-2524 567"],
            ["3", "Nizam's Institute of Medical Sciences, Hyderabad", "Punjagutta, Hyderabad, Telangana 500082",
             "+91-40-2319 3000"],
            ["4", "Postgraduate Institute of Medical Education and Research, Chandigarh",
             "Sector 12, Chandigarh 160012", "+91-172-2744 285"],
            ["5", "National Institute of Mental Health and Neurosciences, Bengaluru",
             "Hosur Road, Bengaluru, Karnataka 560029", "+91-80-2699 5000"]
        ]

        st.title("Top Neurological Parkinson Specialist Hospitals in India")

        with st.container():
            c1, c2 = st.columns([0.075, 0.1])
            with c1:
                st.header("Ranked by the Indian Medical Council ")
            with c2:
                st.image("imc.png", width=70)

        # Create a custom CSS style for the table
        table_style = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap')
          .custom-table {
            width: 100%;
            border-collapse: collapse;
          }
          .custom-table th, .custom-table td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            padding: 20px;
          }
          .custom-table th {
            background-color: #3b5aa3;
            font-weight: bold;
          }
          .custom-table tr{
            transition: 0.5s;

          }
          .custom-table tr:hover {
            background-color: #3b5aa3;
            transition: 0.5s;
          }
          .custom-table .rank-column {
            width: 10%;
            text-align: center;
          }
          .custom-table .hospital-column {
            width: 40%;
          }
          .custom-table .address-column {
            width: 30%;
          }
          .custom-table .contact-column {
            width: 20%;
          }
        </style>
        """

        # Add the custom CSS style to the Streamlit app
        st.markdown(table_style, unsafe_allow_html=True)

        # Create the table
        st.write(
            f"""
            <table class="custom-table">
                <tr>
                    <th class="rank-column">Rank</th>
                    <th class="hospital-column">Hospital Name</th>
                    <th class="address-column">Address</th>
                    <th class="contact-column">Contact</th>
                </tr>
                {''.join([f'<tr><td class="rank-column">{row[0]}</td><td class="hospital-column">{row[1]}</td><td class="address-column">{row[2]}</td><td class="contact-column">{row[3]}</td></tr>' for row in data])}
            </table>
            """,
            unsafe_allow_html=True
        )


#introduction code
if selected == "Home":
    st.title("Introduction to Parkinson's Disease")
    space()
    space()
    # Display the resized image and introduction text
    about_container = st.container()
    with about_container:
        col1,_, col2 = st.columns([1.5,0.1, 0.5])
        with col1:
        #introduction to parkinson disease

         st.subheader("About Parkinson:")
         st.write(
            """
            <div style="text-align: justify; font-size: 18px;">
            Parkinson's disease is a neurodegenerative disorder affecting movement control, resulting from the loss of dopamine-producing cells in the brain. Common symptoms include tremors, rigidity, bradykinesia, and postural instability. While its precise cause remains elusive, both genetic predisposition and environmental factors are implicated. Diagnosis relies on medical history, neurological examination, and imaging tests. Treatment aims to alleviate symptoms and may involve medication, physical therapy, and deep brain stimulation. While incurable, management strategies can significantly enhance quality of life. Ongoing research endeavors seek to unravel novel therapies and elucidate the disease's underlying mechanisms.
            </div>
            """,
            unsafe_allow_html=True
         )
        with col2:
            st.image("parkinson.png", width=250)
        st.divider()

     #What causes Parkinson’s disease
    cause_container = st.container()
    with cause_container:
        col1, _, col2 = st.columns([1.5, 0.1, 0.5])
        with col1:
            st.subheader("What causes Parkinson’s disease:")
            st.write(
                """
               <div style="text-align: justify; font-size: 18px;">
                   ⭕ Parkinson's disease is primarily characterized by the impairment or death of nerve cells in the basal ganglia, leading to a decrease in dopamine production, which is responsible for movement issues associated with the disease.
                </div>
               <br>

               <div style="text-align: justify; font-size: 18px;">
                  ⭕ Loss of norepinephrine-producing nerve endings in individuals with Parkinson's disease can explain various non-movement symptoms, including fatigue, irregular blood pressure, digestive problems, and orthostatic hypotension.
               </div>
               <br>

               <div style="text-align: justify; font-size: 18px;">
                  ⭕ Parkinson's disease is linked to the presence of Lewy bodies containing the protein alpha-synuclein in the brain cells of affected individuals, with ongoing research focusing on understanding the role of alpha-synuclein, genetic factors, and environmental influences in the development of the disease.
               </div>
               """,
                unsafe_allow_html=True
            )
        with col2:
            with stylable_container(
                    key="cause_image",
                    css_styles=[
                        """
                            {
                                margin-top: 50px;
                            }
                        """
                    ]
            ):
                st.image("brain.png", width=250)
        space()
        st.divider()

    #symptoms


    symptom_container = st.container()
    with symptom_container:
        st.subheader("📢 Symptoms")
        space()
        # Display the resized image and introduction text
        col1, col2 = st.columns([1, 1])  # Adjust the ratio of widths as needed
        with col1:
            st.subheader("Motor")
            st.image("symptoms_motor.png", width=585)
        with col2:
            st.subheader("Non-Motor")
            st.image("symptoms_non_motor.png", width=600)
    space()
    space()
    st.divider()
    space()
    space()

    #Stages of Parkinson’s disease code
    st.subheader("📊 Stages of Parkinson’s disease:")
    st.write(
    """
    <div style="text-align: justify; font-size: 18px;">
        Parkinson’s disease can take years or even decades to cause severe effects. In 1967, two experts, Margaret Hoehn and Melvin Yahr, created the staging system for Parkinson’s disease. That staging system is no longer in widespread use because staging this condition is less helpful than determining how it affects each person’s life individually and then treating them accordingly.
    </div>
    <br>
    """,
    unsafe_allow_html=True
    )

    st.write(
    """
    <br>
      <ul>
        <li><span style="color: #F0F0F0; font-size: 20px;"><b>Part 1: Non-motor aspects of experiences of daily living.</b></span> <br>This section deals with non-motor (non-movement) symptoms like dementia, depression, anxiety and other mental ability- and mental health-related issues. It also asks questions about pain, constipation, incontinence, fatigue, etc.</li>
        <br>
        <li><span style="color: #F0F0F0; font-size: 20px;"><b>Part 2: Motor aspects of experiences of daily living.</b></span> <br>This section covers the effects on movement-related tasks and abilities. It includes your ability to speak, eat, chew and swallow, dress and bathe yourself if you have tremors and more.</li>
        <br>
        <li><span style="color: #F0F0F0; font-size: 20px;"><b>Part 3: Motor examination.</b></span> <br>A healthcare provider uses this section to determine the movement-related effects of Parkinson's disease. The criteria measure effects based on how you speak, facial expressions, stiffness and rigidity, walking gait and speed, balance, movement speed, tremors, etc.</li>
        <br>
        <li><span style="color: #F0F0F0; font-size: 20px;"><b>Part 4: Motor complications.</b></span> <br>This section involves a provider determining how much of an impact the symptoms of Parkinson’s disease are affecting your life. That includes both the amount of time you have certain symptoms each day, and whether or not those symptoms affect how you spend your time.</li>
    </ul>
    """,
    unsafe_allow_html=True
    )
    space()
    space()
    st.divider()
    space()
    space()

    #Medications to treat motor symptoms of PD code  table
    st.subheader("📅 Medications to treat motor symptoms of PD:")
    space()
    space()

    # Define the HTML content (assuming it's stored in a variable)
    html_content = """
    <table >
            <tr>
                <th>Category</th>
                <th>Generic</th>
                <th>Brand Name</th>
            </tr>
            <tr>
                <td>Drugs that increase brain levels of dopamine</td>
                <td>Levodopa/carbidopa</td>
                <td>Parcopa, Sinemet</td>
            </tr>
            <tr>
                <td>Drugs that mimic dopamine (dopamine agonists)</td>
                <td>Apomorphine<br>Pramipexole<br>Ropinirole<br>Rotigotine</td>
                <td>Apokyn<br>Mirapex<br>Requip<br>Neupro</td>
            </tr>
            <tr>
                <td>Drugs that inhibit dopamine breakdown (MAO-B inhibitors)</td>
                <td>Rasagiline<br>Selegiline (deprenyl)</td>
                <td>Azilect<br>Eldepryl, Zelapar</td>
            </tr>
            <tr>
                <td>Drugs that inhibit dopamine breakdown (COMT inhibitors)</td>
                <td>Entacapone<br>Tolcapone</td>
                <td>Comtan<br>Tasmar</td>
            </tr>
            <tr>
                <td>Drugs that decrease the action of acetylcholine (anticholinergics)</td>
                <td>Benztropine<br>Ethopropazine<br>Trihexyphenidyl</td>
                <td>Cogentin<br>Parsidol<br>Artane</td>
            </tr>
            <tr>
                <td>Drugs for Parkinson's Disease with unknown mechanism of action</td>
                <td>Amantadine</td>
                <td>Symmetrek</td>
            </tr>
        </table>
    """

    # Use pandas.read_html to parse the HTML content
    df = pd.read_html(html_content)[0]

    # Improve column naming (optional)
    df.columns = ['Category', 'Generic Name', 'Brand Names']

    # Define CSS styles for table formatting
    css = """
    <style>
    table {
      border-collapse: collapse;
      font-size: 18px;  
    }
    table tr td{
      border: 1px solid green;
    }
    th, thead th {
      background-color: #3b5aa3;
      font-size: 20px;
    }
    </style>
    """

    # Create a styled container for the table
    with st.container():

        st.write(css, unsafe_allow_html=True)
        st.table(df)

    space()
    st.divider()
    space()

    #WHO response
    st.subheader("🌍 WHO response:")
    st.write(
    """
    <div style="text-align: justify; font-size: 18px;">
        ⭕ In May 2022, the World Health Assembly endorsed the Intersectoral global action plan on epilepsy and other neurological disorders 2022–2031. The action plan will address the challenges and gaps in providing care and services for people with epilepsy and other neurological disorders such as PD that exist worldwide and ensure a comprehensive, coordinated response across sectors. This includes raising policy prioritization and strengthening governance, providing effective, timely and responsive diagnosis, treatment and care, implementing strategies for promotion and prevention, fostering research and innovation and strengthening information systems.
    </div>
    <br>
    <div style="text-align: justify; font-size: 18px;">
       ⭕ A WHO technical brief entitled Parkinson disease: a public health approach is available for policy-makers, health programme managers and planners, healthcare providers, researchers, people with PD, carers and other stakeholders. It outlines the important action areas for intervention in PD including global health policies focused on prevention and risk reduction, education and awareness and access to treatment and care at various levels of the health system. WHO’s iSupport, a knowledge and skills training programme for carers of people living with dementia is available as an online course and a hardcopy manual. iSupport Lite includes easy-to-read posters and a brief video that can act as a quick reference or a refresher, reinforcing previously acquired caregiving skills and knowledge.

    """,
    unsafe_allow_html=True

    )

    space()
    space()
    st.divider()

    space()
    space()

    # References code
    st.subheader("📃 References:")
    st.markdown(
        "- [National Institute of Neurological Disorders and Stroke - Parkinson's Disease Information Page](https://www.ninds.nih.gov/Disorders/All-Disorders/Parkinsons-Disease-Information-Page)\n"
        "- [Michael J. Fox Foundation for Parkinson's Research](https://www.michaeljfox.org/)\n"
        "- [Parkinson's Foundation](https://www.parkinson.org/)"
     )


#detecting code 2nd side bar

if selected == "Detection":
    # Your Streamlit app code below...
    # Disable scientific notation for clarity
    # Disable scientific notation for clarity

    np.set_printoptions(suppress=True)


    st.title(
        "🧑‍⚕️ Detecting Parkinson's Disease"
    )

    st.divider()
    
    # Load the EfficientNetB7 model
    model_effnet_b7 = load_model("effnet_b7.h5")

    def img_pred(file_content):
        try:
            # Read the content of the uploaded file

            # Read the content of the uploaded file
            image_data = io.BytesIO(file_content[list(file_content.keys())[0]]['content'])

            # Convert bytes-like object to numpy array
            nparr = np.frombuffer(image_data.getvalue(), np.uint8)

            # Decode image
            uploaded_opencv_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Convert BGR to RGB
            uploaded_opencv_img = cv2.cvtColor(uploaded_opencv_img, cv2.COLOR_BGR2RGB)

            # Resize image
            uploaded_resized_img = cv2.resize(uploaded_opencv_img, (150, 150))

            # Display the uploaded image
            st.image(uploaded_resized_img, caption='Uploaded Image', channels="RGB", width=150)

            # Prediction with EfficientNetB7
            pred_effnet_b7 = model_effnet_b7.predict(uploaded_resized_img.reshape(1, 150, 150, 3))
            pred_effnet_b7 = np.argmax(pred_effnet_b7, axis=1)[0]

            if pred_effnet_b7 == 0:
                pred_effnet_b7 = 'Healthy'
                st.balloons()
                st.success(f'EfficientNetB7 predicts: {pred_effnet_b7}')
            elif pred_effnet_b7 == 1:
                pred_effnet_b7 = 'Parkinson'
                st.error(f'EfficientNetB7 predicts: {pred_effnet_b7}')
                if st.button("Recommendation"):
                    recommendation()


        except Exception as e:
            st.warning(f'Error: {e}')


    # Streamlit UI
    uploader = st.file_uploader("Upload an image to detect Parkinson's Disease", type=["jpg", "jpeg", "png"])

    if uploader is not None:
        img_pred({uploader.name: {"content": uploader.getvalue()}})
        space()
        st.divider()
        space()
        # Health care analysis
        st.header("⚕️Health care analysis")
        space()
        with st.container():
            col1, col2 = st.columns([0.5, 1.2])
        with col1:
            # code for Table Countries Affected By Parkinson Disease
            # Custom HTML/CSS for the alternating light and dark white boxes
            num_boxes = 5
            box_colors = ["#f5f5f5", "#e0e0e0"]  # Light and dark white colors
            st.markdown("""
                        <br>
                        <h4 style="text-align: left; font-size: 16px;">Top 10 Countries Affected By Parkinson Disease</h4>
                        <table>
                        <thead>
                        <tr>
                        <th>S.No</th>
                        <th>Countries</th>
                        <th>Affected Peoples</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                        <td>1.</td>
                        <td>China</td>
                        <td>2.5 million</td>
                        </tr>
                        <tr>
                        <td>2.</td>
                        <td>India</td>
                        <td>2.1 million</td>
                        </tr>
                        <tr>
                        <td>3.</td>
                        <td>United States</td>
                        <td>1 million</td>
                        </tr>
                        <tr>
                        <td>4.</td>
                        <td>Brazil</td>
                        <td>600,000</td>
                        </tr>
                        <tr>
                        <td>5.</td>
                        <td>Russia</td>
                        <td>500,000</td>
                        </tr>
                        <tr>
                        <td>6.</td>
                        <td>Japan</td>
                        <td>400,000</td>
                        </tr>
                        <tr>
                        <td>7.</td>
                        <td>Indonesia</td>
                        <td>350,000</td>
                        </tr>
                        <tr>
                        <td>8.</td>
                        <td>Germany</td>
                        <td>250,000</td>
                        </tr>
                        <tr>
                        <td>9.</td>
                        <td>Bangladesh</td>
                        <td>250,000</td>
                        </tr>
                        <tr>
                        <td>10.</td>
                        <td>Nigeria</td>
                        <td>200,000</td>
                        </tr>
                        </tbody>
                        </table>
                            """, unsafe_allow_html=True)


        with col2:

             # Bar chart Parkinson disease
            def parkinson_disease():
                # Sample data for the chart
                years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
                affected_people = [6.1, 6.1, 7, 8.5, 9.4, 9.5, 10]  # in millions

                # Create a bar chart
                fig, ax = plt.subplots(figsize=(14, 6.5), frameon=False)
                ax.bar(years, affected_people, width=0.3, align='center', color='#96C0CE', edgecolor='none',bottom = 0.4)  # Adjusted bar width

                ax.set_xlabel('Year', fontsize=15, color='white', labelpad=10)  # Add labelpad to adjust space
                ax.set_ylabel('Number of Affected People (in millions)', fontsize=15, color='white', labelpad=10)  # Add labelpad to adjust space
                ax.tick_params(axis='x', labelrotation=45, labelcolor='white',labelsize=12, width=2, size=8,)
                ax.tick_params(axis='y', labelcolor='white',labelsize=12, width=2, size=8)
                ax.grid(axis='y', linestyle='-', linewidth=1, color='white', alpha=0.7)

                # Customizing background color
                fig.patch.set_facecolor('#174E6E')
                ax.set_facecolor('#174E6E')
                plt.gca().set_axisbelow(True)

                # Remove spines
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                # Display the chart
                space()
                space()
                st.write(
                     "<p style='font-size: 16px; margin-left: 80px;'>The chart displays the number of Parkinson's disease patients over the years</p>",
                     unsafe_allow_html=True)
                st.pyplot(fig)

            parkinson_disease()
        space()
        space()
        st.divider()
        space()
        st.header("📈 Statistics")
        space()
        # Modified Statistics
        stats_container = st.container()
        with stats_container:
            c1, c2, c3, c4 = st.columns([0.1,0.1,0.1,0.1])
            with c1:
                with stylable_container(
                        key="stats_css",
                        css_styles=[
                            """
                                {
                                    background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
                                    border-radius: 50px;
                                    max-width: 300px;
                                    padding: 20px;
                                    
                                }
                            """
                        ],
                ):
                    st.write("<h1 style='font-size: 25px;color: #28231d; text-align:center; margin-left: -60px;'>10M</h1>", unsafe_allow_html=True)
                    st.write("<h3 style='font-size: 20px;color: #28231d; text-align:center;  margin-top: -10px;margin-left: -60px;'>Total Affected</h3><br>",
                             unsafe_allow_html=True)

            with c2:
                with stylable_container(
                        key="stats_css",
                        css_styles=[],
                ):
                    st.write("<h1 style='font-size: 25px;color: #28231d; text-align:center;margin-left: -60px;'>60</h1>",
                             unsafe_allow_html=True)
                    st.write(
                        "<h3 style='font-size: 20px;color: #28231d; text-align:center; margin-top: -10px;margin-left: -60px;'>Average Age of Onset</h3><br>",
                        unsafe_allow_html=True)
            with c3:
                with stylable_container(
                        key="stats_css",
                        css_styles=[],
                ):
                    st.write("<h1 style='font-size: 25px;color: #28231d; text-align:center;margin-left: -60px;'>4M</h1>",
                             unsafe_allow_html=True)
                    st.write(
                        "<h3 style='font-size: 20px;color: #28231d; text-align:center; margin-top: -10px;margin-left: -60px;'>Total Male Affected</h3><br>",
                        unsafe_allow_html=True)
            with c4:
                with stylable_container(
                        key="stats_css",
                        css_styles=[],
                ):
                    st.write("<h1 style='font-size: 25px;color: #28231d; text-align:center;margin-left: -60px;'>6M</h1>",
                             unsafe_allow_html=True)
                    st.write(
                        "<h3 style='font-size: 20px;color: #28231d; text-align:center; margin-top: -10px;margin-left: -60px;'>Total Female Affected</h3><br>",
                        unsafe_allow_html=True)


        st.divider()


        # PIE Chart
        st.header("📊 Pie Chart")
        with st.container():
            c1, c2 = st.columns([1,1.8])
            with c1:


                html_code = """
                
                <figure class="pie-chart">
                <br>
                <br>
                <figcaption>
                <br>
                <br>
                Age above 60(96.1%) <span style="color:#34ada9"></span><br>
                Age below 60(3.8%)<span style="color:#84a39a"></span>
                </figcaption>
                </figure>
                """

                # CSS code for the pie chart
                css_code = """
                /* CSS code for the pie chart */
                .pie-chart {
                 background: radial-gradient(circle closest-side, #fff 0, #fff 45.14%, transparent 45.14%, transparent 61%, #fff 0),
                 conic-gradient(from 22deg, #87CEEB 96.1%, #87CEEB 96.1%, #84a39a 3.8%, #84a39a 3.8%);
                 position: relative;
                 width: 400px;
                 height: 400px;
                 margin: 0;
                 outline: 1px solid #ccc;
                 background-color: skyblue; /* Change background color to sky blue */
                 }
                
                
                
                .pie-chart h2 {
                position: absolute;
                margin: 1rem;
                }
                
                .pie-chart cite {
                position: absolute;
                bottom: 0;
                font-size: 80%;
                padding: 1rem;
                color: gray;
                }
                
                .pie-chart figcaption {
                position: absolute;
                bottom: 1em;
                right: 1em;
                font-size: smaller;
                text-align: right;
                color:black;
                }
                
                .pie-chart span:after {
                display: inline-block;
                content: "";
                width: .8em;
                height: .8em;
                margin-left: .4em;
                height: .8em;
                border-radius: .2em;
                background: currentColor;
                }
                """

                # Display the HTML and CSS
                st.write("")
                st.write("")
                st.markdown(html_code, unsafe_allow_html=True)
                st.write("")
                st.write("")
                st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

            with c2:

                st.markdown("<p style='font-size:20px; margin-top: 25px; text-align: left;'>Summary</p><br><p style='font-size:18px; text-align: justify; margin-top: -10px;'>The image data suggests a clear distinction between individuals above and below the age "
                             "of 60, with 96.1% falling into the older age category and 3.8% into the younger age "
                             "category. This information is relevant to Parkinson's disease as it is known to "
                             "predominantly affect those over 60, with the risk increasing significantly with age. "
                             "<br><br>Analytically, this data underscores the strong correlation between age and Parkinson's "
                             "disease, emphasizing the higher susceptibility of individuals above 60. <br><br>It further "
                             "highlights the importance of age as a factor in studying the onset and prevalence of "
                             "Parkinson's, providing valuable insights for research, diagnosis, and treatment "
                             "strategies.<br><br>In addition to the age distribution, the image data also reveals a slight gender imbalance, with 53.7% of the individuals being male and 46.3% being female.</p>",unsafe_allow_html=True)


        space()
        st.divider()
        space()
        space()

        # Contact
        with st.container():
         c1, _, c2 = st.columns([1.7, 0.3, 1])
         with c1:
            # Contact Us section
            st.markdown(
            """
            <div style="background-color: #f0f0f0; padding: 30px; border-radius: 10px; text-align:center; max-width: 1400px; margin: auto;">
            <p style="font-size: 24px; font-weight: bold; color: #23395d; margin-top: 20px;">📱Contact Us</p>
            <hr style="border-top: 2px solid #23395d; margin: 20px 0;">
            <div style="text-align: left; margin-bottom: 20px;">
            <p style="font-size: 18px; color: #333; margin: 0;"><strong>📫 Email:</strong> contact@parkinson.com</p>
            </div>
            <div style="text-align: left; margin-bottom: 20px;">
            <p style="font-size: 18px; color: #333; margin: 0;"><strong>📞 Phone:</strong> +91 778-946-5120</p>
            </div>
            <div style="text-align: left;">
            <p style="font-size: 18px; color: #333; margin: 0;"><strong>🏢 Address:</strong></p>
            <p style="font-size: 18px; color: #333; margin: 0;">Parkinson Technologies Pvt. Ltd.,</p>
            <p style="font-size: 18px; color: #333; margin: 0;">1234 Park Street,Bangalore, Karnataka, India - 560001</p>
            </div>
            </div>
            """,
            unsafe_allow_html=True
            )

        with c2:
            with stylable_container(
                key="image_con",
                css_styles=[
                    """
                        {
                            margin-top: 50px;
                        }
                    """
                ],
            ):
                st.image("contact.png", width=250)




# Recommendation
if selected == "Recommendation":
    recommendation()



if selected == "Contact":
    def truncate_url(url, max_length=35):
        if len(url) > max_length:
            url = url[:max_length - 3] + "..."
        return url


    st.title("☎️ Contact Information:")
    space()
    st.write("<p style='font-size: 22px; font-weight: bold;'>For more information about Parkinson’s disease:</p>", unsafe_allow_html=True)
    space()
    contact_info = {
        "Organization": [
            "National Institute of Neurological Disorders and Stroke (NINDS)",
            "National Institute of Environmental Health Sciences (NIEHS)",
            "American Parkinson Disease Association (APDA)",
            "Davis Phinney Foundation",
            "Michael J. Fox Foundation for Parkinson's Research",
            "Parkinson Alliance",
            "Parkinson’s Resource Organization",
            "Parkinson's Foundation"
        ],
        "Phone": [
            "800-352-9424",
            "919-541-3345",
            "800-223-2732",
            "866-358-0285",
            "212-509-0995",
            "800-579-8440",
            "877-775-4111",
            "800-473-4636"
        ],
        "Email": [
            "braininfo@ninds.nih.gov",
            "webcenter@niehs.nih.gov",
            "apda@apdaparkinson.org",
            "info@davisphinneyfoundation.org",
            None,
            "contact@parkinsonalliance.org",
            "info@parkinsonsresource.org",
            "helpline@parkinson.org"
        ],
        "Website": [
            "www.ninds.nih.gov",
            "www.niehs.nih.gov/health/topics/conditions/parkinson",
            "www.apdaparkinson.org",
            "www.davisphinneyfoundation.org",
            "www.michaeljfox.org",
            "www.parkinsonalliance.org",
            "www.parkinsonsresource.org",
            "www.parkinson.org"
        ]
    }

    df = pd.DataFrame(contact_info)

    # Format HTML for the table
    html_table = "<table style='width: 75%;'><tr><th style='width: 40%; height: 60px;  background-color: #3b5aa3;'>Organization</th><th style='width: 20%; height: 50px; background-color: #3b5aa3;'>Phone</th><th style='width: 20%; height: 50px; background-color: #3b5aa3;'>Email</th><th style='width: 10%; height: 10px; background-color: #3b5aa3;'>Website</th></tr>"
    for index, row in df.iterrows():
        organization = f"<b>{row['Organization']}</b>"
        phone = f"<b>{row['Phone']}</b>"
        email = f"<b>{row['Email']}</b>" if row['Email'] else ""
        website = f"<b><a href='http://{row['Website']}' target='_blank'>{truncate_url(row['Website'])}</a></b>"
        html_table += f"<tr><td>{organization}</td><td>{phone}</td><td>{email}</td><td>{website}</td></tr>"
    html_table += "</table>"

    # Display HTML table
    st.write(html_table, unsafe_allow_html=True)
    space()
    space()
    st.divider()

    #FAQ code
    space()
    space()

    # Define a function to create collapsible sections
    st.title("✍️ Frequently asked questions")
    space()

    def create_collapsible_section(question, answer):
    # Use st.expander for collapsible sections
        with st.expander(f"**{question}**"):
        
        
            st.markdown(f"<p style='font-size:18px; text-align:justify'>{answer}</p>", unsafe_allow_html=True)

    # FAQ data
    faq_data = [

        ("What is Parkinson’s?", "There are over 50 different symptoms that people with Parkinson’s can experience, though each person has a different combination of some but not all of them. The nature and severity of symptoms can vary considerably from one individual to another as well as from day to day. In the early stages of the condition, symptoms can be vague and non-specific such as constipation, loss of smell, fatigue, sleep disturbances, unexplained depression, anxiety or muscle pain. The four key motor symptoms are tremor (shaking), muscle rigidity (stiffness), bradykinesia (slowness of movement) and postural instability (balance issues and falls). Generally, you must have at bradykinesia plus another for a diagnosis of Parkinson’s to be considered. It is worth noting that in 30% of cases a resting tremor will not be present. A good place to start building your understanding is by reading some of our resources and information sheets."),
        ("What causes Parkinson’s?", "Just like someone with diabetes cannot produce their own insulin, someone with Parkinson’s cannot produce enough dopamine. The cells in a particular part of the brain die off, causing a reduction in the level of this neurotransmitter brain messenger chemical). Dopamine helps with mood and movement, so these areas are particularly affected. There are several theories on what causes Parkinson’s; however, currently we do not have a clear picture of what triggers this dying off process and why some people are affected, and others are not. Best knowledge to date says it is a combination of head trauma, family history, pharmaceutical and/or environmental toxins like pesticides that trigger onset of parkinsonian symptoms. Being male and of older age also are risk factors. What we do know is that every person with Parkinson’s experiences a loss of dopamine in the brain, along with which combination of symptoms and their progression that is unique to them."),
        ("What will my doctor do if Parkinson’s is suspected?", "There is currently no test or biomarker that can definitively diagnose Parkinson’s. Everyone’s combinations of Parkinson’s symptoms are different making it tricky to diagnose. A GP or neurologists often looks at a clinical history plus motor symptoms, like the stereotypical slow and stiff movements and shaking."),
        ("Is there a cure for Parkinson’s?", "Not yet. Parkinson’s usually has a slow progression but is currently incurable. However, there are a variety of medications and treatments that can help control or reduce the symptoms of Parkinson’s. Many people with Parkinson’s live full and productive lives for decades."),
        ("What can I do to manage my Parkinson’s?", "Being proactive about your Parkinson’s will also help you manage any fear or anxiety you may be experiencing due to the diagnosis. It is very important to gain an understanding of which of your symptoms are caused by Parkinson’s. The good news is that there are a wide range of early intervention strategies you can employ to continue to live well with Parkinson’s for a long time. Assemble a care team that will help you plan your wellness journey."),
        ("Is Parkinson’s hereditary?", "Parkinson’s can run in families because of faulty genes, but this is very rare (about 10-15% of cases). Most people with Parkinson’s have idiopathic Parkinson’s, where the cause is unknown. A person’s risk of developing Parkinson’s may also be influenced through their genes, although exactly how these make some people get Parkinson’s is unclear. Research into Parkinson’s has made remarkable progress. There is very real hope that the causes, whether genetic or environmental, will be identified and the precise effects of these will be understood in the near future."),
        ("Where can I find help?", "National advocacy Parkinson’s Australia develops position statements and policies on matters of national significance. Our policies aim to ensure that Australia provides an environment for the Parkinson’s community to promote the best possible quality of life for people with Parkinson’s. We also work with Parliamentary Friendship Groups – non-partisan forums for Federal Members to meet and interact with community causes."),
        ("How can I help someone who has Parkinson’s?", "Learning about the condition and what symptoms your person living with Parkinson’s may experience can be a big support. There needs to be an understanding that Parkinson’s symptoms fluctuate and may cause variability from day to day or even hour to hour and can affect your plans. However, maintaining a social life is very important to the wellbeing of both the person with Parkinson’s and their families. Being flexible and having patience are key to accommodating people living with Parkinson’s. If you are living with or caring for someone with Parkinson’s, you should also consider your own personal needs and look after yourself… seek counselling if necessary. Register yourself and any young carers on the Carers Gateway and see Carers Australia for more information. Just as there are many support groups for people with Parkinson’s, there are also support groups for carers and young carers.")
        ]

    # Display FAQ sections
    for question, answer in faq_data:
        create_collapsible_section(question, answer)
