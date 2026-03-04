import tkinter as tk

window = tk.Tk()

window.title("going to become coder")
window.geometry("400x200")

def button_click():
    print("Button Clicked!")
    label.config(bg="yellow")
    # label1.config(bg="black")
    # label2.config(bg="white")
    # button.config(text="changed",font="times new roman")
    # button1.config(bg="brown")

button = tk.Button(window, text="Click me", command=button_click)
button.pack()
label=tk.Label(window, text="hello , tkinter!", font=("Arial",16), bg="blue",fg="white")
label.pack()
label1=tk.Label(window, text="hello ghazanfar ali!", font=("Arial",18),bg="yellow",fg="blue")
label.pack()
label2=tk.Label(window, text="hello , ahmad Rrraahim ", font=("Arial",16),bg="green",fg="black")
label.pack()

button1 = tk.Button(window, text="Click me", command=lambda:print("click by lambda"))
button.pack()

entry=tk.Entry(window , width=20)
entry.pack()





label = tk.Label(window, text="Hello, Tkinter",fg= "blue", bg="yellow",padx=10,pady=20)
label.pack()

button = tk.Button(window, text=" Click Me ", width=15, command=lambda:
print("Button clicked! "))
button.pack()

label = tk.Label(window, text="Initial Text")
label.pack()
current_text = label.cget("text") # Using cget()
print(f"Current text: {current_text}")

current_bg = label.config()["bg"][-1] # Using config() and dictionary access
print(f"Current background: {current_bg}")

window.mainloop()


