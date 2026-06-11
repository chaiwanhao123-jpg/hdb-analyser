import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("resale-flat-prices.csv")
df['month'] = pd.to_datetime(df['month'])
df['year'] = df['month'].dt.year

recent = df[df['year'] >= 2022]
by_town = recent.groupby('town')['resale_price'].mean().sort_values(ascending=False).iloc[:10]
print(by_town)

df['price per sqm'] = df['resale_price'] / df['floor_area_sqm']
town_psqm = df.groupby('town')['price per sqm'].mean().sort_values(ascending=False)
print(town_psqm)

price = df.groupby('year')['resale_price'].mean()
print(price)

price.plot(kind='line', title='Average HDB Resale Price by Year')
plt.ylabel('Average Resale Price (SGD)')
plt.tight_layout()
plt.savefig('hdb-price-trend.png')    
plt.show()
# observation: the average resale price of flats have been on an upward trend over the years. interestingly, the upward trend strengthened from 2020 onwards, when the pandemic hit, which may be due to a combination of factors such as low interest rates, increased demand for larger living spaces, and supply constraints.

by_town.plot(kind='bar', title='Average HDB Resale Price by Town')
plt.ylabel('Average Resale Price (SGD)')
plt.tight_layout()
plt.savefig('hdb-price-by-town.png')
plt.show()
# observation: there is no clear correlation between the town and the average resale price of flats, with far flung towns such as Pasir Ris ranked among the towns with highest resale prices. 

town_psqm.plot(kind='bar', title='Average Price per sqm by Town')
plt.ylabel('Average Price per sqm (SGD)')
plt.tight_layout()
plt.savefig('hdb-price-per-sqm-by-town.png')
plt.show()
# observation: with price per sqm by town, the pattern is clearer with the towns located closer to the city such as Queenstown being ranked higher on the list. This indicates that the list focusing on average flat resale prices may be distorted by the towns with primarily larger flats, such as Pasir Ris, which moved many places down from the previous rankings. this is a sign that the towns further from the city may offer greater value for money for flat buyers in terms of floor area, which is especially important for households that plan to have more children or multi-generational households.

price_2017 = df[df['year'] == 2017].groupby('town')['price per sqm'].mean()
price_2022 = df[df['year'] == 2022].groupby('town')['price per sqm'].mean()
price_diff = (price_2022 - price_2017).dropna().sort_values(ascending=False)

price_diff.plot(kind='bar', title='Price per sqm Difference between 2022 and 2017 by Town')
plt.ylabel('Price Difference (SGD/sqm)')
plt.xlabel('Town')
plt.tight_layout()
plt.savefig('hdb-price-diff-2017-2022.png')
plt.show()
# observation: the price per sqm difference between 2017 and 2022 shows some correlation to the previous chart, whereby the towns on the lower end of the price per sqm recorded greater price increases in the period between 2017 and 2022. this indicates that the flats located in the towns have greter potential for capital apprecation. 

# Scatterplot of all resale prices over time
plt.figure(figsize=(14, 6))
plt.scatter(df['month'], df['resale_price'], alpha=0.5, s=20, c=df['year'], cmap='viridis')
plt.xlabel('Transaction Date')
plt.ylabel('Resale Price (SGD)')
plt.title('All Resale Prices Over Time')
plt.colorbar(label='Year')
plt.tight_layout()
plt.savefig('hdb-resale-scatter.png')
# plt.show()
# observation: the magnitude of increase in resale prices is uneven across prices ranges with a markedly sharper increase in the higher price ranges, which may indicate stronger demand for more expensive flats. this is seen from the consistent increase in the price of the most expensive flats transacted while the lowest resale prices have been relatively stable and not on a consistent upward trend.