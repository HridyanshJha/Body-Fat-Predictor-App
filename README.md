# Body Fat Prediction

  This project uses machine learning to predict **body fat percentage** based on biometric data. The model is trained using a dataset of body measurements and serves predictions via a simple web application.

## 🗂 Project Structure

  📁 HridyanshJha/ ├── BODY FAT Prediction.ipynb # Jupyter Notebook with data exploration and model training ├── app.py # Flask web app to serve model predictions ├── bodyfat.csv # Dataset used for training ├── bodyfatmodel.pkl # Saved trained model └── requirements.txt # Python dependencies


## 🚀 How to Run

### 1. Clone the Repository

  ```bash
  git clone https://github.com/your-username/HridyanshJha.git
  cd HridyanshJha

  python -m venv venv
  source venv/bin/activate    # On Windows use `venv\Scripts\activate`

  pip install -r requirements.txt

  python app.py

### More Info
📊 Dataset
bodyfat.csv contains biometric attributes like weight, height, age, and body fat percentage.

The dataset is used to train a regression model predicting body fat %.

🧠 Machine Learning
Techniques: Regression using Scikit-learn

Notebook: BODY FAT Prediction.ipynb

Model file: bodyfatmodel.pkl (used in app.py)

🛠 Tech Stack
Python 3

Pandas, NumPy, Matplotlib, Scikit-learn

Flask (for deployment)

Pickle (for model serialization)

🔮 Future Enhancements
Add input validation and better user interface

Deploy on cloud platforms like Render or Heroku

Improve model accuracy and feature scaling

🤝 Contributing
Feel free to fork this repo, make improvements, and submit pull requests.

📄 License
This project is licensed under the MIT License.




