📌 Breast Cancer Classification using Deep Learning (ANN)

🧠 Project Overview

This project is a Breast Cancer Classification system built using an Artificial Neural Network (ANN).
It predicts whether a tumor is Benign or Malignant using features from the Breast Cancer Wisconsin dataset (sklearn).

The project includes:

Data preprocessing using Pipeline

Exploratory Data Analysis (EDA)

ANN model using TensorFlow/Keras

Streamlit web app for deployment

Docker support for containerization



---

📂 Dataset

The dataset is loaded directly from sklearn:

Breast Cancer Wisconsin Dataset

Features: 30 numeric features

Target:

0 → Malignant

1 → Benign




---

⚙️ Tech Stack

Python 🐍

Pandas & NumPy

Scikit-learn

TensorFlow / Keras

Streamlit

Matplotlib & Seaborn

Docker 🐳



---

📊 Project Workflow

1. Import Libraries


2. Load Dataset from sklearn


3. Exploratory Data Analysis (EDA)


4. Data Preprocessing using Pipeline


5. ANN Model Building


6. Model Evaluation


7. Model Saving


8. Deployment using Streamlit


9. Docker Containerization




---

🧹 Data Preprocessing

Train-test split

Feature scaling using StandardScaler

Pipeline used for clean preprocessing


pipeline = make_pipeline(StandardScaler())


---

🧠 ANN Model Architecture

Input Layer: 30 features

Hidden Layers:

Dense (64 neurons, ReLU)

Dropout (0.3)

Dense (32 neurons, ReLU)

Dropout (0.3)

Dense (16 neurons, ReLU)


Output Layer:

Dense (1 neuron, Sigmoid)




---

📈 Model Performance

Accuracy: ~95% – 99%

Loss: Binary Crossentropy



---

💾 Model Saving

model.save("breast_cancer_ann_model.keras")
joblib.dump(pipeline, "breast_pipeline.pkl")


---

🚀 Run Locally (Streamlit App)

1. Install dependencies

pip install -r requirements.txt

2. Run the app

streamlit run app.py


---

🌐 Streamlit App Features

Manual input of patient data

Real-time prediction

Probability output

Simple UI for medical use case



---

🐳 Docker Deployment

Build Docker Image

docker build -t breast-cancer-app .

Run Container

docker run -p 8501:8501 breast-cancer-app


---

📦 requirements.txt

streamlit
tensorflow
scikit-learn
pandas
numpy
joblib
matplotlib
seaborn


---

📁 Project Structure

Breast_Cancer_Classification/
│
├── app.py
├── breast_cancer_ann_model.keras
├── breast_pipeline.pkl
├── requirements.txt
├── Dockerfile
└── README.md


---

📸 Output Example

Prediction: Benign / Malignant

Probability score shown in Streamlit UI



---

🔥 Future Improvements

Add CSV upload prediction

Improve model with CNN comparison

Deploy on cloud (AWS / Hugging Face Spaces)

Add patient report download (PDF)



---

👨‍💻 Author
Wajid Ul Haq
Data Science Project – Breast Cancer Classification using ANN
