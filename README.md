# AI SMS Spam Detection Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/XGBoost-181717?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
</div>

## 📌 Overview

The **AI SMS Spam Detection Dashboard** is an advanced MVT-based Django application that leverages machine learning (XGBoost/DistilBERT) to instantly classify SMS messages as `Spam` or `Ham`. It functions as a complete platform, featuring real-time analysis, rigorous data privacy through isolated user profiles, and an active learning feedback loop to continually improve analytical models.

---

## 🚀 Features

- **Real-Time Classification**: Instant identification of incoming SMS text messages using trained machine learning models.
- **Robust Machine Learning**: Incorporates standard ML capabilities using Scikit-Learn and XGBoost, with configurable support for DistilBERT embeddings.
- **Data Isolation**: Ensures complete data privacy by isolating prediction and feedback histories per user account.
- **Active Learning Mechanism**: Employs a continuous feedback loop where user corrections train and improve the models.
- **Interactive Dashboard**: A clean, professionally aesthetic layout showcasing system metrics, past searches, and spam distribution.
- **Secure Authentication System**: Complete user registration, login, logout functionalities with CSRF protections and password security. 

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Django 4.x
- **Database**: MySQL Server (Configured via `mysqlclient`)
- **Machine Learning**: XGBoost, Scikit-Learn, Joblib, Numpy (Transformers/Torch optional)
- **Frontend**: HTML5, Vanilla CSS, JS

---

## 🏗 Architecture

The system operates strictly across three tiers adhering to the MVT framework:
1. **Model**: Schema setups for MySQL using Django's ORM, capturing user datasets and their input patterns.
2. **View**: Handles predictive analysis loops (`model_app`) and user isolation protocols (`profile_system`).
3. **Template**: Fully decoupled frontend layer rendering model insights and interactive elements seamlessly.

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-sms-spam-detection.git
cd ai-sms-spam-detection
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the example environment file and update it with your own credentials:
```bash
cp .env.example .env
```
*(Ensure you map the `DB_*` variables in `.env` to your local MySQL database).*

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Local Server
```bash
python manage.py runserver
```
Visit the application at: `http://127.0.0.1:8000`

---

## 📸 Screenshots

*(Add screenshots of your application here to improve your repository's presentation)*

![Landing Page](screenshots/landing_page_demo.png) *(Placeholder)*
![Dashboard Insights](screenshots/dashboard_demo.png) *(Placeholder)*

---

## 🔮 Future Scope

- **Deep Learning Model Scaling**: Fine-tuning transformer models on diverse multi-lingual SMS datasets.
- **RESTful API Endpoint creation**: Decoupling the backend to serve inferences via API for mobile apps.
- **Advanced Threat Detection**: Upgrading keyword-based rules with behavioral mapping for phishing attacks.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Author

**Your Name**  
- [LinkedIn Profile](https://linkedin.com/in/yourusername)  
- [GitHub Profile](https://github.com/yourusername)  
- **Email**: your.email@example.com
