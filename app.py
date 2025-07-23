import pandas as pd
import plotly.express as px
import streamlit as st
from prophet import Prophet
from typing import List

# Set up Streamlit layout
st.set_page_config(page_title="Sales Forecast Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(
        r"D:\Project\sales_forecast_dashboard\Sample_ Superstore.csv",
        parse_dates=['Order Date'],
        encoding='cp1252'
    )
    df = df[['Order Date', 'Sales', 'Profit', 'Region']].dropna()
    return pd.DataFrame(df)

# Load data
df = load_data()

# Page Title
st.title("📊 Sales Forecasting Dashboard - Superstore")

# Region Filter
if 'Region' in df.columns:
    regions: List[str] = df['Region'].dropna().unique().tolist()
    selected_region = st.selectbox("Select Region", regions)

    # Filtered DataFrame for selected region
    region_df = df[df['Region'] == selected_region].copy()

    # Aggregate daily sales (ensure result is DataFrame)
    daily_sales = (
        region_df.groupby('Order Date', as_index=False)['Sales']
        .sum()
        .reset_index(drop=True)
    )
    if not isinstance(daily_sales, pd.DataFrame):
        daily_sales = pd.DataFrame(daily_sales)

    # Plot historical sales
    fig1 = px.line(
        daily_sales,
        x='Order Date',
        y='Sales',
        title=f"📈 Historical Sales - {selected_region}"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Prepare for Prophet model
    df_prophet = daily_sales.rename(columns={"Order Date": "ds", "Sales": "y"})
    if not isinstance(df_prophet, pd.DataFrame):
        df_prophet = pd.DataFrame(df_prophet)

    # Build and train Prophet model
    model = Prophet()
    model.fit(df_prophet)

    # Forecast for next 90 days
    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)

    # Plot forecast
    fig2 = model.plot(forecast)
    st.write(f"### 🔮 Forecasted Sales for Next 90 Days - {selected_region}")
    st.pyplot(fig2)

    # Region-wise profit
    region_profit_raw = df.groupby('Region', as_index=False)['Profit'].sum()
    region_profit = (
        region_profit_raw
        if isinstance(region_profit_raw, pd.DataFrame)
        else pd.DataFrame(region_profit_raw)
    ).sort_values(by='Profit', ascending=False)

    # Profit Bar Chart
    fig3 = px.bar(
        region_profit,
        x='Region',
        y='Profit',
        title="💰 Total Profit by Region",
        color='Profit',
        text='Profit'
    )
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.error("❌ 'Region' column not found in the dataset.")