# Stock Price Prediction – Time Series Analysis
This project forecasts the next 30 days of stock closing prices using ARIMA modeling. 
The application fetches historical stock data using yFinance, trains an ARIMA model based on stationarity checks and differencing, and visualizes the forecast in a clean Streamlit web interface.

## Setup Instructions
1. Clone the repository

```bash
git clone https://github.com/your-username/Stock-Price-Prediction-Time-Series-Analysis.git
cd Stock-Price-Prediction-Time-Series-Analysis
```

2.  Create & activate virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the app
```bash
streamlit run app.py
```

### Final Output
![image](https://github.com/user-attachments/assets/b2dad225-092c-4b05-a261-09811a1cd374)


