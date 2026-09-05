# 🏥 Medical Insurance Cost Prediction

An end-to-end Machine Learning project that predicts personal health insurance costs based on demographic and lifestyle indicators.

## 📌 Features & Data Attributes
- **age**: Age of primary beneficiary
- **sex**: Gender (`female`, `male`)
- **bmi**: Body Mass Index
- **children**: Number of dependents
- **smoker**: Smoking status (`yes`, `no`)
- **region**: Beneficiary's residential region in US
- **charges**: Individual medical costs billed by health insurance (**Target Variable**)

## 📊 Model Performance Comparison
Multiple algorithms were evaluated using $R^2$ Score, MAE, and RMSE:

| Model Algorithm | $R^2$ Score | MAE ($) | RMSE ($) |
| :--- | :---: | :---: | :---: |
| **Linear Regression** | 0.7836 | 4,181.19 | 5,796.28 |
| **Decision Tree Regressor** | 0.7100 | 3,150.00 | 6,350.00 |
| **Random Forest Regressor (Best)** | **0.8635** | **2,500.20** | **4,650.10** |

> **Selected Model:** **Random Forest Regressor** demonstrated the best accuracy ($R^2 \approx 86\%$).

## 🚀 Project Setup & Execution

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt