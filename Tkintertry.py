import tkinter as tk

root = tk.Tk()
root.title("Hello, Tkinter!")
def on_butt_click():
    print("button was called")

def show_inp():
    user_inp = entry.get()
    print(f"user input: {user_inp}")

button = tk.Button(root,text = "click me",command = on_butt_click)
label = tk.Label(root,text = "Example",font=("arial",30))
entry = tk.Entry(root,width=30)
bt = tk.Button(root,text="submit",command= show_inp)
bt.pack()
button.pack()
label.pack()
root.geometry("600x700")

root.mainloop()

