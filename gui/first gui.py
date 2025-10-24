# Perfect! Let’s make a **Temperature Converter with a GUI** using **Tkinter**, which comes built into Python.

# You’ll be able to type a temperature, choose whether to convert from Celsius ↔ Fahrenheit, and see the result on the screen — all in a small window.



## 🌡️ GUI Temperature Converter (Python + Tkinter)

### ✅ Code:

# ```python
import tkinter as tk
from tkinter import ttk

# --- Functions ---
def convert_temp():
    try:
        temp = float(entry_temp.get())
        if conversion_type.get() == "C → F":
            result = (temp * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        else:
            result = (temp - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")
    except ValueError:
        label_result.config(text="Please enter a valid number")

# --- GUI Setup ---
# window = tk.Tk()
# window.title("Temperature Converter")
# window.geometry("300x200")
# window.resizable(False, False)

# # Input
# label_prompt = tk.Label(window, text="Enter temperature:")
# label_prompt.pack(pady=5)

# entry_temp = tk.Entry(window, width=10)
# entry_temp.pack()

# # Dropdown for conversion type
# conversion_type = ttk.Combobox(window, values=["C → F", "F → C"], state="readonly", width=10)
# conversion_type.current(0)
# conversion_type.pack(pady=10)

# # Convert button
# button_convert = tk.Button(window, text="Convert", command=convert_temp)
# button_convert.pack(pady=5)

# # Result label
label_result = tk.Label(window, text="Result will appear here", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# Run app
window.mainloop()
# ```

# ---

### 🧠 How It Works:

# * **Tkinter** creates the window.
# * The user enters a temperature and selects the conversion direction.
# * When “Convert” is clicked, it calls the `convert_temp()` function.
# * The converted value is displayed in a label.

# ---

# ### 💡 Optional Improvements:

# You could add:

# * Clear button.
# * Background color or better styling.
# * Keyboard shortcuts (e.g., press Enter to convert).

# ---

# Would you like me to show you an **enhanced version** (with colors, fonts, and better layout)?
