import streamlit as st
import pandas as pd

st.title("Singapore HDB Resale Price Explorer")

df = pd.read_csv("resale-flat-prices.csv")
df['month'] = pd.to_datetime(df['month'])
df['year'] = df['month'].dt.year

town = st.selectbox("Select a town", sorted(df['town'].unique()))
flat_type = st.selectbox("Select flat type", sorted(df['flat_type'].unique()))

filtered = df[(df['town'] == town) & (df['flat_type'] == flat_type)]
yearly = filtered.groupby('year')['resale_price'].mean()

st.subheader(f"Avg resale price â€” {town}, {flat_type}")
st.line_chart(yearly)
if not yearly.empty:
    st.metric("Most recent avg", f"${yearly.iloc[-1]:,.0f}")

st.divider()
st.subheader("Key insights from the data")

st.write("**1. Price increases are uneven across price ranges**")
st.write("Higher-priced flats have seen markedly sharper increases while the lowest resale prices have remained relatively stable over the years, suggesting stronger demand at the upper end of the market.")
st.image("hdb-resale-scatter.png")

st.write("**2. Post-2020 acceleration**")
st.write("Average resale prices have been on a consistent upward trend, with the increase strengthening from 2020 onwards despite the economic downturn arising from thepandemic. This is likely driven by low interest rates, increased demand for larger living spaces, and supply constraints during the pandemic.")
st.image("hdb-price-trend.png")

st.write("**3. Raw average price is a misleading ranking**")
st.write("There is no clear correlation between town location and average resale price — Pasir Ris ranks among the highest while well-located Marine Parade sits mid-table. This is because towns with primarily larger flats skew the average upward.")
st.image("hdb-price-by-town.png")

st.write("**4. Price per sqm tells a clearer story**")
st.write("When ranked by price per sqm, towns closer to the city like Queenstown rank higher, showing that this is a more accurate measure of relative value than the price of flats. Towns further from the city tend to offer greater floor area value, which is an important consideration for larger or multi-generational households.")
st.image("hdb-price-per-sqm-by-town.png")

st.write("**5. Lower price per sqm towns have higher capital appreciation**")
st.write("Towns on the lower end of price per sqm recorded greater price increases between 2017 and 2022. This can help potential buyers identify properties with stronger potential for capital appreciation.")
st.image("hdb-price-diff-2017-2022.png")