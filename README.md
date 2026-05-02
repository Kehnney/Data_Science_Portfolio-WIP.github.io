# 📊 Kenny Vang - Data Science Portfolio

Welcome to my data science portfolio. This repository is a Quarto website that showcases two projects using statistical analysis, data cleaning, hypothesis testing, interactive visualization, and machine learning.

**🔗 [View the Live Interactive Portfolio Here!](https://Kehnney.github.io/Data_Science_Portfolio-WIP.github.io/)**

---

## 📂 Featured Projects

### 1. Life Expectancy Analysis 🌍
- **Description:** An interactive dashboard and comprehensive statistical report analyzing global life expectancy using WHO data.
- **Highlights:** Dynamic Plotly scatter plots and comprehensive correlations between factors like GDP, Schooling, and Life Expectancy.
- **Tech Stack:** Pandas, Numpy, Plotly.

### 2. Liver Disease Predictor 🩺
- **Description:** A client-side machine learning application that predicts the risk of liver disease based on patient health metrics.
- **Highlights:** Employs a Random Forest Classifier trained on the Indian Liver Patient Dataset (ILPD). Includes dynamic heuristics that diagnose user inputs in real-time. Built with Shiny for Python running through Shinylive in the browser.
- **Tech Stack:** Scikit-Learn, Shiny for Python (Shinylive), Plotly.

---

## 🛠️ Built With
- **[Quarto](https://quarto.org/)**: An open-source scientific and technical publishing system built on Pandoc. Used to generate this entire portfolio website.
- **[Python](https://www.python.org/)**: Core data analysis and machine learning.
- **[Shinylive](https://shiny.posit.co/py/docs/shinylive.html)**: Runs the Shiny app directly in the browser without a backend server.
- **[Plotly](https://plotly.com/python/)**: Interactive graphing library.

---

## 🚀 How to View & Run

**You DO NOT need to download or install anything to view this portfolio!** 
Simply [click here to view the live interactive website](https://Kehnney.github.io/Data_Science_Portfolio-WIP.github.io/) directly in your browser. Thanks to Quarto and Shinylive, the interactive Python content executes directly in the client-side browser environment.

### For Developers (Running the source code locally)
If you want to clone this repository, dig into the code, and run the development environment on your own local machine, follow these steps:

### Prerequisites
1. **Python 3.9+**
2. **Quarto CLI** (Download from [here](https://quarto.org/docs/get-started/))

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kehnney/Data_Science_Portfolio-WIP.github.io.git
   cd Data_Science_Portfolio-WIP.github.io
   ```

2. **Install the required Python packages:**
   ```bash
   pip install jupyter shiny plotly pandas scikit-learn
   ```

3. **Install the Quarto Shinylive Extension:**
   ```bash
   quarto add quarto-ext/shinylive
   ```

### Running the Site
To preview the website locally with live-reloading:
```bash
quarto preview
```
This will open a local web server (typically on `http://localhost:4200`) where you can interact with the Quarto pages and the embedded Shinylive content.

### Building for Production
To render all the HTML files for deployment (outputs to the `/docs` folder):
```bash
quarto render
```
