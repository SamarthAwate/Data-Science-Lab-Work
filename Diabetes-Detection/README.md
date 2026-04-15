# 🧠 Early Detection of Diabetes using Machine Learning

## 📌 Overview
This project focuses on predicting diabetes using machine learning techniques. Early detection of diabetes can help prevent serious complications such as heart disease, kidney failure, and vision loss.

The project uses the Pima Indians Diabetes Dataset and applies multiple classification models to compare performance.

---

## 📊 Dataset
- Source: UCI Machine Learning Repository / Kaggle  
- Records: 768  
- Features: 8 input features + 1 target variable  

### Features include:
- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

### Target:
- `0` → No Diabetes  
- `1` → Diabetes  

---

## 🎯 Objectives
1. To predict diabetes using machine learning models  
2. To compare performance of multiple algorithms  
3. To identify the most effective model  

---

## ⚙️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## 🔄 Methodology

### 1. Data Preprocessing
- Replaced invalid zero values with NaN  
- Filled missing values using median  
- Applied feature scaling using StandardScaler  
- Split data into training (70%) and testing (30%)  

### 2. Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Artificial Neural Network (ANN)  

### 3. Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC Curve  

---

## 📈 Results

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 74%      |
| Decision Tree       | 71%      |
| Random Forest       | 76%      |
| ANN                 | 68%      |

### Key Findings:
- Random Forest performed best  
- Logistic Regression gave stable results  
- ANN underperformed due to small dataset  

---

## 📊 Visualizations
- Scatter Plot (Actual vs Predicted)  
- Confusion Matrix  
- ROC Curve  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/diabetes-ml-project.git
