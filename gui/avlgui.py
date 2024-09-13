import sys
import tkinter as tk
from tkinter import messagebox
from avltree.helpers import step1, step2
from gui.text_redirector import TextRedirector

class AVLTreeGUI(tk.Tk):
    def __init__(self, avl_tree):
        super().__init__()
        self.avl_tree = avl_tree
        self.root = None
        self.title("AVL Tree GUI")
        self.geometry("800x600")
        self.inserts = 1

        self.center_screen()

        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        sys.stdout = TextRedirector(self.text, "stdout")

        self.key_entry = tk.Entry(self)
        self.key_entry.pack()

        self.insert_button = tk.Button(self, text="Insert", command=self.gui_insert_node)
        self.insert_button.pack()

        self.delete_button = tk.Button(self, text="Delete", command=self.gui_delete_node)
        self.delete_button.pack()

        self.key_entry.bind("<Return>", lambda event: self.gui_insert_node())
        self.key_entry.bind("<Delete>", lambda event: self.gui_delete_node())

    def gui_insert_node(self):
        key = self.key_entry.get()
        if key.isdigit():
            key = int(key)
            self.root = step1(self.avl_tree, key, self.root, self.inserts)
            self.inserts += 1
            #messagebox.showinfo("Insertion", f"Node {key} inserted successfully.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        self.key_entry.delete(0, tk.END)

    def gui_delete_node(self):
        key = self.key_entry.get()
        if key.isdigit():
            key = int(key)
            self.root = step2(self.avl_tree, key, self.root)
            #messagebox.showinfo("Deletion", f"Node {key} deleted successfully.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        self.key_entry.delete(0, tk.END)
        
    def center_screen(self):
        self.update()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"+{x}+{y}")