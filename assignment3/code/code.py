import numpy as np
import pandas as pd

#input data
data = pd.read_excel('../tables/mode.xlsx','Sheet1')
mydata =np.array(data)
smple_spce=20

#possible number of marks (out of 10)
marks=[i for i in range(12)]

#number of student getting marks
freq_stdnt=np.histogram(mydata,marks)
freq_stdnt=np.asarray(freq_stdnt[0])

#removing mark[11]
marks.pop()

#getting which is recieved by max number of student
mode= np.where(freq_stdnt==np.amax(freq_stdnt))
mode= np.asarray(mode)[0][0]

#printing
print(mode)

#writing in .xlsx
write=pd.DataFrame({"Marks Obtained \n(out of 10)(X)":marks,"Frequency of\nStudent":freq_stdnt})
write.to_excel('../tables/out.xlsx',index=False)

