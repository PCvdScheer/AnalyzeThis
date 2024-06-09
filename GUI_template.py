import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np
import time
import threading


#All the functions required for the program

def counter():
    for i in range(100):
        time.sleep(0.1)
        print(str(i))
        progress_bar['value'] = i+1
    # progress_bar.stop()

def download_file():
    label1["text"] = "Analyzing..."
    # Disable the button while downloading the file.
    button1["state"] = "disabled"
    # Start the download in a new thread.
    t = threading.Thread(target=counter)
    t.start()
    # Start checking periodically if the thread has finished.
    schedule_check(t)


def check_if_done(t):
    # If the thread has finished, re-enable the button and show a message.
    if not t.is_alive():
        label1["text"] = "File successfully analyzed!"
        button1["state"] = "normal"
    else:
        # Otherwise check again after one second.
        schedule_check(t)

def schedule_check(t):
    """
    Schedule the execution of the `check_if_done()` function after
    one second.
    """
    root.after(1000, check_if_done, t)

def end_program():
    exit()

"Original", "Heatmap", "Contourplot", "density plot"

def plot1():
    # Load and display the first heatmap image
    #print(str(clicked1.get()))
    plot_list = {'Original':'heatmap.png', 'Heatmap': 'heatmap1.png', 'Contourplot':'heatmap2.png', 'density plot':'heatmap3.png'}
    img1 = plot_list[clicked1.get()]
    heatmap_image1 = Image.open(img1).resize((535, 535))  # Replace with the path to your first heatmap image
    heatmap_image1 = ImageTk.PhotoImage(heatmap_image1)
    heatmap_label1 = ttk.Label(left_zone, image=heatmap_image1)
    # heatmap_label1.pack(fill="both", expand=True)
    heatmap_label1.grid(row = 0, column =0, sticky='nsew')
    heatmap_label1.image = heatmap_image1

def plot2():
    # Load and display the first heatmap image
    #print(str(clicked1.get()))
    plot_list = {'Original':'heatmap.png', 'Heatmap': 'heatmap1.png', 'Contourplot':'heatmap2.png', 'density plot':'heatmap3.png'}
    img2 = plot_list[clicked2.get()]
    heatmap_image2 = Image.open(img2).resize((1000, 700))  # Replace with the path to your first heatmap image
    heatmap_image2 = ImageTk.PhotoImage(heatmap_image2)
    heatmap_label2 = ttk.Label(left_zone, image=heatmap_image2)
    # heatmap_label1.pack(fill="both", expand=True)
    heatmap_label2.grid(row = 1, column =0, sticky='nsew')
    heatmap_label2.image = heatmap_image2    


# class analysis():
#     def __init__(self, name, age):


#resources used:
#https://pythonassets.com/posts/background-tasks-with-tk-tkinter/

# Create the main tkinter window
root = tk.Tk()
root.title("Mass regularity analysis")

#Ensure the app is loading center screen
#root.eval('tk::PlaceWindow . center')
root.attributes('-fullscreen',True)

#Ensuring the app always has the same size in the screen
app_width = root.winfo_screenwidth
app_height = root.winfo_screenheight

# Create a frame for the button bar on the left
button_bar = ttk.Frame(root)
button_bar.pack(side="left", fill="y",padx=40)

# Create buttons and dropdown menus in the button bar
# buttons = []
# for i in range(10):
#     button = ttk.Button(button_bar, text=f"Button {i + 1}")
#     button.pack(fill="x", padx=5, pady=5)
#     buttons.append(button)

button2 = ttk.Button(button_bar, text='Select SQL file', state='disabled').pack(fill='x', padx=2, pady=2)
button3 = ttk.Button(button_bar, text='Choose working directory', state='disabled').pack(fill='x', padx=2, pady=2)
button4 = ttk.Button(button_bar, text='Enter user name', state='disabled').pack(fill='x', padx=2, pady=2)
button5 = ttk.Button(button_bar, text='Select data file', state='disabled').pack(fill='x', padx=2, pady=2)
button6 = ttk.Button(button_bar, text='Load new image').pack(fill='x', padx=2, pady=2)
button7 = ttk.Button(button_bar, text='Enter/Update bin-size [pixels]').pack(fill='x', padx=2, pady=2)
button8 = ttk.Button(button_bar, text='Create report').pack(fill='x', padx=2, pady=2)
#button9 = ttk.Button(button_bar, text='Create report').pack(fill='x', padx=2, pady=2)
#button10 = ttk.Button(button_bar, text='re-name file').pack(fill='x', padx=2, pady=2)

# dropdowns = []
# for i in range(4):
#     dropdown_label = ttk.Label(button_bar, text=f"Dropdown {i + 1}")
#     dropdown_label.pack(fill="x", padx=5, pady=5)
#     dropdown = ttk.Combobox(button_bar, values=["Option 1", "Option 2", "Option 3"])
#     dropdown.pack(fill="x", padx=5, pady=5)
#     dropdowns.append(dropdown)
plot_list = ["Original", "Heatmap", "Contourplot", "density plot"]

dropdown_label1 = ttk.Label(button_bar, text="Image 1").pack(fill="x", padx=5, pady=5)
#dropdown1 = ttk.Combobox(button_bar, values=["Original", "Heatmap", "Contourplot", "density plot"]).pack(fill="x", padx=5, pady=5)
clicked1 = tk.StringVar()
clicked1.set("Original")
drop1 = tk.OptionMenu(button_bar, clicked1, "Original", "Heatmap", "Contourplot", "density plot").pack(fill="x", padx=5, pady=5)
button_drop1 = ttk.Button(button_bar, text='show', command=plot1).pack(fill='x', padx=5, pady=5)

dropdown_label2 = ttk.Label(button_bar, text="Image 2").pack(fill="x", padx=5, pady=5)
#dropdown2 = ttk.Combobox(button_bar, values=["Original", "Heatmap", "Contourplot", "density plot"]).pack(fill="x", padx=5, pady=5)
clicked2 = tk.StringVar()
clicked2.set("Original")
drop2 = tk.OptionMenu(button_bar, clicked2, "Original", "Heatmap", "Contourplot", "density plot").pack(fill="x", padx=5, pady=5)
button_drop2 = ttk.Button(button_bar, text='show', command = plot2).pack(fill='x', padx=5, pady=5)

dropdown_label3 = ttk.Label(button_bar, text="Plot 1").pack(fill="x", padx=5, pady=5)
dropdown3 = ttk.Combobox(button_bar, values=["Variance MD", "Variance CD", "Var vs. binsize", "Variance Hist.", "Grey value Hist.", "Quantum data"]).pack(fill="x", padx=5, pady=5)

button_drop3 = ttk.Button(button_bar, text='show').pack(fill='x', padx=5, pady=5)

dropdown_label4 = ttk.Label(button_bar, text="Plot 2").pack(fill="x", padx=5, pady=5)
dropdown4 = ttk.Combobox(button_bar, values=["Variance MD", "Variance CD", "Var vs. binsize", "Variance Hist.", "Grey value Hist.", "Quantum data"]).pack(fill="x", padx=5, pady=5)

button_drop4 = ttk.Button(button_bar, text='show').pack(fill='x', padx=5, pady=5)

# Create input boxes in the button bar
# inputs = []
# for i in range(4):
#     input_label = ttk.Label(button_bar, text=f"Input {i + 1}:")
#     input_label.pack(fill="x", padx=5, pady=5)
#     input_entry = ttk.Entry(button_bar)
#     input_entry.pack(fill="x", padx=5, pady=5)
#     inputs.append(input_entry)

input_label1 = ttk.Label(button_bar, text="Sample weight").pack(fill="x", padx=5, pady=5)
input_entry = ttk.Entry(button_bar).pack(fill="x", padx=5, pady=5)

input_label2 = ttk.Label(button_bar, text="width/height [mm]").pack(fill="x", padx=5, pady=5)
input_entry2 = ttk.Entry(button_bar).pack(fill="x", padx=5, pady=5)

input_label3 = ttk.Label(button_bar, text="dtex").pack(fill="x", padx=5, pady=5)
input_entry3 = ttk.Entry(button_bar).pack(fill="x", padx=5, pady=5)

input_label4 = ttk.Label(button_bar, text="threads").pack(fill="x", padx=5, pady=5)
input_entry4 = ttk.Entry(button_bar).pack(fill="x", padx=5, pady=5)

# Create a progress bar at the top
progress_bar = ttk.Progressbar(button_bar, mode='determinate', length=200)
progress_bar.pack(fill="x", padx=5, pady=5)

# Create two buttons in the top frame
label1 = ttk.Label(button_bar, text="Idle")
label1.pack(padx=5, pady=5)
button1 = ttk.Button(button_bar, text="Analyze", command= download_file)
button1.pack(padx=5, pady=5,  fill="x")

button11 = ttk.Button(button_bar, text='Exit', command=end_program).pack(fill='x', padx=5, pady=5)

# Create a frame for the right part of the screen divided into two equally spaced zones
right_frame = ttk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

# Create a frame for the left zone with two stacked heatmaps
left_zone = ttk.Frame(right_frame)
left_zone.grid(row=0, column=0, sticky="nsew")
left_zone.propagate(0)

# Load and display the first heatmap image
heatmap_image1 = Image.open("heatmap.png").resize((535, 535))  # Replace with the path to your first heatmap image
heatmap_image1 = ImageTk.PhotoImage(heatmap_image1)
heatmap_label1 = ttk.Label(left_zone, image=heatmap_image1)
# heatmap_label1.pack(fill="both", expand=True)
heatmap_label1.grid(row = 0, column =0, sticky='nsew')
heatmap_label1.image = heatmap_image1

# Load and display the second heatmap image below the first
heatmap_image2 = Image.open("heatmap1.png").resize((535, 535))  # Replace with the path to your second heatmap image
heatmap_image2 = ImageTk.PhotoImage(heatmap_image2)
heatmap_label2 = ttk.Label(left_zone, image=heatmap_image2)
# heatmap_label2.pack(fill="both", expand=True)
heatmap_label2.grid(row = 1, column =0, sticky='nsew')
heatmap_label2.image = heatmap_image2

# Create a frame for the right zone with two identical example plots stacked vertically
middle_zone = ttk.Frame(right_frame)
middle_zone.grid(row=0, column=1, sticky="nsew")
middle_zone.propagate(1)

# Create example plots
fig, ax = plt.subplots(figsize=(8, 2))
ax.plot(np.random.rand(10))
ax.set_title("Identical Plots")

# Embed the first plot in the right zone
plot_canvas = FigureCanvasTkAgg(fig, master=middle_zone)
plot_canvas.get_tk_widget().pack(fill="both", expand=True, anchor='e')

# Clone the first plot to create the second identical plot
fig2, ax2 = fig, ax

# Embed the second identical plot in the right zone
plot_canvas2 = FigureCanvasTkAgg(fig2, master=middle_zone)
plot_canvas2.get_tk_widget().pack(fill="both", expand=True, anchor='e')

# Create a frame for the right zone with two identical example plots stacked vertically
right_zone = ttk.Frame(right_frame)
right_zone.grid(row=0, column=2, sticky="n")
right_zone.propagate(1)

label_list = ['Dimension x [mm]','Dimension y [mm]', 'Pixel size [mm]', 'bin size [pixels]', 'Sample weight [g/m2]', 'Av. val MD', 'Stdev. MD',' Variance MD', 'Av. val CD', 'Stdev. CD', 'Variance CD','MD/CD',]
value_list = ['100', '100', '0.01', '4', '113', '50', '5', '1', '50', '5', '1','1.1']

for i in range(len(label_list)):
    input_label = ttk.Label(right_zone, text=f"{label_list[i]}: {value_list[i]}", font='Helvetica 12 bold')
    input_label.grid(row=i, column = 0, padx=5, pady=5, sticky='w')

# Configure row weights to ensure equal spacing of heatmaps and plots
left_zone.grid_rowconfigure(0, weight=1)
left_zone.grid_rowconfigure(1, weight=1)
middle_zone.grid_rowconfigure(0, weight=1)
middle_zone.grid_rowconfigure(1, weight=1)
right_zone.grid_rowconfigure(0, weight=1)
right_zone.grid_rowconfigure(1, weight=1)



# Run the tkinter main loop
root.mainloop()
