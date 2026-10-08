import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="European Stock Analytics",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
# Finds the data folder relative to app.py
base_path = Path(__file__).resolve().parent / "data"

final_score = pd.read_csv(
    base_path / "final_investment_ranking.csv"
)

financial_summary = pd.read_csv(
    base_path / "financial_summary.csv"
)

risk_summary = pd.read_csv(
    base_path / "risk_summary.csv"
)

valuation_table = pd.read_csv(
    base_path / "valuation_table.csv"
)

stock_returns = pd.read_csv(
    base_path / "stock_returns.csv"
)

# Convert stock return columns to numbers
for column in ["1Y Return", "3Y Return", "5Y Return"]:
    stock_returns[column] = pd.to_numeric(
        stock_returns[column],
        errors="coerce"
    )

# -----------------------------
# CALCULATE REVENUE CAGR
# -----------------------------
financial_file = base_path / "financial_data.xlsx"

company_sheets = [
    "ASML",
    "SAP",
    "LVMH",
    "Siemens",
    "Novo Nordisk",
    "Accenture"
]

growth_results = []

for company in company_sheets:

    df = pd.read_excel(
        financial_file,
        sheet_name=company
    )

    beginning_revenue = df.loc[
        df["Metric"] == "Revenue", 2021
    ].iloc[0]

    ending_revenue = df.loc[
        df["Metric"] == "Revenue", 2025
    ].iloc[0]

    cagr = (
        (ending_revenue / beginning_revenue) ** (1 / 4) - 1
    ) * 100

    growth_results.append({
        "Company": company,
        "Revenue CAGR": cagr
    })

growth_data = pd.DataFrame(growth_results)

# -----------------------------
# TITLE
# -----------------------------
st.title("🇪🇺 European Stock Analytics & Valuation Dashboard")

st.markdown(
    """
    ### Which European company offers the best combination of
    **growth, profitability, valuation and risk?**

    This dashboard compares six major European companies using
    a quantitative multi-factor scoring framework.
    """
)

st.divider()

# -----------------------------
# TOP METRICS
# -----------------------------
winner = final_score.iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🏆 Top Ranked Company",
    winner["Company"]
)

col2.metric(
    "Final Score",
    f"{winner['Final Score']:.1f}/100"
)

col3.metric(
    "Companies Analysed",
    len(final_score)
)

col4.metric(
    "Analysis Dimensions",
    "4"
)

st.divider()

# -----------------------------
# FINAL RANKING
# -----------------------------
st.header("🏆 Overall Investment Ranking")

ranking = final_score[
    [
        "Rank",
        "Company",
        "Growth Score",
        "Profitability Score",
        "Valuation Score",
        "Risk Score",
        "Final Score"
    ]
].copy()

st.dataframe(
    ranking.style.format({
        "Growth Score": "{:.1f}",
        "Profitability Score": "{:.1f}",
        "Valuation Score": "{:.1f}",
        "Risk Score": "{:.1f}",
        "Final Score": "{:.1f}"
    }),
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# OVERALL RANKING CHART
# -----------------------------
st.subheader("Overall Score")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    final_score["Company"],
    final_score["Final Score"]
)

ax.set_ylabel("Final Score / 100")
ax.set_xlabel("Company")
ax.set_ylim(0, 100)

plt.xticks(rotation=35)
plt.tight_layout()

st.pyplot(fig)

st.divider()

# -----------------------------
# STOCK PERFORMANCE
# -----------------------------
st.header("📈 Stock Performance")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("1-Year Return")

    data = stock_returns.sort_values(
        "1Y Return",
        ascending=False
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        data["Company"],
        data["1Y Return"]
    )

    ax.set_ylabel("Return (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("3-Year Return")

    data = stock_returns.sort_values(
        "3Y Return",
        ascending=False
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        data["Company"],
        data["3Y Return"]
    )

    ax.set_ylabel("Return (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

with col3:

    st.subheader("5-Year Return")

    data = stock_returns.sort_values(
        "5Y Return",
        ascending=False
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        data["Company"],
        data["5Y Return"]
    )

    ax.set_ylabel("Return (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

st.subheader("Historical Stock Returns")

st.dataframe(
    stock_returns.style.format({
        "1Y Return": "{:.1f}%",
        "3Y Return": "{:.1f}%",
        "5Y Return": "{:.1f}%"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------
# FUNDAMENTAL ANALYSIS
# -----------------------------
st.header("📊 Fundamental Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Revenue CAGR (2021–2025)")

    data = growth_data.sort_values(
        "Revenue CAGR",
        ascending=False
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        data["Company"],
        data["Revenue CAGR"]
    )

    ax.set_ylabel("CAGR (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("2025 EBITDA Margin")

    margin_data = financial_summary[
        ["Company", "EBITDA Margin"]
    ].sort_values(
        "EBITDA Margin",
        ascending=False
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        margin_data["Company"],
        margin_data["EBITDA Margin"]
    )

    ax.set_ylabel("EBITDA Margin (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

st.divider()

# -----------------------------
# VALUATION
# -----------------------------
st.header("💰 Valuation Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Trailing P/E")

    pe_data = valuation_table[
        ["Company", "Trailing P/E"]
    ].dropna().sort_values(
        "Trailing P/E"
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        pe_data["Company"],
        pe_data["Trailing P/E"]
    )

    ax.set_ylabel("P/E Multiple")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("EV / EBITDA")

    ev_data = valuation_table[
        ["Company", "EV/EBITDA"]
    ].dropna().sort_values(
        "EV/EBITDA"
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        ev_data["Company"],
        ev_data["EV/EBITDA"]
    )

    ax.set_ylabel("EV / EBITDA")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

st.divider()

# -----------------------------
# RISK ANALYSIS
# -----------------------------
st.header("⚠️ Risk Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Annualized Volatility")

    risk_data = risk_summary[
        ["Company", "Annualized Volatility"]
    ].sort_values(
        "Annualized Volatility"
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        risk_data["Company"],
        risk_data["Annualized Volatility"]
    )

    ax.set_ylabel("Volatility (%)")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

with col2:

    st.subheader("Beta vs S&P 500")

    beta_data = risk_summary[
        ["Company", "Beta"]
    ].sort_values(
        "Beta"
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        beta_data["Company"],
        beta_data["Beta"]
    )

    ax.axhline(
        1,
        linestyle="--"
    )

    ax.set_ylabel("Beta")

    plt.xticks(rotation=35)
    plt.tight_layout()

    st.pyplot(fig)

st.divider()

# -----------------------------
# COMPANY DEEP DIVE
# -----------------------------
st.header("🔎 Company Deep Dive")

company = st.selectbox(
    "Select a company",
    final_score["Company"].tolist()
)

selected_final = final_score[
    final_score["Company"] == company
].iloc[0]

selected_financial = financial_summary[
    financial_summary["Company"] == company
].iloc[0]

selected_risk = risk_summary[
    risk_summary["Company"] == company
].iloc[0]

selected_valuation = valuation_table[
    valuation_table["Company"] == company
].iloc[0]

selected_returns = stock_returns[
    stock_returns["Company"] == company
].iloc[0]

selected_growth = growth_data[
    growth_data["Company"] == company
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Growth Score",
    f"{selected_final['Growth Score']:.1f}"
)

col2.metric(
    "Profitability Score",
    f"{selected_final['Profitability Score']:.1f}"
)

col3.metric(
    "Valuation Score",
    f"{selected_final['Valuation Score']:.1f}"
)

col4.metric(
    "Risk Score",
    f"{selected_final['Risk Score']:.1f}"
)

st.subheader(f"{company} — Key Metrics")

company_metrics = pd.DataFrame({
    "Metric": [
        "Revenue CAGR",
        "1Y Stock Return",
        "3Y Stock Return",
        "5Y Stock Return",
        "EBITDA Margin",
        "Net Margin",
        "ROE",
        "Debt / Equity",
        "Cash / Debt",
        "Trailing P/E",
        "Forward P/E",
        "EV / EBITDA",
        "Volatility",
        "Maximum Drawdown",
        "Beta"
    ],
    "Value": [
        selected_growth["Revenue CAGR"],
        selected_returns["1Y Return"],
        selected_returns["3Y Return"],
        selected_returns["5Y Return"],
        selected_financial["EBITDA Margin"],
        selected_financial["Net Margin"],
        selected_financial["ROE"],
        selected_financial["Debt/Equity"],
        selected_financial["Cash/Debt"],
        selected_valuation["Trailing P/E"],
        selected_valuation["Forward P/E"],
        selected_valuation["EV/EBITDA"],
        selected_risk["Annualized Volatility"],
        selected_risk["Maximum Drawdown"],
        selected_risk["Beta"]
    ]
})

st.dataframe(
    company_metrics.style.format({
        "Value": "{:.2f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.info(
    f"{company} has an overall score of "
    f"{selected_final['Final Score']:.1f}/100."
)

st.divider()

# -----------------------------
# METHODOLOGY
# -----------------------------
st.header("📐 Methodology")

st.markdown(
    """
    ### Four-Dimension Scoring Framework

    Each company receives a score from **0–100** across four dimensions.

    **Growth — 25%**
    - 2021–2025 Revenue CAGR

    **Profitability — 25%**
    - EBITDA Margin
    - Net Margin
    - ROE

    **Valuation — 25%**
    - Trailing P/E
    - EV / EBITDA

    **Risk — 25%**
    - Annualized Volatility
    - Maximum Drawdown
    - Beta vs S&P 500

    Higher growth and profitability receive higher scores.

    Lower valuation multiples and lower risk receive higher scores.

    The final score is the equally weighted average of the
    four dimension scores.
    """
)

st.caption(
    "This dashboard is an analytical screening model and does not constitute investment advice."
)
