🎯 1. Project Overview
The Finance Market Pulse ETL is a fully automated data pipeline designed to ingest historical and daily financial asset data. The system ensures high data quality and provides ready-to-use indicators for downstream analytical dashboards.

🧱 2. Core Functional Requirements
Automatic Ingestion: Retrieve daily closing prices for a configurable list of stock tickers (e.g., AAPL, TSLA, BTC-USD).

Data Transformation: * Compute 24-hour price change percentage.

Calculate rolling 7-day mean price (Moving Average).

Handling of market close days (weekends/holidays) via padding/interpolation.

Reliability: * Idempotent Loading: Prevents row duplication on reruns.

Auto-Healing: Ability to perform "backfills" for missing historical dates.

🛠️ 3. Tech Stack
Orchestration: Apache Airflow (Docker-based).

Language: Python 3.10+.

Libraries: Pandas (Vectorized transformations), yfinance (Data source).

Database: PostgreSQL (Analytical storage).

Deployment: Docker Compose for multi-container architecture.

📊 4. Data Model (PostgreSQL)
Ticker: VARCHAR(10)

Trade Date: DATE (Primary Key part)

Close Price: NUMERIC(15, 4)

Daily Return: NUMERIC(10, 2) (Percentage)

Moving Avg (7d): NUMERIC(15, 4)