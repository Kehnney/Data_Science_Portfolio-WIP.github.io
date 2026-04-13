import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import os

# --- Page Config ---
st.set_page_config(
    page_title="Data Science Portfolio | Kenny Vang",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Define File Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIFE_EXP_DATA_PATH = os.path.join(BASE_DIR, "LifeExpectancy_Analysis_Project", "data", "Life-Expectancy-Data-Updated.csv")
LIVER_DIS_DATA_PATH = os.path.join(BASE_DIR, "LiverDisease_Analysis_Project", "data", "ILPD.csv")

# --- Caching Data Loading ---
@st.cache_data
def load_life_expectancy_data():
    try:
        df = pd.read_csv(LIFE_EXP_DATA_PATH)
        return df
    except FileNotFoundError:
        st.error(f"Cannot find data at {LIFE_EXP_DATA_PATH}")
        return pd.DataFrame()

@st.cache_data
def load_liver_disease_data():
    try:
        df = pd.read_csv(LIVER_DIS_DATA_PATH)
        # Preprocessing categorical 'Gender' based on sample
        if 'Gender' in df.columns:
            df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
        # Handle nan
        df = df.dropna()
        return df
    except FileNotFoundError:
        st.error(f"Cannot find data at {LIVER_DIS_DATA_PATH}")
        return pd.DataFrame()

# --- Fake Model Training / Caching ---
@st.cache_resource
def train_liver_model(df):
    if df.empty:
        return None
    # Assuming 'Selector' is the target variable (1=Disease, 2=No Disease or similar)
    features = [c for c in df.columns if c != 'Selector']
    X = df[features]
    y = df['Selector']
    model = RandomForestClassifier(n_estimators=100, max_depth=5, class_weight='balanced', random_state=42)
    model.fit(X, y)
    return model, features

# --- Sidebar ---
st.sidebar.title("Data Science Portfolio")

st.sidebar.markdown("---")
st.sidebar.subheader("Contact Information")
st.sidebar.markdown("**Kenny Vang**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/Kehnney)")

st.sidebar.markdown("---")
st.sidebar.info("🎓 UCSB Data Science Portfolio - Work in Progress (W.I.P).")


# --- Main Content / Tabs ---
tab_home, tab_life, tab_liver = st.tabs(['🏠 Home', '🌍 Life Expectancy', '🩺 Liver Disease'])


with tab_home:
    st.title("Welcome to My Data Science Portfolio 🚀")
    st.markdown("""
    Hello! I'm Kenny Vang, a student at UCSB. This dashboard showcases some of my recent data science projects.
    
    ### Available Projects:
    - **Life Expectancy Dashboard**: Interactive data exploration of global life expectancy and various socioeconomic factors.
    - **Liver Disease Predictor**: A machine learning application predicting liver disease likelihood using patient health metrics.
    
    Please click on the tabs above to explore the projects!
    """)

with tab_life:
    st.title("Life Expectancy Analysis 🌍")
    df_life = load_life_expectancy_data()
    
    if not df_life.empty:
        st.markdown("Explore the factors influencing life expectancy across different countries and years.")
        
        # 1. Plotly Scatter Plot
        st.subheader("Interactive Feature Explorer")
        numeric_cols = df_life.select_dtypes(include=np.number).columns.tolist()
        
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("Select X-Axis", numeric_cols, index=numeric_cols.index('GDP per capita') if 'GDP per capita' in numeric_cols else 0)
        with col2:
            y_axis = st.selectbox("Select Y-Axis", numeric_cols, index=numeric_cols.index('Schooling') if 'Schooling' in numeric_cols else 1)
            
        fig = px.scatter(df_life, x=x_axis, y=y_axis, hover_data=['Country', 'Year'] if 'Country' in df_life.columns else None,
                         opacity=0.6, color='Economy Status - Developed' if 'Economy Status - Developed' in df_life.columns else None,
                         title=f"{y_axis} vs. {x_axis}")
        st.plotly_chart(fig, use_container_width=True)
        
        # 2. Seaborn Correlation Heatmap
        st.subheader("Correlation Heatmap")
        st.markdown("Analyze how different socioeconomic and health factors correlate with each other.")
        
        # Calculate correlation matrix
        corr = df_life[numeric_cols].corr()
        
        # Plot using matplotlib/seaborn
        fig_heat, ax_heat = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=False, cmap='coolwarm', ax=ax_heat, fmt=".2f", linewidths=.5)
        st.pyplot(fig_heat)

with tab_liver:
    st.title("Liver Disease Prediction 🩺")
    st.markdown("Use the sliders to perform a 'What-If' analysis and predict the likelihood of liver disease based on health metrics.")
    
    # Educational part
    st.info("""
    **Understanding Liver Disease Risk Factors:**
    - **Bilirubin (TB & DB)**: High levels cause jaundice (yellowing of skin/eyes) and indicate poor liver function.
    - **Enzymes (Alkphos, SGPT, SGOT)**: Elevated levels mean liver cells are damaged, leaking these enzymes into the blood. Very high levels are a primary indicator of liver disease.
    - **Proteins (TP, ALB, A/G Ratio)**: The liver manufactures albumin. Low protein levels and a low A/G ratio indicate the liver isn't producing proteins effectively.
    """)
    
    df_liver = load_liver_disease_data()
    
    if not df_liver.empty:
        model_data = train_liver_model(df_liver)
        
        if model_data:
            model, features = model_data
            
            st.subheader("Patient Health Metrics")
            
            # Presets
            preset = st.selectbox("🧪 Choose a Patient Profile (Preset):", ["Custom", "Healthy Adult", "High-Risk Patient"])
            
            preset_dict = {
                "Healthy Adult": {
                    "Age": 32, "Gender": 0, "TB": 0.8, "DB": 0.2, "Alkphos": 160.0, 
                    "Sgpt": 22.0, "Sgot": 25.0, "TP": 7.5, "ALB": 4.0, "A/G Ratio": 1.2
                },
                "High-Risk Patient": {
                    "Age": 65, "Gender": 1, "TB": 7.5, "DB": 3.8, "Alkphos": 480.0, 
                    "Sgpt": 85.0, "Sgot": 110.0, "TP": 5.8, "ALB": 2.4, "A/G Ratio": 0.6
                }
            }
            
            # Create user inputs dynamically based on features
            user_input = {}
            cols = st.columns(3)
            
            # Categorize features for better layout
            for i, feature in enumerate(features):
                with cols[i % 3]:
                    # Determine step/type based on the data
                    min_val = float(df_liver[feature].min())
                    max_val = float(df_liver[feature].max())
                    mean_val = float(df_liver[feature].mean())
                    
                    # Set default value based on preset or mean
                    if preset != "Custom" and feature in preset_dict[preset]:
                        default_val = float(preset_dict[preset][feature])
                    else:
                        default_val = mean_val
                    
                    if feature == 'Gender':
                        user_input[feature] = st.selectbox(f"{feature} (1=Male, 0=Female)", [1, 0], index=0 if default_val==1 else 1)
                    elif df_liver[feature].dtype == int:
                        user_input[feature] = st.slider(f"{feature}", int(min_val), int(max_val), int(default_val))
                    else:
                        user_input[feature] = st.slider(f"{feature}", min_val, max_val, float(default_val))

            # Predict
            st.markdown("---")
            if st.button("Predict 📊", type="primary"):
                input_df = pd.DataFrame([user_input])
                prediction = model.predict(input_df)[0]
                proba = model.predict_proba(input_df)[0]
                
                # Based on ILPD dataset, 1 usually means liver disease, 2 means no disease.
                st.subheader("Prediction Result:")
                
                if prediction == 1:
                    st.error(f"⚠️ High Likelihood of Liver Disease (Confidence: {proba[0] if len(proba)>1 else 1.0:.2%})")
                else:
                    st.success(f"✅ Low Likelihood of Liver Disease")
