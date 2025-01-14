import tkinter as tk
from tkinter import ttk
import time
from gingerit.gingerit import GingerIt

parser = GingerIt()

root = tk.Tk()
root.title("Chat App")
root.geometry("800x600")
root.configure(bg='#252525')
root.resizable(width=False, height=False)

# create a frame for displaying the chat history
history_frame = tk.Frame(root, bg="#141414")
history_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)

# create a scrollbar for the history frame
scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# create a canvas to display the chat history
history_canvas = tk.Canvas(history_frame, bg="#141414", yscrollcommand=scrollbar.set, highlightthickness=0)
history_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=history_canvas.yview)

# create a frame for the chat history items
history_items = tk.Frame(history_canvas, bg="#141414")
history_canvas.create_window((0, 0), window=history_items, anchor=tk.NW)

# create a frame for entering the chat message
input_frame = tk.Frame(root, bg="#252525", height=70)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

# create an entry widget for typing the chat message
input_entry = tk.Entry(input_frame, bg="#141414", fg="white", font=("Poppins", 14), borderwidth=0)
input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)


# create a frame for the settings menu
settings_frame = tk.Frame(root, bg="#252525")
settings_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

# create a label for the autocorrect setting
autocorrect_label = tk.Label(settings_frame, text="Autocorrect", bg="#252525", fg="white", font=("Poppins", 14))
autocorrect_label.pack(side=tk.LEFT, padx=10)

# create a canvas for the autocorrect setting
autocorrect_canvas = tk.Canvas(settings_frame, width=30, height=30, bg="red", highlightthickness=0)
autocorrect_canvas.pack(side=tk.LEFT)

# create an X text for the red square
autocorrect_canvas.create_text(15, 15, text="X", font=("Poppins", 14), fill="white")

# bind click event to toggle autocorrect setting
autocorrect_canvas.bind("<Button-1>", lambda event: toggle_autocorrect())

# define a function to toggle the autocorrect setting
def toggle_autocorrect():
    global autocorrect
    autocorrect = not autocorrect
    if autocorrect:
        autocorrect_canvas.configure(bg="green")
        autocorrect_canvas.delete("all")
        autocorrect_canvas.create_text(15, 15, text="✔", font=("Poppins", 14), fill="white")
    else:
        autocorrect_canvas.configure(bg="red")
        autocorrect_canvas.delete("all")
        autocorrect_canvas.create_text(15, 15, text="X", font=("Poppins", 14), fill="white")


# create a button to send the chat message
send_button = tk.Button(input_frame, text="Send", bg="#5E5CE6", fg="white", font=("Poppins", 14), highlightthickness=0,
                         borderwidth=3)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)


autocorrect = False

def send_message(event=None):

    message = input_entry.get()

    if message:

        if autocorrect:
            message = parser.parse(message)['result']

        else:
            pass

        message = " " + str(message) + " "
        # create a frame for the chat message
        message_frame = tk.Frame(history_items, bg="#141414", padx=10, pady=5)

        # create a label to display the chat message text
        message_text = tk.Label(
            message_frame, text=message, bg="#5E5CE6", fg="white", font=("Poppins", 14),
            wraplength=400, justify=tk.LEFT, padx=10, pady=10,
            borderwidth=0, relief=tk.RAISED,
        )
        message_text.pack(side=tk.RIGHT, fill=tk.Y)

        # create a label to display the time the message was sent
        timestamp = time.strftime("%H:%M", time.localtime())
        time_label = tk.Label(
            message_frame, text=timestamp, bg="#141414", fg="gray", font=("Poppins", 10),
            padx=5, pady=5,
        )
        time_label.pack(side=tk.RIGHT)

        # add the chat message frame to the chat history items
        message_frame.update()
        message_frame_width = message_frame.winfo_width()
        history_items.config(width=message_frame_width)
        history_canvas.config(scrollregion=history_canvas.bbox(tk.ALL))
        history_items.pack(fill=tk.BOTH, expand=True)
        message_frame.pack(fill=tk.X)

        # clear the input entry
        input_entry.delete(0, tk.END)

        # scroll to the bottom of the chat history
        history_canvas.yview_moveto(1)

        # clear the input entry
        input_entry.delete(0, tk.END)

        # scroll to the bottom of the chat history
        history_canvas.yview_moveto(1)

        recieve_message()
def recieve_message(event=None):

    message = "Hello!"

    if message:



        message = " " + str(message) + " "
        # create a frame for the chat message
        message_frame = tk.Frame(history_items, bg="#141414", padx=10, pady=5)

        # create a label to display the chat message text
        message_text = tk.Label(
            message_frame, text=message, bg="#81B622", fg="white", font=("Poppins", 14),
            wraplength=400, justify=tk.LEFT, padx=10, pady=10,
            borderwidth=0, relief=tk.RAISED,
        )
        message_text.pack(side=tk.LEFT, fill=tk.Y)

        # create a label to display the time the message was sent
        timestamp = time.strftime("%H:%M", time.localtime())
        time_label = tk.Label(
            message_frame, text=timestamp, bg="#141414", fg="gray", font=("Poppins", 10),
            padx=5, pady=5,
        )
        time_label.pack(side=tk.LEFT)

        # add the chat message frame to the chat history items
        message_frame.update()
        message_frame_width = message_frame.winfo_width()
        history_items.config(width=message_frame_width)
        history_canvas.config(scrollregion=history_canvas.bbox(tk.ALL))
        history_items.pack(fill=tk.BOTH, expand=True)
        message_frame.pack(fill=tk.X)

        # clear the input entry
        input_entry.delete(0, tk.END)

        # scroll to the bottom of the chat history
        history_canvas.yview_moveto(1)

        # clear the input entry
        input_entry.delete(0, tk.END)

        # scroll to the bottom of the chat history
        history_canvas.yview_moveto(1)


# bind the send button and the Enter key to the send_message function
send_button.bind("<Button-1>", send_message)
input_entry.bind("<Return>", send_message)

# bind the mousewheel to the history canvas for scrolling
def mouse_wheel(event):
    history_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

history_canvas.bind_all("<MouseWheel>", mouse_wheel)

root.mainloop()
