import streamlit as st
import pickle

st.title('Welcome to my ML app!')
st.image('image.png')
#Load the pretrained model
with open('titanicpickle.pkl', 'rb') as pickle_file:
    pickle_file_load = pickle.load(pickle_file)

#Function that makes the prediction
def PredictionFunction(Pclass, Sex, Age,SibSp, Parch, Fare, Embarked):
    prediction = pickle_file_load.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction)
    return prediction


def main():
    st.title('Titanic Prediction App!')
    Pclass = st.text_input('Passenger Class') #1
    Sex = st.text_input('Sex') #0
    Age = st.text_input('Age')#23
    SibSp = st.text_input('Sib/Sp')
    Parch = st.text_input('Par/Child')
    Fare = st.text_input('Fare')
    Embarked = st.text_input('Embarked')
    result = ''

    if st.button('Predict'):
        #Convert the inputs to appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)
        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f'The output is: {result}')

main()