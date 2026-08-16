# Livestock Products Price Analytics Dashboard

Try Live Demo: https://livestock-appucts-price-analytics-q5q2sqm68fparunfxxehcf.streamlit.app/

---

PROBLEM STATEMENT

Indonesian farmers and SMEs struggle with unpredictable livestock prices, making it difficult to plan inventory purchases, set competitive pricing, and manage business risk. This dashboard provides historical price stability analysis to help stakeholders understand price patterns and make better business decisions.

---

FEATURES

1. Trend Visualization - See price movements across years
2. Price Stability Analysis - Coefficient of Variation (CV) categorization
3. Multi-Year Comparison - Compare price trends year-over-year
4. Interactive Filters - Filter by commodity and year
5. Statistical Metrics - Mean, median, and standard deviation calculations

---

UNDERSTANDING PRICE STABILITY

Price volatility is measured using Coefficient of Variation (CV):

CV less than or equal to 10% - Very Stable. Safe for business planning.
10% less than CV less than or equal to 25% - Moderate Fluctuation. Requires attention.
CV greater than 25% - Highly Volatile. Risky for small businesses.

This helps farmers and SMEs understand whether prices are safe for planning or too unpredictable.

---

DATA

Dataset: Historical livestock price data from BPN (Badan Pangan Nasional)
Time Period: 2019-2024
Update Frequency: As new BPN data becomes available

While this project uses historical data, the analysis framework can be applied to real-time data streams for live price monitoring.

---

TECH STACK

Python - Core programming language
Streamlit - Web app framework
Pandas - Data processing and analysis
Plotly - Interactive visualizations
NumPy - Statistical calculations

---

GETTING STARTED

Prerequisites: Python 3.8 or higher, pip (Python package manager)

Installation:

1. Clone the repository:
git clone https://github.com/altairrayyan/Livestock-Products-Price-Analytics
cd Livestock-Products-Price-Analytics

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
python -m streamlit run ep1.py

The app will open at http://localhost:8501 in your browser.

---

PROJECT STRUCTURE

ep1.py - Entry point and page navigation
PersProject.py - Main dashboard page
perbandingan.py - Year-over-year comparison charts
BPNCSV.csv - Livestock price dataset from BPN
requirements.txt - Python dependencies
ERD.png - Application flowchart
README.md - This file

---

HOW IT WORKS

1. Load Data: Read livestock price data from BPN CSV
2. Process Data: Clean price values and handle currency formatting
3. Calculate Stability: Compute CV for each commodity and year
4. Visualize: Create interactive charts with Plotly
5. Filter: Allow users to explore by commodity and year

---

KEY INSIGHTS

Different livestock commodities show different price stability patterns.
Some commodities are more suitable for UMKM planning than others.
Historical price trends help predict future volatility.
Seasonal patterns affect price stability across years.

---

DATA SOURCE

BPN (Badan Pangan Nasional) - Indonesian Food Security Agency

This project uses publicly available livestock price data to help improve food security awareness in Indonesia.

---

LEARNING BACKGROUND

This project is informed by statistical research on agricultural data distribution and demonstrates the practical application of the Coefficient of Variation in real-world scenarios.

---

Built by: Muhammad Altair Rayyan Kamajaya
Created: July 2026
Portfolio Project
