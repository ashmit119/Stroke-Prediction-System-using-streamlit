# Stroke Prediction System using streamlit
Welcome to StrokeSniffer — a personalized health companion app designed to predict the likelihood of experiencing a stroke based on important health and lifestyle factors.


Project Overview
StrokeSniffer leverages machine learning trained on real medical data to analyze user inputs such as age, gender, medical history, and lifestyle choices to provide an assessment of stroke risk. This project demonstrates the use of Streamlit for a clean, interactive web app interface, combined with data science and model deployment best practices.

Note: This app provides predictive guidance and should never replace professional medical advice. Please consult a healthcare professional for diagnosis and treatment.


Prerequisites
Python 3.7 or above

pip package manager


Features
Interactive web interface built with Streamlit

Inputs include demographics, health conditions, and lifestyle factors

Predictive model loaded from pre-trained machine learning model files

Visual guidance, warnings, and health recommendations based on prediction

Navigation tabs: Home, About, Contributors for rich user guidance


Files Description
app.py: Main Streamlit app file containing UI and prediction logic

model.pkl: Pre-trained stroke prediction machine learning model

label_encoders.pkl: Encoders for categorical variables used in the model

metrics.pkl: Model metrics used for evaluation

confusion_matrix.pkl: Confusion matrix data for model performance

stroke_prediction_dataset.csv: Dataset used for training/testing the model

new notebook.ipynb: Jupyter notebook containing data exploration, model training, or analysis steps

requirements.txt: Python dependencies for the project


License
This project is open-source and free to use for educational and research purposes.


