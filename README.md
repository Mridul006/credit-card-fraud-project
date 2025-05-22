# credit-card-fraud-project

# 💳 Fraud Detection in Credit Card Transactions

Anomaly detection-based machine learning project to identify fraudulent transactions using advanced models like Isolation Forest, Local Outlier Factor, and XGBoost. Includes an interactive Streamlit dashboard for real-time prediction and visualization.

---

## 🎯 Objective

To accurately identify fraudulent credit card transactions using anomaly detection and classification algorithms, and to deploy a user-friendly web application for predictions.

---

## 🛠️ Tools & Technologies

- Python
- Pandas, NumPy
- Scikit-Learn
- XGBoost
- Matplotlib / Seaborn
- Streamlit

---

## 📊 Dataset

- **Source:** [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Description:**
  - 284,807 transactions.
  - 492 fraudulent cases.
  - Features `V1` to `V28` are anonymized PCA components.
  - `Time`, `Amount`, and `Class` (fraud = 1, non-fraud = 0) are also included.

---

## 🧪 Mini Guide to the Project

### 1. 📥 Load and Explore Data
- Use the Kaggle dataset and understand class imbalance.

### 2. ⚙️ Preprocess & Balance Data
- Normalize `Amount` and `Time` if required.
- Apply undersampling or SMOTE to handle class imbalance.

### 3. 🧠 Train XGBoost Classifier
- Use a balanced dataset to train XGBoost for better performance.
- Tune hyperparameters for accuracy and recall.

### 4. 📈 Evaluate Model
- Compare model performance using Receiver Operating Characteristic (ROC).

### 5. 🖥️ Create Dashboard (Streamlit)
- Build a web interface with:
  - Input fields for transaction features.
  - Predict button to show if transaction is Fraud or Not Fraud.
  - Display probability scores and charts (e.g. ROC, feature importances).

### 7. 🚀 Deployment
- Deploy locally using:
  ```bash
  streamlit run app.py
