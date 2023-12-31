# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_27/day_27_env/Scripts/Activate.ps1

import tkinter

# window = tkinter.Tk()
# window.title("My Program")
# window.minsize(width=500, height=300)

# def clicked_button():
#     my_label.config(text=input.get())

# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()


# button = tkinter.Button(text="Click Me!", command=clicked_button)
# button.pack()

# input = tkinter.Entry(width=10)
# input.pack()

window = tkinter.Tk()
window.title("Miles to kilometers converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def clicked_button():
    distance = float(miles_input.get()) * 1.609
    label_calculation.config(text=f"{distance:.2f}")


miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to", font=("Arial", 12))
label_equal.grid(column=0, row=1)

label_km = tkinter.Label(text="Kilometres", font=("Arial", 12))
label_km.grid(column=2, row=1)

label_calculation = tkinter.Label(text="", font=("Arial", 12))
label_calculation.grid(column=1, row=1)


button = tkinter.Button(text="Calculate", command=clicked_button)
button.grid(column=1, row=2)


window.mainloop()
