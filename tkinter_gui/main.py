import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Chat App")
root.geometry("500x600")
root.resizable(False, False)

history_frame = tk.Frame(root, bg="white", bd=5)
history_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.6, anchor="n")

scrollbar = ttk.Scrollbar(history_frame)
scrollbar.pack(side="right", fill="y")

history_canvas = tk.Canvas(history_frame, bg="white", bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
history_canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=history_canvas.yview)

def on_configure(event):
    history_canvas.configure(scrollregion=history_canvas.bbox("all"))

history_canvas.bind("<Configure>", on_configure)

messages_frame = tk.Frame(history_canvas, bg="white", bd=0)
history_canvas.create_window((0, 0), window=messages_frame, anchor="nw")

def send_message(text, direction):
    if direction == "left":
        color = "lightgreen"
        anchor = "w"
    else:
        color = "lightblue"
        anchor = "e"
    message_widget = tk.Label(messages_frame, bg=color, fg="black", text=text, font=("Helvetica", 12), wraplength=300, padx=10, pady=5, borderwidth=2, relief="groove")
    message_widget.pack(side="top", fill="x", padx=5, pady=5, anchor=anchor)
    messages_frame.update_idletasks()
    history_canvas.configure(scrollregion=history_canvas.bbox("all"))
    # AI response
    if direction == "right":
        if text.lower() == "hello":
            response = "Hello, how can I assist you?"
        else:
            response = "I'm sorry, I don't know the answer to that."
        ai_message_widget = tk.Label(messages_frame, bg="lightgreen", fg="black", text=response, font=("Helvetica", 12), wraplength=300, padx=10, pady=5, borderwidth=2, relief="groove")
        ai_message_widget.pack(side="top", fill="x", padx=5, pady=5, anchor="w")
        messages_frame.update_idletasks()
        history_canvas.configure(scrollregion=history_canvas.bbox("all"))

def send_message_wrapper():
    text = entry.get()
    if text != "":
        entry.delete(0, "end")
        send_message(text, "right")

entry_frame = tk.Frame(root, bg="white", bd=5)
entry_frame.place(relx=0.5, rely=0.8, relwidth=0.9, relheight=0.1, anchor="n")

entry = tk.Entry(entry_frame, font=("Helvetica", 12))
entry.pack(side="left", fill="both", expand=True, padx=5, pady=5)

send_button = tk.Button(entry_frame, text="Send", font=("Helvetica", 12), command=send_message_wrapper)
send_button.pack(side="right", padx=5, pady=5)

root.mainloop()
