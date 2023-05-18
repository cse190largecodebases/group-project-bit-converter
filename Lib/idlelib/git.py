import tkinter as tk
from tkinter import ttk
import subprocess

class GitConfigurationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Git Configuration")
        
        # Create the tabs
        self.tab_control = ttk.Notebook(self)
        self.add_tab()
        self.commit_tab()
        self.push_tab()
        # Add more tabs for other Git commands
        
        self.tab_control.pack(expand=True, fill=tk.BOTH)
    
    def add_tab(self):
        add_frame = ttk.Frame(self.tab_control)
        add_button = ttk.Button(add_frame, text="Add", command=self.git_add)
        add_button.pack(padx=10, pady=10)
        self.tab_control.add(add_frame, text="Add")
    
    def commit_tab(self):
        commit_frame = ttk.Frame(self.tab_control)
        commit_button = ttk.Button(commit_frame, text="Commit", command=self.git_commit)
        commit_button.pack(padx=10, pady=10)
        self.tab_control.add(commit_frame, text="Commit")
    
    def push_tab(self):
        push_frame = ttk.Frame(self.tab_control)
        push_button = ttk.Button(push_frame, text="Push", command=self.git_push)
        push_button.pack(padx=10, pady=10)
        self.tab_control.add(push_frame, text="Push")
    
    def git_add(self):
        # Run the 'git add' command using subprocess
        result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            print(output)
    
    def git_commit(self):
        # Run the 'git commit' command using subprocess
        commit_window = tk.Toplevel(self)
        commit_window.title("Git Commit")
        
        commit_frame = ttk.Frame(commit_window)
        commit_label = ttk.Label(commit_frame, text="Commit Message:")
        commit_label.pack(padx=10, pady=10)
        
        commit_entry = ttk.Entry(commit_frame, width=50)
        commit_entry.pack(padx=10, pady=10)
        
        commit_button = ttk.Button(commit_frame, text="Commit", command=lambda: self.perform_commit(commit_entry.get()))
        commit_button.pack(padx=10, pady=10)
        
        commit_frame.pack()
    
    def perform_commit(self, message):
        result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            print(output)
    
    def git_push(self):
        # Run the 'git push' command using subprocess
        result = subprocess.run(["git", "push"], capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            print(output)
