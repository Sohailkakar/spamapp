"""
Titanic Survival Prediction App
A simple Streamlit web application that predicts passenger survival on the Titanic
using a pre-trained machine learning model.

Author: Muhammad Sohail
"""

import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff7f0e;
    }
</style>
""", unsafe_allow_html=True)

def load_model():
    """Load the pre-trained model from pickle file."""
    try:
        with open('titanicpickle.pkl', 'rb') as pickle_file:
            model = pickle.load(pickle_file)
        return model
    except FileNotFoundError:
        st.error("Model file 'titanicpickle.pkl' not found!")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()

def validate_inputs(pclass, sex, age, sibsp, parch, fare, embarked):
    """Check if all inputs are valid."""
    # Check if all fields are filled
    if not all([pclass, sex, age, sibsp, parch, fare, embarked]):
        return False, "All fields are required. Please fill in all inputs."
    
    # Check if age is reasonable
    try:
        age_float = float(age)
        if age_float < 0 or age_float > 120:
            return False, "Age must be between 0 and 120."
    except:
        return False, "Age must be a valid number."
    
    # Check if fare is reasonable
    try:
        fare_float = float(fare)
        if fare_float < 0:
            return False, "Fare cannot be negative."
    except:
        return False, "Fare must be a valid number."
    
    return True, ""

def predict_survival(model, pclass, sex, age, sibsp, parch, fare, embarked):
    """Make survival prediction using the model."""
    try:
        # Prepare input features
        features = [[pclass, sex, age, sibsp, parch, fare, embarked]]
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get prediction probability if available
        try:
            confidence = model.predict_proba(features)[0]
            confidence_score = max(confidence)
        except:
            confidence_score = 0.8
        
        return prediction, confidence_score
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None, 0

def main():
    """Main application function."""
    
    # Display header
    st.markdown('<h1 class="main-header">Titanic Survival Predictor</h1>', unsafe_allow_html=True)
    
    # Display image if available
    try:
        st.image('image.png', use_column_width=True)
    except:
        st.info("Titanic image not found. Please add 'image.png' to the project directory.")
    
    # About section
    st.markdown("""
    <div class="info-box">
    <h3>About this App</h3>
    <p>This application predicts whether a passenger would have survived the Titanic disaster 
    based on their characteristics using a machine learning model trained on historical data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input guidelines
    with st.expander("Input Guidelines", expanded=False):
        st.markdown("""
        **How to fill in the form:**
        
        - **Passenger Class**: 1 (First), 2 (Second), or 3 (Third)
        - **Sex**: 0 (Male) or 1 (Female)
        - **Age**: Age in years (0-120)
        - **Siblings/Spouses**: Number of siblings or spouses aboard (0+)
        - **Parents/Children**: Number of parents or children aboard (0+)
        - **Fare**: Passenger fare in pounds (0+)
        - **Embarked**: Port of embarkation - 0 (Southampton), 1 (Cherbourg), 2 (Queenstown)
        """)
    
    # Load model
    model = load_model()
    
    # Create input form
    st.subheader("Passenger Information")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        pclass = st.selectbox(
            "Passenger Class",
            options=[1, 2, 3],
            format_func=lambda x: f"Class {x} ({'First' if x==1 else 'Second' if x==2 else 'Third'})"
        )
        sex = st.selectbox(
            "Sex",
            options=[0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female"
        )
        age = st.number_input("Age", min_value=0.0, max_value=120.0, value=30.0, step=0.1)
        sibsp = st.number_input("Siblings/Spouses", min_value=0, max_value=10, value=0, step=1)
    
    with col2:
        parch = st.number_input("Parents/Children", min_value=0, max_value=10, value=0, step=1)
        fare = st.number_input("Fare (£)", min_value=0.0, max_value=1000.0, value=50.0, step=0.1)
        embarked = st.selectbox(
            "Port of Embarkation",
            options=[0, 1, 2],
            format_func=lambda x: "Southampton" if x == 0 else "Cherbourg" if x == 1 else "Queenstown"
        )
    
    # Prediction button
    if st.button("Predict Survival", type="primary", use_container_width=True):
        with st.spinner("Analyzing passenger data..."):
            # Validate inputs
            is_valid, error_message = validate_inputs(pclass, sex, age, sibsp, parch, fare, embarked)
            
            if not is_valid:
                st.error(f"Validation Error: {error_message}")
                return
            
            # Make prediction
            prediction, confidence = predict_survival(model, pclass, sex, age, sibsp, parch, fare, embarked)
            
            if prediction is not None:
                # Display result
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                
                if prediction == 1:
                    st.success("**SURVIVED** - This passenger would likely have survived!")
                    st.balloons()
                else:
                    st.error("**DID NOT SURVIVE** - This passenger would likely not have survived.")
                
                # Display confidence
                confidence_percent = confidence * 100
                st.metric("Prediction Confidence", f"{confidence_percent:.1f}%")
                
                # Display input summary
                st.markdown("**Passenger Details:**")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"Class: {pclass}")
                    st.write(f"Sex: {'Male' if sex == 0 else 'Female'}")
                    st.write(f"Age: {age} years")
                    st.write(f"Siblings/Spouses: {sibsp}")
                
                with col2:
                    st.write(f"Parents/Children: {parch}")
                    st.write(f"Fare: £{fare}")
                    embarked_map = {0: 'Southampton', 1: 'Cherbourg', 2: 'Queenstown'}
                    st.write(f"Embarked: {embarked_map[embarked]}")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Add footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
    <p>Built with Streamlit and Machine Learning</p>
    <p>Data source: Titanic passenger dataset</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()