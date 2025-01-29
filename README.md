# Sentiment Analyzer API and Dashboard

This project is a **Sentiment Analysis Web Application** built using **Flask**, **TextBlob**, and **Streamlit**. It consists of three key components:

## Components

### 1. **Flask API (`app.py`)**
A simple API that processes POST requests to analyze the sentiment of the provided text using the `analyze_sentiment` function from `sentiment_analysis.py`.

### 2. **Sentiment Analysis Module (`sentiment_analysis.py`)**
Uses **TextBlob** to determine the sentiment polarity, categorizing text as **Positive**, **Negative**, or **Neutral** based on polarity scores.

### 3. **Streamlit Dashboard (`dashboard.py`)**
Provides a user-friendly interface for inputting text and viewing sentiment analysis results. It communicates with the Flask API for real-time sentiment evaluation.


This project provides a comprehensive sentiment analysis application using Flask and Streamlit. The application includes an API to process text and analyze its sentiment using the TextBlob library. Additionally, a user-friendly dashboard is provided for interactive analysis.

## Project Structure
```
.
├── app.py                  # Flask API for sentiment analysis
├── sentiment_analysis.py    # Sentiment analysis logic using TextBlob
└── dashboard/
    └── dashboard.py         # Streamlit dashboard for user interaction
```

## Features
- Analyze text sentiment as **Positive**, **Neutral**, or **Negative**.
- Display polarity scores for the analyzed text on a scale of -1 to 1.
- User-friendly interface using Streamlit for easy interaction.

## Setup and Installation

### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/aryaman-0011/Sentyy.git
cd Sentyy
```

### Install Dependencies
```bash
pip install -r requirements.txt
```


### Start the API
```bash
python app.py
```
The Flask API will be available at `http://127.0.0.1:5000`.

### Run the Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```
The dashboard will open in your web browser.

## Usage
### API
#### Analyze Sentiment (POST)
**Endpoint:** `/analyze`

**Request:**
```json
{
  "text": "I love this project!"
}
```

**Response:**
```json
{
  "text": "I love this project!",
  "sentiment": {
    "polarity": 0.5,
    "sentiment": "Positive"
  }
}
```

### Dashboard
1. Open the Streamlit dashboard in your browser.
2. Enter text in the provided text area.
3. Click the **Analyze** button.
4. View the sentiment result and polarity score.

## Example Screenshot
![Screenshot (1)](https://github.com/user-attachments/assets/d8041f20-0d10-4dbb-8b3b-6bae76e297fd)

## Error Handling
- If no text is provided to the API, it returns:
  ```json
  {
    "error": "No text provided"
  }
  ```
- The dashboard provides warnings to guide users in providing valid input.

## Contributing
We welcome contributions! Feel free to open issues or submit pull requests for improvements and suggestions.


---

Happy Coding! 🚀

