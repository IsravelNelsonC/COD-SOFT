import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Password Generator")
        self.root.geometry("500x500")
        self.root.configure(bg='#2c3e50')
        
        # Custom style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.map('TButton',
                     foreground=[('pressed', 'white'), ('active', 'white')],
                     background=[('pressed', '#34495e'), ('active', '#3498db')])
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg='#3498db', height=80)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Password Generator", 
                font=('Arial', 20, 'bold'), bg='#3498db', fg='white').pack(pady=20)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(pady=20, padx=30, fill='both', expand=True)
        
        # Length selection
        tk.Label(main_frame, text="Password Length:", 
                font=('Arial', 12), bg='#2c3e50', fg='#ecf0f1').pack(pady=(0, 5))
        
        self.length_var = tk.IntVar(value=12)
        length_slider = ttk.Scale(main_frame, from_=8, to=32, variable=self.length_var,
                                 orient='horizontal', length=300)
        length_slider.pack(pady=5)
        
        self.length_display = tk.Label(main_frame, textvariable=self.length_var, 
                                     font=('Arial', 12, 'bold'), bg='#2c3e50', fg='#3498db')
        self.length_display.pack()
        
        # Complexity options
        complexity_frame = tk.Frame(main_frame, bg='#2c3e50')
        complexity_frame.pack(pady=15)
        
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        tk.Checkbutton(complexity_frame, text="Uppercase (A-Z)", variable=self.upper_var,
                      font=('Arial', 10), bg='#2c3e50', fg='#ecf0f1', 
                      selectcolor='#2c3e50', activebackground='#2c3e50').grid(row=0, column=0, sticky='w')
        tk.Checkbutton(complexity_frame, text="Lowercase (a-z)", variable=self.lower_var,
                      font=('Arial', 10), bg='#2c3e50', fg='#ecf0f1',
                      selectcolor='#2c3e50', activebackground='#2c3e50').grid(row=1, column=0, sticky='w')
        tk.Checkbutton(complexity_frame, text="Digits (0-9)", variable=self.digits_var,
                      font=('Arial', 10), bg='#2c3e50', fg='#ecf0f1',
                      selectcolor='#2c3e50', activebackground='#2c3e50').grid(row=2, column=0, sticky='w')
        tk.Checkbutton(complexity_frame, text="Symbols (!@#)", variable=self.symbols_var,
                      font=('Arial', 10), bg='#2c3e50', fg='#ecf0f1',
                      selectcolor='#2c3e50', activebackground='#2c3e50').grid(row=3, column=0, sticky='w')
        
        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate Password", 
                                 command=self.generate_password)
        generate_btn.pack(pady=20)
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(main_frame, textvariable=self.password_var, 
                                font=('Arial', 14), bd=0, relief='flat', 
                                bg='#34495e', fg='#2ecc71', justify='center')
        password_entry.pack(fill='x', ipady=10)
        
        # Copy button
        copy_btn = ttk.Button(main_frame, text="Copy to Clipboard", 
                             command=self.copy_to_clipboard)
        copy_btn.pack(pady=10)
    
    def generate_password(self):
        length = self.length_var.get()
        chars = ''
        
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.digits_var.get():
            chars += string.digits
        if self.symbols_var.get():
            chars += string.punctuation
        
        if not chars:
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()