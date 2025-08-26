# Waste_Classification_App

# ♻️ Waste Classification Web App  

## 📖 Project Overview  
This project is a **Flask-based web application** that classifies waste images into categories (e.g., recyclable, non-recyclable, biodegradable, etc.) using a trained **deep learning model (`waste_model.h5`)**.  
The app also provides **recycling information** and allows users to **submit their address for waste pickup**, bridging AI with real-world sustainability.  

---

## 📂 Dataset  
- Images of different types of waste (plastic, glass, paper, organic, etc.)  
- Preprocessed by resizing, normalization, and augmentation  
- Split into **train, validation, and test sets**  

---

## ⚙️ Methodology  

### 🔹 Model Training  
- Built and trained a **Convolutional Neural Network (CNN)** on labeled waste images  
- Optimized with techniques such as dropout and batch normalization  
- Saved trained model as **`waste_model.h5`** for deployment  

### 🔹 Web Application (Flask)  
- **Frontend:** HTML, CSS for simple and clean user interface  
- **Backend:** Flask to handle requests and integrate ML model  
- **Features:**  
  - Upload an image of waste for classification  
  - Get **waste type + recycling info**  
  - Submit address for **pickup scheduling**  

### 🔹 Tech Stack  
- **Python, Flask**  
- **TensorFlow / Keras**  
- **HTML, CSS**  
- **Bootstrap (optional for styling)**  

---

## 📊 Results  
- Achieved strong accuracy on the test set with reliable predictions across waste categories  
- Provided meaningful **recycling guidelines** for each waste type  
- Integrated ML model into a fully functional **web application**  

---

## 🚀 Key Learnings  
- Applying **CNNs** to image classification tasks  
- Saving and reusing models (`.h5`) for deployment  
- Integrating **Flask backend** with an ML model  
- Building a user-friendly **web interface** for real-world use cases  

---

## 🔮 Future Improvements  
- Extend dataset with more waste categories  
- Deploy on cloud (Heroku, AWS, or GCP) for public access  
- Add user authentication and database for tracking submissions  
- Enhance model with **transfer learning (e.g., ResNet, MobileNet)** for higher accuracy  

---

## ▶️ How to Run  

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/waste-classification.git
   cd waste-classification
2. Install dependencies
 pip install -r requirements.txt
3. Run
 python app.py
