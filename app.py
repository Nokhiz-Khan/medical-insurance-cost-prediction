import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Load trained model and features
model = joblib.load('best_insurance_model.pkl')
model_columns = joblib.load('model_columns.pkl')

def predict_cost(age, sex, bmi, children, smoker, region):
    sex_val = 1 if sex == "male" else 0
    smoker_val = 1 if smoker == "yes" else 0
    
    # Empty DataFrame matching input structure
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    input_df['age'] = age
    input_df['sex'] = sex_val
    input_df['bmi'] = bmi
    input_df['children'] = children
    input_df['smoker'] = smoker_val
    
    region_col = f"region_{region}"
    if region_col in input_df.columns:
        input_df[region_col] = 1
        
    prediction = model.predict(input_df)[0]
    return f"${prediction:,.2f}"

# Interface UI Controls
inputs = [
    gr.Number(label="Age", value=25),
    gr.Dropdown(choices=["female", "male"], label="Sex"),
    gr.Number(label="BMI", value=24.5),
    gr.Slider(minimum=0, maximum=5, step=1, label="Children"),
    gr.Radio(choices=["no", "yes"], label="Smoker?"),
    gr.Dropdown(choices=["southwest", "southeast", "northwest", "northeast"], label="Region")
]

app = gr.Interface(
    fn=predict_cost,
    inputs=inputs,
    outputs=gr.Textbox(label="Predicted Medical Charges ($)"),
    title="🏥 Medical Insurance Cost Predictor",
    description="Enter demographic and health details to estimate annual medical insurance charges."
)

if __name__ == "__main__":
    app.launch()