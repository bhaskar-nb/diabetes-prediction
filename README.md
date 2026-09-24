# Diabetes Prediction — Machine Learning + Streamlit

An educational **binary classification project** that predicts the diabetes outcome in the supplied dataset using health-related features, preprocessing, class balancing, and a Random Forest classifier.

The project includes a saved model and scaler and a Streamlit interface for entering patient parameters and generating a model prediction.

> **Medical disclaimer:** This project is for educational and machine-learning demonstration purposes only. Its predictions are not medical diagnoses or medical advice.

## What This Project Does

- Loads and cleans the diabetes dataset.
- Replaces zero values in selected clinical fields with missing values.
- Imputes those missing values with the corresponding feature median.
- Balances the classes using SMOTE.
- Standardizes features with `StandardScaler`.
- Trains a Random Forest classifier.
- Also trains a Logistic Regression model for comparison.
- Saves the trained model and scaler with Pickle.
- Uses Streamlit to collect inputs and display predictions.

## Input Features

The Streamlit application accepts:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin-fold thickness |
| Insulin | Serum insulin level |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age in years |

## Machine Learning Workflow

```text
Diabetes Dataset
      ↓
Data Cleaning
      ↓
Median Imputation
      ↓
SMOTE Class Balancing
      ↓
Train / Test Split
      ↓
Standard Scaling
      ↓
Random Forest + Logistic Regression
      ↓
Model Evaluation
      ↓
Model + Scaler Serialization
      ↓
Streamlit Prediction App
```

## Models

### Random Forest Classifier

The application uses a Random Forest classifier as its saved prediction model.

Configured parameters include:

- 500 trees
- Maximum depth: 10
- Minimum samples split: 5
- Minimum samples leaf: 2
- Square-root feature selection
- `random_state=42`

### Logistic Regression

A Logistic Regression model is also trained as a comparison model during the development workflow.

## Preprocessing

The training script replaces zero values with missing values for:

- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI

Those missing values are filled using the median of each feature before model training.

Feature scaling is performed with `StandardScaler`, and the fitted scaler is saved as `scaler.pkl` so application inputs can be transformed consistently.

## Dataset

The repository contains the source dataset:

```text
diabetes.csv
```

The target column is `Outcome`, with the remaining columns used as model features.

## Project Structure

```text
diabetes-prediction/
├── app.py
├── diabetes_prediction.py
├── diabetes.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## Key Files

| File | Purpose |
|---|---|
| `diabetes_prediction.py` | Data preparation, model training, evaluation, and serialization |
| `app.py` | Streamlit prediction interface |
| `diabetes.csv` | Source dataset |
| `model.pkl` | Saved Random Forest model |
| `scaler.pkl` | Saved StandardScaler |
| `requirements.txt` | Python dependencies |

## Run Locally

### Prerequisites

- Python 3.x
- pip

### Setup

```bash
git clone https://github.com/bhaskar-nb/diabetes-prediction.git
cd diabetes-prediction
python -m venv venv
```

On Windows PowerShell:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Model Evaluation

The training script calculates:

- Accuracy
- Confusion matrix
- Classification report

These results are printed during execution of `diabetes_prediction.py`.

> **Methodology note:** The current script applies SMOTE before the train/test split. This can introduce information leakage into evaluation data and can make the reported test metrics optimistic. A stronger implementation would split first, then apply SMOTE only to the training set.

## Limitations

- The model is trained on the supplied historical dataset and should not be treated as a clinical tool.
- The project does not provide external clinical validation.
- The current evaluation workflow has the SMOTE-before-split leakage issue noted above.
- Model performance may change with different train/test splits or datasets.
- The Streamlit application returns a classification result but does not provide a calibrated clinical risk score.

## Future Improvements

- Apply SMOTE only after the train/test split.
- Use a Pipeline to combine preprocessing, resampling, and model training safely.
- Add cross-validation.
- Report precision, recall, F1-score, ROC-AUC, and other relevant metrics clearly.
- Compare multiple models systematically.
- Add calibrated prediction probabilities.
- Add model explainability such as model-derived feature importance.
- Add tests for input validation and preprocessing consistency.

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Random Forest
- Logistic Regression
- StandardScaler
- SMOTE
- Classification evaluation
- Pickle model serialization
- Streamlit
- Data preprocessing
- Git & GitHub

## Portfolio Relevance

This project demonstrates an applied machine-learning workflow from **raw health dataset → preprocessing → class balancing → model training → evaluation → serialized model → interactive application**.

It is best presented as a **machine-learning learning project**, not as a clinical or production healthcare system.

## Author

**Bhaskar Nakka**  
Data Analyst | SQL · Python · Excel · Tableau · Power BI