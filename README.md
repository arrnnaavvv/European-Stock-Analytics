# 🇪🇺 European Stock Analytics & Valuation Dashboard

An interactive financial analytics dashboard that compares six major European companies across **growth, profitability, valuation, stock performance, and risk** to identify which company offers the strongest overall investment profile.

🔗 **Live Dashboard:** https://european-stock-analytics-e5pshhew83s6tel9jbudyj.streamlit.app/

---

## 📊 Project Overview

### Core Question

> **Which European company offers the best combination of growth, profitability, valuation and risk?**

The project uses a quantitative multi-factor framework to compare:

- ASML
- SAP
- LVMH
- Siemens
- Novo Nordisk
- Accenture

The analysis combines fundamental financial data with historical stock-market performance and valuation metrics.

---

## 🏢 Companies Analysed

| Company | Country | Industry |
|---|---|---|
| ASML | Netherlands | Semiconductors |
| SAP | Germany | Software |
| LVMH | France | Luxury |
| Siemens | Germany | Industrials |
| Novo Nordisk | Denmark | Healthcare |
| Accenture | Ireland | Technology & Consulting |

---

## 📐 Analytical Framework

Each company receives a score from **0–100** across four dimensions.

### 1. Growth — 25%

Measured using:

- 2021–2025 Revenue CAGR

### 2. Profitability — 25%

Measured using:

- EBITDA Margin
- Net Margin
- ROE

### 3. Valuation — 25%

Measured using:

- Trailing P/E
- EV / EBITDA

Lower valuation multiples receive higher scores.

### 4. Risk — 25%

Measured using:

- Annualized Volatility
- Maximum Drawdown
- Beta vs S&P 500

Lower risk receives a higher score.

### Final Score

The overall score is calculated as:

**Final Score = 25% Growth + 25% Profitability + 25% Valuation + 25% Risk**

---

## 🏆 Final Ranking

Based on the quantitative scoring model:

| Rank | Company |
|---:|---|
| 1 | Novo Nordisk |
| 2 | SAP |
| 3 | Accenture |
| 4 | LVMH |
| 5 | ASML |
| 6 | Siemens |

The ranking represents the output of the project's quantitative screening framework and should not be interpreted as personalized investment advice.

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- Overall investment ranking
- Growth and profitability comparison
- 1-year, 3-year and 5-year stock returns
- P/E and EV/EBITDA valuation comparison
- Annualized volatility analysis
- Beta comparison
- Company-level deep dives
- Interactive company selection
- Four-factor investment scoring
- Methodology and assumptions

---

## 🛠️ Technology Stack

**Programming & Analytics**
- Python
- Pandas
- NumPy
- Matplotlib

**Financial Analysis**
- Financial statement analysis
- Equity valuation
- Ratio analysis
- Risk analysis
- Quantitative scoring

**Dashboard & Deployment**
- Streamlit
- GitHub
- Streamlit Community Cloud

**Data Storage**
- Excel
- CSV

---

## 📁 Project Structure

```text
European-Stock-Analytics/
│
├── app.py
├── requirements.txt
│
└── data/
    ├── financial_data.xlsx
    ├── final_investment_ranking.csv
    ├── financial_summary.csv
    ├── risk_summary.csv
    ├── stock_returns.csv
    └── valuation_table.csv
