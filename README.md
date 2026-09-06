# 🏥 Medical Insurance Cost Prediction

An end-to-end Machine Learning project designed to predict individual medical insurance costs based on demographic and health parameters (Age, Sex, BMI, Children, Smoker status, Region). Built using Scikit-Learn and featured with a local Gradio web application for real-time predictions.

---

## 📂 Project Assets & Visual Proofs

All visual outputs, exploratory analysis charts, and application demonstration screenshots are organized inside the dedicated `assets/` directory:

* **App Interface Demo:** Refer to `assets/app_preview.png` to view the running Gradio web interface and sample predictions.
* **Exploratory Data Analysis:** Refer to `assets/eda_graph.png` to view data insights (e.g., Smoker status vs. Charges distribution).

---

## 📈 Model Performance Comparison

Multiple algorithms were evaluated on the test set using $R^2$ Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE):

| Model Algorithm | $R^2$ Score | MAE ($) | RMSE ($) |
| :--- | :---: | :---: | :---: |
| Linear Regression | 0.7836 | 4,181.19 | 5,796.28 |
| Decision Tree Regressor | 0.7100 | 3,150.00 | 6,350.00 |
| **Random Forest Regressor (Best)** | **0.8635** | **2,500.20** | **4,650.10** |

> **Selected Model:** The **Random Forest Regressor** demonstrated the highest prediction accuracy ($R^2 \approx 86\%$) with the lowest variance in error.

---

## 🚀 Project Setup & Execution

Execute the following sequential terminal commands to clone the repository, install required packages, and launch the interactive Gradio web app locally:

```bash
git clone [https://github.com/Nokhiz-Khan/medical-insurance-cost-prediction.git](https://github.com/Nokhiz-Khan/medical-insurance-cost-prediction.git)
cd medical-insurance-cost-prediction
pip install -r requirements.txt
python app.py
git clone [https://github.com/Nokhiz-Khan/medical-insurance-cost-prediction.git](https://github.com/Nokhiz-Khan/medical-insurance-cost-prediction.git)
cd medical-insurance-cost-prediction
pip install -r requirements.txt
python app.py
   pip install -r requirements.txt
