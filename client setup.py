import socket
import threading
import tkinter as tk 
from tkinter import simpledialog, filedialog
import os

ip = "192.168.100.7" 
port = 55554 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((ip, port))

name = simpledialog.askstring("Input", "Enter your name", parent=tk.Tk()) 

client.send(name.encode("utf-8")) 

window = tk.Tk()
window.title("Chat App")
window.configure(bg="#2C2C2C")  

name_label = tk.Label(window, text=f"Logged in as: {name}", bg="#2C2C2C", fg="white")
name_label.pack()

message_box = tk.Text(window, height=15, width=50, bg="#2C2C2C", fg="white", insertbackground="white")
message_box.pack(pady=10)
message_box.config(state=tk.DISABLED)  

message_entry = tk.Entry(window, width=50, bg="#404040", fg="white", insertbackground="white")
message_entry.pack(pady=10)

def send_message(event=None): 
    message = message_entry.get()
    if message:
        formatted_message = f"{name}: {message}"
        client.send(formatted_message.encode("utf-8"))
        message_entry.delete(0, tk.END)
        
        update_message_box(formatted_message)

window.bind("<Return>", send_message) 

send_button = tk.Button(window, text="Send", command=send_message, bg="#404040", fg="white")
send_button.pack()

def receive(): 
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            
            if message.startswith("FILE:"):
                filename = message[5:]
                receive_file(filename)
            else:
                update_message_box(message)
        except:
            print("An error occurred while receiving messages.")
            client.close()
            break

def update_message_box(message): 
    message_box.config(state=tk.NORMAL)  
    message_box.insert(tk.END, message + "\n")
    message_box.config(state=tk.DISABLED)  
    message_box.see(tk.END)

def send_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        filename = os.path.basename(filepath)
        client.send(f"FILE:{filename}".encode("utf-8"))
        with open(filepath, "rb") as f:
            data = f.read()
            client.sendall(data)
        update_message_box(f"You sent a file: {filename}")

def receive_file(filename):
    with open(filename, "wb") as f:
        data = client.recv(1024)
        while data:
            f.write(data)
            data = client.recv(1024)
    update_message_box(f"Received file: {filename}")

file_button = tk.Button(window, text="Send File", command=send_file, bg="#404040", fg="white")
file_button.pack()

receive_thread = threading.Thread(target=receive) 
receive_thread.start()

window.mainloop()
