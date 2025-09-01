# 🚢 Titanic Survival Predictor

A modern, user-friendly Streamlit web application that predicts passenger survival on the Titanic using machine learning. This application provides an interactive interface for users to input passenger characteristics and receive survival predictions with confidence scores.

## ✨ Features

- **Interactive Web Interface**: Beautiful, responsive UI built with Streamlit
- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Robust error handling and user-friendly error messages
- **Confidence Scores**: Prediction confidence levels for better insights
- **Modern Design**: Clean, professional styling with custom CSS
- **Responsive Layout**: Optimized for different screen sizes
- **Logging**: Comprehensive logging for debugging and monitoring

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd spamapp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the required files**
   - `titanicapplication.py` - Main application file
   - `titanicpickle.pkl` - Pre-trained machine learning model
   - `image.png` - Titanic image (optional)
   - `requirements.txt` - Python dependencies

## 🚀 Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run titanicapplication.py
   ```

2. **Open your web browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL manually

### How to Use the App

1. **Read the Guidelines**: Click on "📖 Input Guidelines" to understand how to fill the form
2. **Enter Passenger Information**:
   - **Passenger Class**: Select from First, Second, or Third class
   - **Sex**: Choose Male or Female
   - **Age**: Enter age in years (0-120)
   - **Siblings/Spouses**: Number of siblings or spouses aboard (0+)
   - **Parents/Children**: Number of parents or children aboard (0+)
   - **Fare**: Passenger fare in pounds (0+)
   - **Port of Embarkation**: Choose from Southampton, Cherbourg, or Queenstown
3. **Make Prediction**: Click "🔮 Predict Survival" button
4. **View Results**: See the prediction result with confidence score and passenger details

## 📊 Input Format

The application expects the following input format for the machine learning model:

| Feature | Description | Valid Values |
|---------|-------------|--------------|
| Pclass | Passenger Class | 1 (First), 2 (Second), 3 (Third) |
| Sex | Gender | 0 (Male), 1 (Female) |
| Age | Age in years | 0-120 |
| SibSp | Siblings/Spouses aboard | 0+ |
| Parch | Parents/Children aboard | 0+ |
| Fare | Passenger fare | 0+ |
| Embarked | Port of embarkation | 0 (Southampton), 1 (Cherbourg), 2 (Queenstown) |

## 🏗️ Project Structure

```
spamapp/
├── titanicapplication.py    # Main application file
├── titanicpickle.pkl       # Pre-trained ML model
├── image.png              # Titanic image (optional)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Technical Details

### Architecture

The application follows a modular, object-oriented design:

- **TitanicPredictor Class**: Handles model loading, input validation, and predictions
- **UI Functions**: Separate functions for different UI components
- **Error Handling**: Comprehensive try-catch blocks and user feedback
- **Logging**: Structured logging for debugging and monitoring

### Key Improvements

1. **Input Validation**: Comprehensive validation for all user inputs
2. **Error Handling**: Graceful error handling with user-friendly messages
3. **User Experience**: Modern UI with better form controls and visual feedback
4. **Code Organization**: Modular, well-documented code structure
5. **Type Hints**: Full type annotations for better code maintainability
6. **Logging**: Structured logging for debugging and monitoring

### Dependencies

- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Typing-extensions**: Type hint support

## 🐛 Troubleshooting

### Common Issues

1. **Model file not found**
   - Ensure `titanicpickle.pkl` is in the same directory as the application
   - Check file permissions

2. **Dependencies not installed**
   - Run `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+

3. **Port already in use**
   - Streamlit will automatically use the next available port
   - Check the terminal output for the correct URL

4. **Image not displaying**
   - Ensure `image.png` is in the project directory
   - The app will work without the image

### Debug Mode

To run with debug information:
```bash
streamlit run titanicapplication.py --logger.level debug
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Titanic dataset for providing the training data
- Streamlit team for the excellent web framework
- Scikit-learn team for the machine learning tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the error messages in the terminal
3. Ensure all dependencies are properly installed
4. Verify the model file is present and accessible

---

**Built with ❤️ using Streamlit and Machine Learning** 