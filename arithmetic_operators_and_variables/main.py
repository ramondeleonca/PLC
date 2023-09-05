# Import necessary modules
import tkinter
import utils
from tkinter import ttk

# Create the main application window
root = tkinter.Tk()
root.title("Arithmetic Operators and Variables: Chemist's calculator")

# Create a frame to organize the input fields and labels
left_frame = ttk.Frame(root, padding=10)
left_frame.grid(row=0, column=0)

# Create labels and entry fields for protons, electrons, neutrons, mass, and charge
protons_label = ttk.Label(left_frame, text="Protons")
protons_label.grid(row=0, column=0)
protons_entry = ttk.Entry(left_frame)
protons_entry.grid(row=0, column=1)

electrons_label = ttk.Label(left_frame, text="Electrons")
electrons_label.grid(row=1, column=0)
electrons_entry = ttk.Entry(left_frame)
electrons_entry.grid(row=1, column=1)

neutrons_label = ttk.Label(left_frame, text="Neutrons")
neutrons_label.grid(row=2, column=0)
neutrons_entry = ttk.Entry(left_frame)
neutrons_entry.grid(row=2, column=1)

mass_label = ttk.Label(left_frame, text="Mass")
mass_label.grid(row=3, column=0)
mass_entry = ttk.Entry(left_frame)
mass_entry.grid(row=3, column=1)

charge_label = ttk.Label(left_frame, text="Charge")
charge_label.grid(row=4, column=0)
charge_entry = ttk.Entry(left_frame)
charge_entry.grid(row=4, column=1)

# Create labels to display the calculation results
result_label_label = ttk.Label(left_frame, text="Result:")
result_label_label.grid(row=7, column=0, columnspan=2)

result_label = ttk.Label(left_frame, text="")
result_label.grid(row=8, column=0, columnspan=2)

# Define a function to perform calculations based on user input
def calculate():
    protons = int(protons_entry.get() or 0)
    electrons = int(electrons_entry.get() or 0)
    neutrons = int(neutrons_entry.get() or 0)
    mass = int(mass_entry.get() or 0)
    charge = int(charge_entry.get() or 0)
    
    # Check various combinations of input values and call corresponding utility functions
    if neutrons and electrons and protons:
        result = utils.mass_and_charge(neutrons, electrons, protons)
        result_label["text"] = "mass " + str(result[0]) + ", charge " + str(result[1])
    if charge and mass and protons:
        result = utils.neutrons_and_electrons(charge, mass, protons)
        result_label["text"] = "neutrons " + str(result[0]) + ", electrons " + str(result[1])
    if charge and mass:
        result = utils.neutrons_and_protons(charge, mass)
        result_label["text"] = "neutrons " + str(result[0]) + ", protons " + str(result[1])
    if charge and mass and neutrons:
        result = utils.protons_and_electrons(charge, mass, neutrons)
        result_label["text"] = "protons " + str(result[0]) + ", electrons " + str(result[1])
    if charge and neutrons and protons:
        result = utils.mass_and_electrons(charge, neutrons, protons)
        result_label["text"] = "mass " + str(result[0]) + ", electrons " + str(result[1])
    if charge and neutrons:
        result = utils.protons_and_mass(charge, neutrons)
        result_label["text"] = "protons " + str(result[0]) + ", mass " + str(result[1])
    if mass and electrons and protons:
        result = utils.neutrons_and_charge(mass, electrons, protons)
        result_label["text"] = "neutrons " + str(result[0]) + ", charge " + str(result[1])
    if mass and neutrons and electrons:
        result = utils.protons_and_charge(mass, neutrons, electrons)
        result_label["text"] = "protons " + str(result[0]) + ", charge " + str(result[1])

# Create a "Calculate" button and bind it to the calculate function
calculate_button = ttk.Button(left_frame, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

# Define a function to clear all input fields and result label
def clear():
    protons_entry.delete(0, tkinter.END)
    electrons_entry.delete(0, tkinter.END)
    neutrons_entry.delete(0, tkinter.END)
    mass_entry.delete(0, tkinter.END)
    charge_entry.delete(0, tkinter.END)
    result_label["text"] = ""

# Create a "Clear" button and bind it to the clear function
calculate_button = ttk.Button(left_frame, text="Clear", command=clear)
calculate_button.grid(row=6, column=0, columnspan=2)

# Start the main application event loop
if __name__ == "__main__":
    root.mainloop()
