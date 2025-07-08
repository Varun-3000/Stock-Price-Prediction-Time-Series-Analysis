import streamlit as st
import pandas as pd
from model_train import *
from datetime import datetime, timedelta

st.title("📈 30-Day Stock Price Forecast")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", value="AAPL")

if ticker:
    try:
        with st.spinner("Fetching and forecasting..."):
            # Step 1: Get data
            data = get_data(ticker.upper())
            close_series = data['Close']

            # Step 2: Get differencing order
            d_order = get_differencing_order(close_series)

            # Step 3: Fit model and forecast
            predictions = fit_model(close_series, d_order)

            # Step 4: Build forecast index and DataFrame
            start_date = datetime.now().strftime('%Y-%m-%d')
            end_date = (datetime.now() + timedelta(days=29)).strftime('%Y-%m-%d')
            forecast_index = pd.date_range(start=start_date, end=end_date, freq='D')
            forecast_df = pd.DataFrame(predictions.values, index=forecast_index, columns=['Predicted Close'])

        # Display forecast
        st.subheader(f"📅 Forecast for {ticker.upper()} (Next 30 Days)")
        st.dataframe(forecast_df.style.format({"Predicted Close": "{:.2f}"}))

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
