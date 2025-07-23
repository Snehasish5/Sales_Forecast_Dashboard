# Sales Forecast Dashboard - Superstore

📊 A **Sales Forecasting Dashboard** built with **Streamlit**, **Facebook Prophet**, and **Plotly** to visualize historical sales data and forecast future sales for different regions using the Superstore dataset.

---

## 🚀 Features

- Interactive dashboard built with **Streamlit**
- Historical sales visualization by region using **Plotly**
- Sales forecasting for the next 90 days using **Facebook Prophet**
- Region-wise total profit analysis with bar charts
- User-friendly interface with dynamic filtering by region

---

## 🛠️ Technologies Used

- Python 3.12.3
- [Streamlit](https://streamlit.io/) — Web app framework for data apps
- [Facebook Prophet](https://facebook.github.io/prophet/) — Time series forecasting
- [Plotly](https://plotly.com/python/) — Interactive plotting
- Pandas — Data manipulation

---

## 📁 Dataset

The project uses the **Superstore Sales dataset** (`Sample_ Superstore.csv`), which includes sales, profit, order date, and region information.

> **Note:** Make sure to place the dataset in the correct path or update the path in `app.py`.

---

## 🔧 How to Run Locally

1. **Clone the repository:**

   git clone https://github.com/yourusername/sales-forecast-dashboard.git

   cd sales-forecast-dashboard

Create and activate a virtual environment (recommended):

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Open your browser at http://localhost:8501

📦 Requirements
Include these in a requirements.txt:

streamlit
pandas
plotly
prophet

🧑‍💻 Project Structure

sales-forecast-dashboard/
│
├── app.py                 # Main Streamlit app script
├── Sample_ Superstore.csv # Dataset file
├── requirements.txt       # Python dependencies
└── README.md              # This file

🤝 Contributions
Feel free to fork the repo, create branches, and submit pull requests! Any contributions or suggestions are welcome.

📄 License
This project is licensed under the MIT License.