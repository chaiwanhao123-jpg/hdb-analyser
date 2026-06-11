# Singapore HDB Resale Price Explorer

An interactive data dashboard exploring trends in Singapore's 
HDB resale flat market, built using Python, pandas, and Streamlit.

🔗 [Live app](https://hdb-resale-price-tracker-8erebo8cw4bghhs2hpmxav.streamlit.app/)

## What it does

Users can select any town and flat type to see how average 
resale prices have changed year by year. The app also surfaces 
five data-driven insights about the broader HDB resale market.

## Key insights

1. **Price increases are uneven across price ranges** — higher-priced 
flats have seen markedly sharper increases while the lowest resale 
prices have remained relatively stable, suggesting stronger demand 
at the upper end of the market.

2. **Post-2020 acceleration** — the upward trend in average resale 
prices strengthened from 2020 onwards despite the economic downturn, 
likely driven by low interest rates, demand for larger living spaces, 
and supply constraints.

3. **Raw average price is a misleading ranking** — Pasir Ris ranks 
among the most expensive towns despite its location, while 
well-located Marine Parade sits mid-table. Towns with primarily 
larger flats skew the average upward.

4. **Price per sqm tells a clearer story** — when ranked by price 
per sqm, towns closer to the city rank higher. Towns further out 
offer greater floor area value, especially relevant for larger or 
multi-generational households.

5. **Lower price per sqm towns show stronger capital appreciation** — 
towns on the lower end of price per sqm recorded greater price 
increases between 2017 and 2022, useful for buyers prioritising 
long-term value.

## Tech stack

- Python
- pandas — data manipulation and analysis
- matplotlib / seaborn — chart generation
- SQLite — data storage and SQL queries
- Streamlit — interactive web dashboard

## Data source

[HDB Resale Flat Prices](https://data.gov.sg) — data.gov.sg

## Running locally

git clone https://github.com/chaiwanhao123-jpg/hdb-analyser
cd hdb-analyser
pip install -r requirements.txt
streamlit run app.py
