import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#opening file
data = pd.read_excel('./tables/out.xlsx','Sheet1')

marks=data.to_numpy()[:,0] #x coordinate
prob=data.to_numpy()[:,2]  #y coordinate

#plotting
plt.plot(marks,prob, label="Probability Distribution")

plt.ylim(0,1)
plt.xlim(0,10)

#labelling 
plt.xlabel("Marks")
plt.ylabel("Probability Distribution")

plt.legend(loc="best")

plt.grid()

#saving figure
plt.savefig("./figures/fig.png")

#displaying
plt.show()
