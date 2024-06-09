import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np

# Create the main tkinter window
root = tk.Tk()
root.title("Button Bar, Inputs, Progress Bar, and Equally Spaced Plots")

# Create a frame for the button bar on the left
button_bar = ttk.Frame(root)
button_bar.pack(side="left", fill="y")

# Create input boxes in the button bar
inputs = []
for i in range(4):
    input_label = ttk.Label(button_bar, text=f"Input {i + 1}:")
    input_label.pack(fill="x", padx=5, pady=5)
    input_entry = ttk.Entry(button_bar)
    input_entry.pack(fill="x", padx=5, pady=5)
    inputs.append(input_entry)

# Create a frame for the progress bar and buttons at the top
top_frame = ttk.Frame(root)
top_frame.pack(fill="x")

# Create a progress bar at the top
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(top_frame, variable=progress_var, maximum=100)
progress_bar.pack(fill="x", padx=5, pady=5)

# Create two buttons in the top frame
button1 = ttk.Button(top_frame, text="Start")
button2 = ttk.Button(top_frame, text="Stop")
button1.pack(side="left", padx=5, pady=5)
button2.pack(side="left", padx=5, pady=5)

# Create a frame for the right part of the screen divided into two equally spaced zones
right_frame = ttk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

# Create a frame for the left zone with two stacked heatmaps
left_zone = ttk.Frame(right_frame)
left_zone.grid(row=0, column=0, sticky="nsew")

# Load and display the first heatmap image
heatmap_image1 = Image.open("heatmap.png").resize((500,500))  # Replace with the path to your first heatmap image
heatmap_image1 = ImageTk.PhotoImage(heatmap_image1)
heatmap_label1 = ttk.Label(left_zone, image=heatmap_image1)
heatmap_label1.pack(fill="both", expand=True)
heatmap_label1.image = heatmap_image1

# Load and display the second heatmap image below the first
heatmap_image2 = Image.open("heatmap1.png").resize((500,500))  # Replace with the path to your second heatmap image
heatmap_image2 = ImageTk.PhotoImage(heatmap_image2)
heatmap_label2 = ttk.Label(left_zone, image=heatmap_image2)
heatmap_label2.pack(fill="both", expand=True)
heatmap_label2.image = heatmap_image2

# Create a frame for the right zone with two identical example plots stacked vertically
right_zone = ttk.Frame(right_frame)
right_zone.grid(row=0, column=1, sticky="nsew")

# Create example plots
fig, ax = plt.subplots(figsize=(13, 2))
ax.plot(np.random.rand(10))
ax.set_title("Identical Plots")

# Embed the first plot in the right zone
plot_canvas = FigureCanvasTkAgg(fig, master=right_zone)
plot_canvas.get_tk_widget().pack(fill="both", expand=True)

# Clone the first plot to create the second identical plot
fig2, ax2 = fig, ax

# Embed the second identical plot in the right zone
plot_canvas2 = FigureCanvasTkAgg(fig2, master=right_zone)
plot_canvas2.get_tk_widget().pack(fill="both", expand=True)

# Configure row weights to ensure equal spacing of heatmaps and plots
left_zone.grid_rowconfigure(0, weight=1)
left_zone.grid_rowconfigure(1, weight=1)
right_zone.grid_rowconfigure(0, weight=1)
right_zone.grid_rowconfigure(1, weight=1)

# Run the tkinter main loop
root.mainloop()
