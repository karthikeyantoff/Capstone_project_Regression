# import joblib

# # Load model and columns
# model = joblib.load("car_price.pkl")
# columns = joblib.load("columns.pkl")

# print("✅ Model loaded:", type(model))
# print("✅ Columns loaded:", columns)

# # 🔹 Sample test input (same order as columns)
# sample_input = {
#     'wheelbase': 98.8,
#     'carlength': 176.6,
#     'carwidth': 66.2,
#     'enginesize': 130,
#     'horsepower': 111,
#     'citympg': 21,
#     'highwaympg': 27
# }

# # Arrange data in correct order
# data = [float(sample_input.get(col, 0)) for col in columns]

# # Predict
# prediction = model.predict([data])[0]

# print("✅ Predicted Car Price:", round(prediction, 2))
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# 🔹 Load model and columns (same as test code)
model = joblib.load("car_price.pkl")
columns = joblib.load("columns.pkl")

@app.route("/")
def home():
    return render_template("index.html", columns=columns)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input
        input_data = request.form.to_dict()

        # SAME LOGIC AS test_model.py
        data = [float(input_data.get(col, 0)) for col in columns]

        # Predict
        prediction = model.predict([data])[0]

        return render_template(
            "index.html",
            columns=columns,
            prediction_text=f"Predicted Car Price: ₹ {round(prediction, 2)}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            columns=columns,
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
