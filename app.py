import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.datasets import load_breast_cancer

# Load model and pipeline
model = load_model("breast_cancer_ann_model.keras")
pipeline = joblib.load("breast_pipeline.pkl")

# Load dataset feature names
data = load_breast_cancer()
feature_names = data.feature_names

st.title("Breast Cancer Classification")
st.write("Enter the feature values below:")

input_data = []

for feature in feature_names:
    value = st.number_input(
            feature,
                    value=0.0,
                            format="%.6f"
                                )
                                    input_data.append(value)

                                    if st.button("Predict"):

                                        input_df = pd.DataFrame(
                                                [input_data],
                                                        columns=feature_names
                                                            )

                                                                input_scaled = pipeline.transform(input_df)

                                                                    prediction = model.predict(input_scaled)

                                                                        result = int(prediction[0][0] > 0.5)

                                                                            if result == 1:
                                                                                    st.success("Prediction: Benign")
                                                                                        else:
                                                                                                st.error("Prediction: Malignant")

                                                                                                    st.write("Probability:", float(prediction[0][0]))