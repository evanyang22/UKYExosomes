#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv
import pandas as pd
import PySimpleGUI as sg

sg.theme('SandyBeach')
layout = [
    [sg.Text('How many normalization columns would you like to add?')],
    [sg.Text('Number of times', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()


numTimes=int(values[0])
counter=0

while counter<numTimes:
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Please enter reference m/z, C13, and name for new column')],
        [sg.Text('Reference m/z', size =(15, 1)), sg.InputText()],
        [sg.Text('Column Name', size =(15, 1)), sg.InputText()],
        [sg.Text('C13', size =(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()

    refNum=float(values[0])
    newColumnHeader=values[1]
    C13Value=int(values[2])


    print("Using reference m/z of " + str(refNum))
    print("New Column Name is "+ newColumnHeader)
    for filename in os.scandir():
        try:
            if filename.path.endswith(".csv"):
                df = pd.read_csv(filename.name)
                #extracts denominator using refNum and 13C==0 
                denominator=df.loc[(df['Ref m/z'] == refNum) & (df["13C"]==C13Value)]["Corrected Intensity"].iloc[0]
                #dividing everything and adding to column
                addColumn=[]
                numerators= df["Corrected Intensity"]
                for num in numerators:
                    addColumn.append(num/denominator)
                df[newColumnHeader]=addColumn
                #overwrites to csv
                df.to_csv(filename.name, index=False)
            print("Done: "+ filename.name)
        except:
            print("Error: " +filename.name)
            pass
    
    counter+=1


# ### 

# In[ ]:





# In[ ]:




