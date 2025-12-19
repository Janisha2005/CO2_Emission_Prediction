# 🚗 CO₂ Emission Prediction using Polynomial Regression

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Project Overview
This project predicts **vehicle CO₂ emissions (g/km)** based on engine specifications and fuel consumption using a **Polynomial Regression model**.  
The model is deployed as an **interactive Streamlit web application** and follows **best ML practices** using a full `sklearn Pipeline`.

---

## 🎯 Problem Statement
Vehicle CO₂ emissions depend on factors like engine size, cylinders, and fuel consumption, which often have **non-linear relationships**.  
This project aims to model those relationships accurately and provide **real-time predictions** through a web interface.

---

## 🧠 Solution Approach
- Applied **IQR-based outlier handling** to reduce the impact of extreme values
- Used **Polynomial Regression** to capture non-linear patterns
- Built a **scikit-learn Pipeline** to avoid data leakage
- Evaluated model performance using **R² Score** and **RMSE**
- Deployed the trained pipeline using **Streamlit**

---

## 📊 Dataset
**Fuel Consumption & CO₂ Emissions (Canada)**  
Source: Kaggle  

### Features Used
- `ENGINESIZE`
- `CYLINDERS`
- `FUELCONSUMPTION_COMB`

### Target
- `CO2EMISSIONS`

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

## 🧪 Model Pipeline
- Outliers handled using **Interquartile Range (IQR)**
- Polynomial features used to model non-linear relationships
- Entire pipeline saved as a `.pkl` file for deployment

---

## 📈 Model Performance
| Metric | Value |
|------|------|
| R² Score | **0.888** |
| RMSE | **18.77 g/km** |

✅ Explains ~89% of variance  
✅ Average prediction error ≈ 19 g/km  

---

## 🌐 Streamlit Web App
The app allows users to:
- Enter vehicle specifications
- Predict CO₂ emissions in real time
- View model performance metrics
