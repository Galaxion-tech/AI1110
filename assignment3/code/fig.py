import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#opening file
data = pd.read_excel('./tables/out.xlsx','Sheet1')

marks=data.to_numpy()[:,0] #x coordinate
freq=data.to_numpy()[:,1]  #y coordinate

#plotting
plt.plot(marks,freq,marker='o', label="Graphical Representation")

plt.ylim(0,5)
plt.xlim(0,10)

#labelling 
plt.xlabel("Marks")
plt.ylabel("Frequency of Students")

plt.legend(loc="best")

plt.grid()

#saving figure
plt.savefig("./figures/fig.png")

#displaying
plt.show()
