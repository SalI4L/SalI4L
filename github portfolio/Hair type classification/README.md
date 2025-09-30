# Hair Type Classification

## 📌 Project Overview  
This project develops an **image classification model** that categorizes hair textures into four main types:  
- **Straight**  
- **Wavy**  
- **Curly**  
- **Kinky**  

The model is designed to help consumers accurately identify their hair type, enabling **personalized recommendations** for hair care products, treatments, and daily routines. Beyond consumer use, the project explores the role of AI in the beauty industry and raises awareness about **fairness and inclusivity** in machine learning systems.

---

## 🎯 Objectives
1. Build a deep learning model for hair type classification.  
2. Provide an accessible demo for non-technical users.  
3. Address **bias and fairness issues** in datasets and models.  
4. Document the process in line with **CRISP-DM methodology**:  
   - Business Understanding  
   - Data Understanding & Preparation  
   - Modeling  
   - Evaluation  
   - Deployment & Communication  

---

## 📂 Project Structure
```
Hair type classification/
│── CreativeBrief_Sally_Ibrahim_211066.ipynb   # Main notebook (business understanding, data, modeling)
│── Hair-texture-classifier-Demo.mp4           # Demo video of the classifier
│── Group-Fairness InfoGraphic.pdf             # Ethical/fairness considerations
│── Project Proposal.pptx                      # Initial project proposal & plan
│── certificates/                              # Certificates of completed ML courses
│     └── image-modeling-with-keras-certificate.pdf
```

---

## 🛠️ Technologies & Dependencies
- **Python 3.x**
- **TensorFlow / Keras** (deep learning framework)  
- **NumPy, Pandas** (data handling)  
- **Matplotlib, Seaborn** (visualization)  
- **scikit-learn** (evaluation metrics, preprocessing)  
- **Jupyter Notebook** (development environment)

*(You can install dependencies via `pip install -r requirements.txt` if provided.)*

---

## 📊 Dataset
- Images of different hair textures collected from publicly available sources.  
- Classes: *straight, wavy, curly, kinky*.  
- Preprocessing steps include resizing, normalization, and augmentation to improve generalization.  
- Dataset split: **training, validation, and test sets**.  

⚠️ **Note on Bias:** Hair type datasets often underrepresent certain textures (especially kinky/coily hair). This project emphasizes **fair data collection** and highlights the risks of biased predictions.

---

## 🤖 Model Development
- Implemented using **Convolutional Neural Networks (CNNs)** in Keras.  
- Data augmentation applied (rotation, flipping, zooming) to increase robustness.  
- Optimized with techniques like **dropout** and **batch normalization** to avoid overfitting.  
- Evaluation based on **accuracy, confusion matrix, and fairness metrics**.  

---

## 🚀 Usage
1. Clone the repository and navigate to the project folder.  
2. Open the notebook:  
   ```bash
   jupyter notebook CreativeBrief_Sally_Ibrahim_211066.ipynb
   ```
3. Run all cells to reproduce training and evaluation.  
4. Test with your own images by adding them to the input directory and updating the notebook code.  

---

## 📹 Demo
A short **video demo** (`Hair-texture-classifier-Demo.mp4`) illustrates how the trained model can classify input images and return hair type predictions.

---

## ⚖️ Fairness & Ethics
- The project explicitly addresses **group fairness** in AI.  
- A dedicated infographic (`Group-Fairness InfoGraphic.pdf`) explains the risks of bias in beauty-related AI applications.  
- Special focus is given to inclusivity, ensuring that **all hair textures are equally represented and respected**.  

---

## 📈 Results
- Model achieves promising accuracy in distinguishing between the four classes.  
- Some challenges remain in separating visually similar textures (e.g., wavy vs. curly).  
- Demonstrates the feasibility of AI-powered **personalized beauty tech**.  

---

## 🔮 Future Work
- Improve dataset size and diversity, especially for underrepresented hair textures.  
- Deploy as a **web or mobile application** for real-world use.  
- Integrate product recommendation systems tailored to predicted hair type.  
- Conduct user studies to evaluate **usability and fairness** in practice.  

---

## 👩‍💻 Author
**Sally Ibrahim**  
Data Science student at Breda University of Applied Sciences  
