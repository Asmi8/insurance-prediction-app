# 🧠 Insurance Purchase Prediction App

This project is a real-world machine learning simulation built to predict whether a customer is likely to purchase caravan insurance, using behavioral and demographic data. The model is deployed using Streamlit to enable real-time scoring and customer targeting.

## 🚀 Live App

👉 [Click here to try the live app](https://insurance-prediction-app-sbvenweidyku9gdpx2lbdz.streamlit.app)

Upload a CSV file containing customer data and receive predictions on the likelihood of caravan insurance purchase.

## 📂 Repository Overview

- `app(2).py`: Streamlit application code
- `final_rf_model.pkl`: Trained Random Forest Classifier
- `final_scaler.pkl`: StandardScaler used to preprocess the data
- `requirements.txt`: Required Python libraries
- `sample_input.csv`: Sample input file to test the app

## 🎯 Project Objective

To build an end-to-end machine learning solution that:
- Predicts caravan insurance purchases
- Prioritizes customer leads for marketing or sales
- Provides a deployable, user-friendly interface for business teams

## 🧰 Tools & Technologies

- Python, Pandas, NumPy
- Scikit-learn (Random Forest, Preprocessing)
- Streamlit for app deployment
- Joblib for model persistence
- Git & GitHub for version control

## 📊 Dataset

- **Source**: [UCI ML Repository - Insurance Company Benchmark (COIL 2000)](https://archive.ics.uci.edu/dataset/125/insurance+company+benchmark+coil+2000)
- **Features**: 85 customer-related features
- **Target**: `CARAVAN` (1 = purchased, 0 = not purchased)

## 🧪 Model Performance

- Random Forest Classifier trained with class weights
- Evaluated using precision, recall, F1-score, and ROC-AUC
- Predictions output as:
  - `Predicted_Probability`
  - `Predicted_Caravan` (0 or 1)

## 📥 How to Use

1. Go to the [Streamlit app](https://insurance-prediction-app-sbvenweidyku9gdpx2lbdz.streamlit.app)
2. Upload a CSV file with 85 features (`Feature_0` to `Feature_84`)
3. View predicted probabilities and download the results

## 📈 Example Output

| Feature_0 | ... | Feature_84 | Predicted_Probability | Predicted_Caravan |
|-----------|-----|-------------|------------------------|-------------------|
| ...       | ... | ...         | 0.82                   | 1                 |

## About Me

This project was developed by [Asmi Panigrahi](https://www.linkedin.com/in/asmi-panigrahi/), a Master's student in Computer Science passionate about applying AI and machine learning in real-world business scenarios. I am currently seeking full-time opportunities in data science and machine learning.

## 📫 Contact

📧 Email: [panigrahiasmi18@gmail.com]  
🔗 LinkedIn: [https://www.linkedin.com/in/asmi-panigrahi/](https://www.linkedin.com/in/asmi-panigrahi/)

## ⭐️ If you find this useful, please star the repo or share it!

