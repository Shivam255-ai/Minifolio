from tkinter import *
import time
import random

# Create window
root = Tk()
root.title("✨ Colorful Digital Clock ✨")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="black")

# Function to change color dynamically
def random_color():
    colors = ["#FF5733", "#33FF57", "#33D4FF", "#FF33F6", "#FFD133", "#9D33FF", "#FF3364"]
    return random.choice(colors)

# Time updating function
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time, fg=random_color())
    clock_label.after(1000, update_time)

# Heading
Label(root, text="⏰ DIGITAL CLOCK ⏰", font=("Comic Sans MS", 20, "bold"), fg="cyan", bg="black").pack(pady=10)

# Clock display
clock_label = Label(root, font=("Digital-7 Mono", 60), bg="black")
clock_label.pack(pady=20)

# Footer text
Label(root, text="Made with ❤️ in Python", font=("Arial", 12, "italic"), fg="white", bg="black").pack(side=BOTTOM)

# Start the clock
update_time()
root.mainloop()
