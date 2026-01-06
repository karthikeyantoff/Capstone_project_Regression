 Car Price Prediction – Flask ML App
 
A Machine Learning web application built using **Python, Flask, and Scikit-learn** to predict car prices based on input features.

This project follows a **proper ML workflow**, where multiple regression algorithms were trained, evaluated, and compared.  
The **best-performing model (Decision Tree Regressor)** was selected based on evaluation metrics and deployed using **Vercel** 🚀.

---

## 🔗 Live Demo
👉 https://fiveinoneproject.vercel.app/
---
## Machine Learning Workflow
### 🔹 Algorithms Trained & Tested
The following regression algorithms were implemented and evaluated:
- Linear Regression
- K-Nearest Neighbors Regressor
- Random Forest Regressor
- Decision Tree Regressor  *(Best Performing)*

### 🔹 Evaluation Metric
- **R² Score (Coefficient of Determination)**

After comparing all models, **Decision Tree Regressor achieved the highest accuracy**, so it was finalized and deployed.

---

## Final Deployed Model
- **Algorithm**: Decision Tree Regressor
- **Model Storage**: `joblib`
- **Feature Columns**: Saved separately for consistent inference
- **Prediction Type**: Regression (Car Price)

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- NumPy
- Pandas
- Scikit-learn
  - `LinearRegression`
  - `KNeighborsRegressor`
  - `RandomForestRegressor`
  - `DecisionTreeRegressor`
  - `r2_score`

### Deployment & Tools
- Joblib (Model Serialization)
- Vercel
- Git & GitHub

---

## 📂 Project Structure

```

five_in_one_project/
│
├── app.py                  # Flask backend
├── model.pkl               # Best ML model (Decision Tree)
├── columns.pkl             # Saved feature columns
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment config
├── templates/
│   └── index.html          # Frontend (HTML)
└── README.md

````

---

## ⚙️ Installation (Local Setup)

```bash
# Clone the repository
git clone https://github.com/karthikeyantoff/Capstone_project_Regression

# Navigate into the project
cd capstone_project_Regression

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
````

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📌 How the Application Works

1. User enters car details through the HTML form
2. Flask backend receives the input
3. Input data is aligned using saved feature columns
4. Decision Tree model predicts the car price
5. Predicted price is displayed on the UI

---

## 📦 Requirements

```
flask
gunicorn
numpy
pandas
scikit-learn
joblib
```

---

## 🚀 Deployment

* Successfully deployed on **Vercel**
* Flask backend served using `@vercel/python`
* No build step required
* Model loaded dynamically at runtime

---

## 👨‍💻 Author

**Karthikeyan T**
🔗 GitHub: [https://github.com/karthikeyantoff](https://github.com/karthikeyantoff)

---

## 🔥 Future Improvements

* Add model comparison dashboard
* Improve UI using Bootstrap or Tailwind
* Add REST API endpoints
* Implement model retraining pipeline
* Dockerize the application
