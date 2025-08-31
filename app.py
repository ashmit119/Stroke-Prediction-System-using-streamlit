import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
metrics = joblib.load('metrics.pkl')
confusion_matrix = joblib.load('confusion_matrix.pkl')

def pred_new(new_record):
    new_df = pd.DataFrame([new_record])
    for col in label_encoders:
        new_df[col] = label_encoders[col].transform(new_df[col])
    prediction = model.predict(new_df)
    return prediction

# CSS for the top navigation bar and styling
st.markdown("""
    <style>
    .body {
        background: linear-gradient(135deg, #f06, #fceabb);
        margin: 0;
    }
    /* Flex container for nav buttons */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        background-color: #333;
        padding: 10px 0;
        margin-bottom: 30px;
        border-radius: 10px;
    }
    /* Streamlit buttons override */
    div.stButton > button {
        background: none;
        border: none;
        color: #f2f2f2;
        font-size: 22px;
        font-weight: 600;
        cursor: pointer;
        padding: 10px 20px;
        border-radius: 8px 8px 0 0;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #ddd;
        color: black;
    }
    /* Custom active button style */
    div.stButton > button:focus, div.stButton > button.active {
        background-color: #008CBA !important;
        color: white !important;
        font-weight: 700 !important;
        outline: none;
        box-shadow: none;
    }
    /* Title with heart logo */
    .main-title {
        font-size: 64px;
        font-weight: 900;
        text-align: center;
        color: #FF6347;
        margin-bottom: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }
    /* Heart logo styling */
    .heart-logo {
        font-size: 70px;
        line-height: 1;
    }
    /* Subtitle smaller under title */
    .subtitle {
        font-size: 28px;
        color: #2E8B57;
        text-align: center;
        font-style: italic;
        margin-top: 0;
        margin-bottom: 30px;
    }
    /* Section titles */
    .section-title {
        color: #4682B4;
        font-size: 24px;
        margin-top: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Pages in nav
pages = ["Home", "About", "Contributors"]

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# Navigation bar container
nav_cols = st.columns(len(pages), gap="large")

for i, page in enumerate(pages):
    is_active = st.session_state.selected_page == page
    # Mark active tab with additional CSS class by using st.markdown workaround with focus
    with nav_cols[i]:
        if st.button(page, key=f"nav_{page}"):
            st.session_state.selected_page = page
        # After render, inject 'active' class for the active button via JS or focus hack is limited so 
        # Currently active styling is best effort with focus or button pressed unless native Streamlit supports.

# Main page content rendering
if st.session_state.selected_page == "Home":
    st.markdown("""
        <div class='main-title'>
            <span class='heart-logo'>❤️</span>
            StrokeSniffer
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your health, your responsibility!</p>', unsafe_allow_html=True)

    st.markdown('<p class="section-title">Fill in your details below</p>', unsafe_allow_html=True)

    gender = st.selectbox("What is your gender?", options=['Please Select', 'Male', 'Female'], index=0)
    age = st.number_input("Please enter your age", min_value=0, max_value=120)
    hypertension = st.selectbox("Do you have hypertension?", options=['Please Select', 'Yes', 'No'], index=0)
    heart_disease = st.selectbox("Do you have heart disease?", options=['Please Select', 'Yes', 'No'], index=0)
    ever_married = st.selectbox("Have you ever been married?", options=['Please Select', 'Yes', 'No'], index=0)
    work_type = st.selectbox("What is your work type?", options=['Please Select', 'Private', 'Self-employed', 'Govt_job', 'Children', 'Never_worked'], index=0)
    Residence_type = st.selectbox("What is your residence type?", options=['Please Select', 'Urban', 'Rural'], index=0)
    avg_glucose_level = st.number_input("Please enter your average glucose level (mg/dL) (Note: The normal range for average glucose levels is between 70 and 140 mg/dL.)", min_value=0.0)
    bmi = st.number_input("Please enter your BMI (Note: A normal BMI value for a healthy individual is around 23.)", min_value=0.0, max_value=50.0)
    smoking_status = st.selectbox("What is your smoking status?", options=['Please Select', 'formerly smoked', 'never smoked', 'smokes'], index=0)

    new_record = {
        'gender': gender,
        'age': age,
        'hypertension': 1 if hypertension == 'Yes' else 0,
        'heart_disease': 1 if heart_disease == 'Yes' else 0,
        'ever_married': 1 if ever_married == 'Yes' else 0,
        'work_type': work_type,
        'Residence_type': Residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }
    if st.button("Predict Stroke", help="Click to predict"):
        if (gender == 'Please Select' or age == 0 or hypertension == 'Please Select' or heart_disease == 'Please Select' or 
            ever_married == 'Please Select' or work_type == 'Please Select' or Residence_type == 'Please Select' or 
            avg_glucose_level == 0.0 or bmi == 0.0 or smoking_status == 'Please Select'):
            st.warning("Please enter all the information asked before proceeding.")
        else:
            prediction = pred_new(new_record)
            if prediction == 1:
                st.error("The model suggests that you may be at risk for a stroke. It's important not to panic, but we strongly recommend that you consult with a healthcare professional for a thorough evaluation. In the meantime, adopting healthier habits like regular exercise, a balanced diet, managing stress, and avoiding smoking can make a significant difference in reducing risks. Early action can be life-saving—take care of yourself!")
            else:
                st.success("Hurray! The model predicts that you are unlikely to have a stroke. Keep up the great work! To maintain your health, continue incorporating regular exercise, a balanced diet, and healthy habits into your routine. Remember, prevention is key—stay active, eat well, and get regular checkups to ensure a healthy future!")

elif st.session_state.selected_page == "About":
    st.title("About StrokeSniffer 🧠💡")
    st.write("""
        Welcome to **StrokeSniffer**, your personalized health companion! This app is designed to help predict the likelihood
        of experiencing a stroke based on critical health and lifestyle factors.

        Leveraging the power of **machine learning**, StrokeSniffer analyzes your inputs—like age, gender, medical history, and 
        more—to provide a prediction. Our model is trained on real medical data to make accurate, data-driven assessments 
        of stroke risk.

        However, it’s important to remember that StrokeSniffer is a **preventive tool** meant to offer guidance, not a 
        diagnostic conclusion. While it provides valuable insights into your health risks, it is always recommended to 
        consult a healthcare professional for an expert evaluation and advice.

        By combining **AI technology** and **user-friendly design**, we aim to empower individuals to take proactive steps 
        toward maintaining their health and well-being. Early detection and awareness can make all the difference when it 
        comes to stroke prevention.

        Whether you’re looking for peace of mind or a prompt to visit your doctor, StrokeSniffer is here to help you on your 
        health journey. Remember—your health is your greatest asset, and prevention is the best cure.

        Take control of your health, and let StrokeSniffer be your guide!
    """)

elif st.session_state.selected_page == "Contributors":
    st.title("👨‍💻 Contributors")
    # Display all contributor names at the top as a list
    st.markdown("""
    **Contributors:**  
    Ashmit Banerjee | Prasun Sengupta | Ankur Chowdhury | Tamoghna Das
    """)
    st.write("---")  # separator line
    st.markdown(""" 
    UG Student, Dept. Of CSE, Institute of Engineering and Management, Kolkata  
    📞 Phone: +91 8583862662  
    ✉️ Email: [ashmitbanerjee11.pkt@gmail.com](mailto:ashmitbanerjee11.pkt@gmail.com)
    """)

