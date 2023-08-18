import pandas as pd
import io
data = pd.read_csv(io.BytesIO(uploaded['McDonaldsMenuNutrition 2 (1).csv']))
print(data)


import matplotlib as mp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('McDonaldsMenuNutrition 2 (1).csv')

df.head()

df.tail()

#Pie chart
chart=df.plot.pie(y="Calories",figsize=(100,10))
plt.show()

#Histogram

from matplotlib import pyplot as plt
data=df.head()
fig,ax=plt.subplots(figsize=(7,7))
ax.hist(data,bins=[240,260,290,300,310])
plt.show()
