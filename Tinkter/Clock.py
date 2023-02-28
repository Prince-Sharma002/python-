import tkinter as tk
import time

counter = 0

def counter_label(label , label2):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label2.config(text = time.strftime("%H:%M:%S"))
        label.after(1000, count)

    count()

root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()

label2 = tk.Label(root)
label2.pack()

counter_label(label , label2)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
