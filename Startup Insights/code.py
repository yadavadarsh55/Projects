# ## Insights of the Data
# * The number of startups listed here are almost equally distributed in the three states **NewYork**, **Florida** and **California** are 17, 16, 17 respectively.
# * The startups which are spending more in **Research and Development** are making High Profits. **Marketing Spend** is also tends to give profits to the startups.
# * Startups which are spending in the **Research and Development** are often spending in the **Marketing** also.
# * **Florida** is the state in which the startups are investing more in **Research and Development** and **Marketing**, which helps in making the state with the highest profits among the states.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("50_Startups.csv")
df = pd.read_csv("50_Startups.csv")
state = dataset.iloc[: ,3].values
dataset = dataset.drop('State', axis = 1)
R_and_D = dataset.iloc[: ,0].values
Administration = dataset.iloc[: ,1].values
Market_Spend = dataset.iloc[: ,2].values
Profit = dataset.iloc[: ,-1].values

relation = dataset.corr()

plt.plot(R_and_D, Profit, color = 'black')
plt.title("Research & Development ")
plt.xlabel("Research and Development Spend (in $)")
plt.ylabel("Profit (in $)")
plt.show()

plt.plot(Administration, Profit, color = 'red')
plt.title("Administration ")
plt.xlabel("Administration Spend (in $)")
plt.ylabel("Profit (in $)")
plt.show()

plt.plot(Market_Spend, Profit)
plt.title("Market Spend ")
plt.xlabel("Market Spend (in $)")
plt.ylabel("Profit (in $)")
plt.show()

plt.plot(R_and_D, Market_Spend, color = 'black', label= 'R&D Expenditure', ls='--')
plt.title("R&D and Administration comparision")
plt.ylabel("Market Spend (in $)")
plt.xlabel("R&D Spend (in $)")
plt.show()

values = list(relation.iloc[: ,-1].values)
values.pop(-1)
features = []
features.append("R&D")
features.append("Administration")
features.append("Market Spend")
print(values)
print(features)

plt.bar(features, values, width=0.5, color='hotpink')
plt.ylabel('Corelation Coefficient')
plt.show()

le = LabelEncoder()
state = le.fit_transform(state)
cont = []
mylabels = ['New York', 'Florida', 'California']
ny = 0
fl = 0
cf = 0
for x in state:
    if x == 2:
        ny = ny+1
    elif x == 1:
        fl = fl+1
    else:
        cf = cf+1
cont.append(ny)
cont.append(fl)
cont.append(cf)
print(cont)

plt.pie(cont, labels=cont, shadow=True)
plt.legend(mylabels, loc=2)
plt.show()

grpdata = df.groupby(['State']).mean()
print(grpdata)

avg_profit = list(grpdata['Profit'])
RnD_spend = grpdata['R&D Spend']
admin_spend = grpdata['Administration']
marketing_spend = grpdata['Marketing Spend']
mylables = ['California', 'Florida', 'New York']
plt.subplot(2, 2, 1)
plt.bar(mylabels, avg_profit, color = 'pink', width=0.5)
plt.title("Profit")

plt.subplot(2, 2, 2)
plt.bar(mylabels, RnD_spend, color = 'yellow', width=0.5)
plt.title("R&D Spend")

plt.subplot(2, 2, 3)
plt.bar(mylabels, admin_spend, color = 'orange', width=0.5)
plt.title("Administration")

plt.subplot(2, 2, 4)
plt.bar(mylabels, marketing_spend, color = 'green', width=0.5)
plt.title("Marketing")

plt.tight_layout()
plt.show()