# 📊 Kenny Vang - Data Science Portfolio

Welcome to my Data Science Portfolio! This repository contains a collection of projects demonstrating my skills in statistical analysis, data cleaning, hypothesis testing, interactive visualization, and machine learning.

**🔗 [View the Live Interactive Portfolio Here!](https://kennyvang.github.io/Data_Science_Portfolio-W.I.P/)** *(Note: Update this link if your repository name changes)*

---

## 📂 Featured Projects

### 1. Life Expectancy Analysis 🌍
- **Description:** An interactive dashboard and comprehensive statistical report analyzing global life expectancy using WHO data.
- **Highlights:** Dynamic Plotly scatter plots and comprehensive correlations between factors like GDP, Schooling, and Life Expectancy.
- **Tech Stack:** Pandas, Numpy, Plotly.

### 2. Liver Disease Predictor 🩺
- **Description:** A client-side machine learning application that predicts the risk of liver disease based on patient health metrics.
- **Highlights:** Employs a Random Forest Classifier trained on the Indian Liver Patient Dataset (ILPD). Includes dynamic heuristics that diagnose user inputs in real-time. Built entirely with Shinylive (Python running entirely in the browser!).
- **Tech Stack:** Scikit-Learn, Shiny for Python (Shinylive), Plotly.

---

## 🛠️ Built With
- **[Quarto](https://quarto.org/)**: An open-source scientific and technical publishing system built on Pandoc. Used to generate this entire portfolio website.
- **[Python](https://www.python.org/)**: Core data analysis and machine learning.
- **[Shinylive](https://shiny.posit.co/py/docs/shinylive.html)**: Serverless interactive web applications in Python. Allows the machine learning model to execute directly in the user's web browser without a backend server!
- **[Plotly](https://plotly.com/python/)**: Interactive graphing library.

---

## 🚀 How to View & Run

**You DO NOT need to download or install anything to view this portfolio!** 
Simply [click here to view the live interactive website](https://kennyvang.github.io/Data_Science_Portfolio-W.I.P/) directly in your browser. Thanks to Quarto and Shinylive, all Python machine learning models and visualizations compile into WebAssembly and execute entirely on the client-side.

### For Developers (Running the source code locally)
If you want to clone this repository, dig into the code, and run the development environment on your own local machine, follow these steps:

### Prerequisites
1. **Python 3.9+**
2. **Quarto CLI** (Download from [here](https://quarto.org/docs/get-started/))

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/kennyvang/Data_Science_Portfolio-W.I.P.git
   cd Data_Science_Portfolio-W.I.P
   ```

2. **Install the required Python packages:**
   ```bash
   pip install jupyter shiny plotly pandas scikit-learn
   ```

3. **Install the Quarto Shinylive Extension:**
   ```bash
   quarto add quarto-ext/shinylive
   ```

### Running the App
To preview the website locally with live-reloading:
```bash
quarto preview
```
This will open a local web server (typically on `http://localhost:4200`) where you can interact with the apps and view the Quarto documents!

### Building for Production
To render all the HTML files for deployment (outputs to the `/docs` folder):
```bash
quarto render
```
