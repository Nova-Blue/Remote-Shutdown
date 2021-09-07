from cryptography.fernet import Fernet
import tkinter as tk
import tkinter.filedialog


root = tk.Tk()
root.attributes("-alpha", 0)
f = tk.filedialog.asksaveasfile(parent=root, mode="wb", title="Choose location for the secret key:")
root.destroy()

key = Fernet.generate_key()
f.write(key)
f.close()
