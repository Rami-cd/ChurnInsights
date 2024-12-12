# Customer Churn Prediction
### Project Overview:

This project aims to predict customer churn using machine learning techniques. By analyzing customer data such as demographic information, subscription details, and service usage, the model can predict whether a customer will churn (leave) or stay with the company. The model uses a Random Forest Classifier and other machine learning techniques to achieve this.
Technologies Used:

- Python: Programming language used for data analysis and model training.
- pandas: Data manipulation and analysis.
- numpy: Numerical computations.
- scikit-learn: For machine learning models and evaluation.
- matplotlib and seaborn: Data visualization.
- FastAPI: API framework to serve the model.
- Docker: Containerization for deployment.
- Git: Version control for the project.

### How the Model Works
### Data Preprocessing:

- Data Cleaning: The dataset is cleaned by handling missing values, encoding categorical variables, and scaling numerical features.
- Model Training: A RandomForestClassifier is trained to predict customer churn. Other models like Logistic Regression, and Support Vector Machine were tested, but Random Forest provided the best results.
- Model Evaluation: The model is evaluated using accuracy, precision, recall, F1 score, and a confusion matrix to ensure its reliability.

### Final Model:

    Model: Random Forest Classifier
    Accuracy: 81+%