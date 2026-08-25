## END TO END ML PROJECT

### Project Overview

This project is a Machine Learning regression project that predicts a student's math score based on factors such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score. The project follows a complete end-to-end ML pipeline, starting from data ingestion and preprocessing, followed by model training and evaluation, and finally deploying the trained model through a Flask web application for making predictions on new user input.

### Project Workflow

The complete project flow is:

Raw Dataset
    ↓
Data Ingestion
    ↓
Train/Test Split
    ↓
Data Transformation
    ↓
Feature Preprocessing
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Best Model Selection
    ↓
Save Model + Preprocessor
    ↓
Flask Application
    ↓
User Input
    ↓
Prediction
    ↓
Predicted Math Score
Project Structure
MLProject/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── preprocessing.pkl
│   └── model.pkl
│
├── notebook/
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utile.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── setup.py
├── requirements.txt
└── README.md
### 1. Data Ingestion

The data_ingestion.py file is responsible for reading the original dataset and splitting it into training and testing datasets.

The dataset is read from:

notebook/data/stud.csv

The data is then split into:

80% Training Data
20% Testing Data

The resulting files are stored inside the artifacts directory:

artifacts/train.csv
artifacts/test.csv
artifacts/data.csv

The DataIngestion class also calls the data transformation and model training components to continue the ML pipeline.

## 2. Data Transformation

The data_transformation.py file prepares the raw data so that it can be used by Machine Learning models.

Numerical Features

The numerical columns are:

reading_score
writing_score

For numerical columns:

Missing values are replaced using the median.
StandardScaler is applied to scale the values.
Categorical Features

The categorical columns are:

gender
race_ethnicity
parental_level_of_education
lunch
test_preparation_course

For categorical columns:

Missing values are replaced using the most frequent value.
OneHotEncoder converts categorical values into numerical values.
StandardScaler is applied.

A ColumnTransformer is used to apply the appropriate preprocessing pipeline to numerical and categorical columns.

The target column is:

math_score

The preprocessing object is saved as:

artifacts/preprocessing.pkl
Important

During training:

fit_transform()

is used on the training data.

For testing:

transform()

is used on the test data.

This ensures that the preprocessing rules are learned only from the training data.

### 3. Model Training

The model_trainer.py file is responsible for training and evaluating multiple regression models.

The project evaluates models such as:

Random Forest Regressor
Decision Tree Regressor
Gradient Boosting Regressor
Linear Regression
XGBoost Regressor
CatBoost Regressor
AdaBoost Regressor

Different hyperparameter combinations are evaluated to find the best-performing model.

The models are compared using the R² score.

The model with the highest score is selected as the best model.

If the best model's score is below 0.60, a CustomException is raised.

The selected model is saved as:

artifacts/model.pkl
### 4. Model Evaluation

The evaluate_models() function from src/utile.py is used to train and evaluate the different models.

The general process is:

Training Data
     ↓
Train Multiple Models
     ↓
Try Different Parameters
     ↓
Evaluate Models
     ↓
Compare R² Scores
     ↓
Select Best Model

The R² score is calculated using:

r2_score()

A higher R² score indicates better predictive performance.

### 5. Prediction Pipeline

The predict_pipeline.py file is responsible for making predictions on new data.

It contains two important classes:

CustomData

CustomData receives the user's input:

gender
race_ethnicity
parental_level_of_education
lunch
test_preparation_course
reading_score
writing_score

These values are converted into a Pandas DataFrame.

PredictPipeline

PredictPipeline loads the saved:

artifacts/preprocessing.pkl
artifacts/model.pkl

The new input is first transformed using the saved preprocessing object:

preprocessor.transform(features)

The transformed data is then passed to the trained model:

model.predict(data_scaled)

The final prediction is the student's predicted:

Math Score
### 6. Flask Application

The app.py file provides the web interface for making predictions.

The Flask application contains two main routes:

Home Route
@app.route('/')

This displays the main page.

Prediction Route
@app.route('/predictdata', methods=['GET', 'POST'])

When the user submits the form:

User Input
    ↓
app.py
    ↓
CustomData
    ↓
DataFrame
    ↓
PredictPipeline
    ↓
Preprocessing
    ↓
Trained Model
    ↓
Prediction
    ↓
home.html

The predicted math score is then displayed to the user.

### 7. Complete End-to-End Flow

The complete training pipeline works as follows:

stud.csv
   ↓
data_ingestion.py
   ↓
Train/Test Split
   ↓
train.csv + test.csv
   ↓
data_transformation.py
   ↓
Handle Missing Values
   ↓
Encode Categorical Features
   ↓
Scale Numerical Features
   ↓
preprocessing.pkl
   ↓
model_trainer.py
   ↓
Train Multiple Models
   ↓
Evaluate Models
   ↓
Select Best Model
   ↓
model.pkl

After training, the prediction pipeline works as follows:

User Input
   ↓
app.py
   ↓
CustomData
   ↓
Pandas DataFrame
   ↓
PredictPipeline
   ↓
Load preprocessing.pkl
   ↓
transform()
   ↓
Load model.pkl
   ↓
predict()
   ↓
Predicted Math Score
   ↓
Display Result
8. Installation

Clone the project and navigate to the project directory.

Install the required dependencies:

pip install -r requirements.txt

Install the project as a package:

pip install -e .
### 9. Run the Project

To run the Flask application:

python app.py

The application will start locally and can be accessed through the Flask server URL.

### 10. Technologies Used
Python
Pandas
NumPy
Scikit-learn
XGBoost
CatBoost
Flask
Joblib/Pickle
HTML/CSS
### 11. Key Concepts Demonstrated

This project demonstrates several important Machine Learning concepts:

Data Ingestion
Train/Test Split
Data Preprocessing
Missing Value Imputation
One-Hot Encoding
Feature Scaling
Pipelines
ColumnTransformer
Regression Algorithms
Hyperparameter Tuning
Model Evaluation
R² Score
Model Serialization
Prediction Pipeline
Flask Deployment
End-to-End Machine Learning Workflow
Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow, from loading and preprocessing raw data to training multiple regression models, selecting the best-performing model, saving the trained model and preprocessing object, and finally using them through a Flask web application to predict a student's math score from new input data.