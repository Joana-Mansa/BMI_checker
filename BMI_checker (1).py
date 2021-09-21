#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# imports tkinter a GUI package
import tkinter as tk

# this function performs the bmi calculation

def calculate_bmi():
    get_height_cm = float(entry_height.get())
    get_weight = float(entry_weight.get())
    height_m = get_height_cm / 100
    
    # the bmi formula
    bmi = get_weight / (height_m) ** 2
    label_bmi.configure(text=f'Your bmi is : {bmi}')
    
    # commands for the various scenarios
    if bmi < 18.5:
        label_result.configure(text=f'You are underweight')
    elif bmi > 18.5 and bmi < 24.9:
        label_result.configure(text=f'You have a healthy weight')
    elif bmi > 25.0 and bmi < 29.9:
        label_result.configure(text=f'You are overweight')
    elif bmi > 30:
        label_result.configure(text=f'You are obese')

# specifications for the GUI window 
window = tk.Tk()
window.title('BMI checker')
label_height = tk.Label(text="Enter your height in cm")
entry_height = tk.Entry(width=25)
label_weight = tk.Label(text="Enter your weight in kg")
entry_weight = tk.Entry(width=25)
label_bmi = tk.Label()
label_result = tk.Label()
button_calc = tk.Button(text="Calculate", command=calculate_bmi)
label_height.pack()
entry_height.pack()
label_weight.pack()
entry_weight.pack()
label_bmi.pack()
label_result.pack()
button_calc.pack()

window.mainloop()


# In[ ]:




