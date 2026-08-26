# Diabetes Prediction System

A machine learning web application that predicts whether a person is likely to have diabetes based on health and medical parameters. The project combines data preprocessing, feature scaling, machine learning classification, and an interactive Streamlit interface to provide real-time predictions.

## 📌 Overview

The Diabetes Prediction System is an end-to-end machine learning project that demonstrates how a trained classification model can be integrated into an interactive web application.

Users can enter the required health parameters through the Streamlit interface, and the application processes the input using the saved scaler before passing it to the trained machine learning model.

The project covers the complete workflow from dataset preparation and model development to model serialization and deployment through Streamlit.

## ✨ Features

- Interactive Streamlit web application
- Real-time diabetes prediction
- Machine learning-based classification
- Data preprocessing and feature preparation
- Feature scaling using a saved scaler
- Pre-trained machine learning model
- User-friendly prediction interface
- Dataset included for experimentation
- Reusable trained model and scaler
- Reproducible environment using `requirements.txt`

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Streamlit
- Pickle
- Git
- GitHub

## 🤖 Machine Learning

The project uses a trained classification model to predict the likelihood of diabetes based on the input health parameters.

The machine learning workflow includes:

1. Loading the diabetes dataset
2. Exploring and preparing the data
3. Separating input features and target variable
4. Preprocessing the data
5. Scaling the input features
6. Training the classification model
7. Evaluating the model
8. Saving the trained model
9. Saving the feature scaler
10. Loading the model and scaler in the Streamlit application
11. Generating predictions from user input

The trained model is stored in:

    model.pkl

The feature scaler is stored in:

    scaler.pkl

## 📊 Dataset

The project uses a diabetes dataset containing health-related patient attributes and diabetes outcomes.

The dataset is stored in:

    diabetes.csv

The dataset is used for model development, preprocessing, and experimentation.

## 📂 Project Structure

    diabetes-prediction/
    │
    ├── app.py
    ├── diabetes_prediction.py
    ├── diabetes.csv
    ├── model.pkl
    ├── scaler.pkl
    ├── requirements.txt
    └── README.md

## 📁 Project Files

### app.py

The main Streamlit application responsible for collecting user inputs and displaying diabetes predictions.

### diabetes_prediction.py

Contains the machine learning workflow used for data preparation, preprocessing, model training, evaluation, and saving the trained model and scaler.

### diabetes.csv

The dataset used for machine learning development and analysis.

### model.pkl

The serialized trained machine learning model used by the Streamlit application.

### scaler.pkl

The serialized feature scaler used to transform user inputs in the same way as the training data.

### requirements.txt

Contains the Python packages required to run the project.

### README.md

Project documentation and setup instructions.

## 🖥️ Application

The application is built using Streamlit and provides an interactive interface for entering the required health parameters.

The user provides the input values, the application preprocesses the data using the saved scaler, and the trained model generates the final prediction.

## 🔄 Prediction Workflow

    User enters health parameters
              │
              ▼
       Input validation
              │
              ▼
      Feature preprocessing
              │
              ▼
        Feature scaling
              │
              ▼
       Trained ML model
              │
              ▼
          Prediction
              │
              ▼
       Result displayed

## ⚙️ Installation

### 1. Clone the Repository

    git clone https://github.com/bhaskar-nb/diabetes-prediction.git

### 2. Navigate to the Project Directory

    cd diabetes-prediction

### 3. Create a Virtual Environment

Windows:

    python -m venv venv

### 4. Activate the Virtual Environment

Windows PowerShell:

    venv\Scripts\activate

### 5. Install Dependencies

    pip install -r requirements.txt

## ▶️ Run the Application

Start the Streamlit application using:

    streamlit run app.py

After running the command, Streamlit will provide a local URL in the terminal.

Open the URL in your browser to use the Diabetes Prediction System.

## 📦 Requirements

The project dependencies are maintained in:

    requirements.txt

The required packages include:

- pandas
- numpy
- scikit-learn
- imbalanced-learn
- streamlit

## 🎯 Project Objectives

The project was developed to:

- Build a machine learning system for diabetes prediction
- Apply data preprocessing techniques
- Scale input features before prediction
- Train and evaluate a classification model
- Save and reuse the trained model
- Save and reuse the feature scaler
- Develop an interactive Streamlit application
- Demonstrate an end-to-end machine learning workflow

## 🔮 Future Improvements

Potential improvements include:

- Compare multiple classification algorithms
- Hyperparameter tuning
- Cross-validation
- Improve model evaluation and reporting
- Add model performance metrics
- Add feature importance visualization
- Display prediction probability
- Improve input validation
- Improve Streamlit UI and user experience
- Deploy the application to a cloud platform
- Implement automated model retraining

## ⚠️ Disclaimer

This project is developed for educational and machine learning demonstration purposes.

The predictions generated by this application should not be considered medical advice or a medical diagnosis. Medical decisions should always be made with the guidance of a qualified healthcare professional.

## 👨‍💻 Author

### Bhaskar Nakka

GitHub:

https://github.com/bhaskar-nb