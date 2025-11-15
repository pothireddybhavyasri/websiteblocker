import os
import tkinter as tk
from tkinter import END, Label, messagebox

# Set path and IP for blocking
host_path = r'C:\Windows\System32\drivers\etc\hosts' if os.name == 'nt' else '/etc/hosts'
ip_address = '127.0.0.1'

# Function to block websites
def block():
    ws_list = en1.get("1.0", END)
    ws = [w.strip() for w in ws_list.split(",") if w.strip()]
    try:
        with open(host_path, 'r+') as host_file:
            file = host_file.read()
            for w in ws:
                if w in file or f"www.{w}" in file:
                    msg = "Already Blocked!"
                else:
                    host_file.write(ip_address + " " + w + '\n')
                    host_file.write(ip_address + " www." + w + '\n')
                    msg = "Website(s) Blocked!"
        Label(root, text=msg, font=('Arial', 12, 'bold'), bg='#515151', fg='white').place(x=90, y=160)
    except PermissionError:
        messagebox.showerror("Permission Denied", "Run this program as Administrator.")

# Function to unblock websites
def unblock():
    ws_list = en1.get("1.0", END)
    ws = [w.strip() for w in ws_list.split(",") if w.strip()]
    try:
        with open(host_path, 'r+') as host_file:
            lines = host_file.readlines()
            host_file.seek(0)
            for line in lines:
                if not any(w in line for w in ws):
                    host_file.write(line)
            host_file.truncate()
        Label(root, text="Website(s) Unblocked!", font=('Arial', 12, 'bold'), bg='#515151', fg='white').place(x=90, y=160)
    except PermissionError:
        messagebox.showerror("Permission Denied", "Run this program as Administrator.")


root = tk.Tk()
root.title("Website Blocker")
root.geometry("400x260")
root.config(bg="#515151")
root.resizable(False, False)

Label(root, text="Website Blocker", font=('Arial', 16, 'bold'), bg='#515151', fg='white').pack(pady=10)

Label(root, text="Enter websites (comma-separated):", font=('Arial', 10), bg='#515151', fg='white').place(x=20, y=60)

en1 = tk.Text(root, height=2, width=40, font=('Arial', 10))
en1.place(x=20, y=85)

tk.Button(root, text="Block", font=('Arial', 10, 'bold'), bg="red", fg="white", width=10, command=block).place(x=80, y=200)

tk.Button(root, text="Unblock", font=('Arial', 10, 'bold'), bg="green", fg="white", width=10, command=unblock).place(x=220, y=200)

root.mainloop()
