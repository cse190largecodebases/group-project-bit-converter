import tkinter as tk
from tkinter import ttk
import subprocess
import git

class SourceControlGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Source Control")
        self.repo = None  # repository class variable for running GitPython methods
        
        # Create the tabs
        self.tab_control = ttk.Notebook(self)
        self.repo_tab()
        self.add_tab()
        self.commit_tab()
        self.push_tab()
        # Add more tabs for other Git commands
        
        self.tab_control.pack(expand=True, fill=tk.BOTH)

    def repo_tab(self):
        repo_frame = ttk.Frame(self.tab_control)
        repo_button = ttk.Button(repo_frame, text="Select Repository", command=self.git_repo)
        repo_button.pack(padx=10, pady=10)
        self.tab_control.add(repo_frame, text="Select Repository")
    
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
    
    def git_repo(self):
        # Initialize or select repo based on user input for folder location
        repo_window = tk.Toplevel(self)
        repo_window.title("Select Repository")
        
        repo_frame = ttk.Frame(repo_window)
        repo_label = ttk.Label(repo_frame, text="Enter Path of Folder. Initializes Git Repository if one isn't Found. \ne.g. /Users/name/repositoryfolder")
        repo_label.pack(padx=10, pady=10)
        
        repo_entry = ttk.Entry(repo_frame, width=50)
        repo_entry.pack(padx=10, pady=10)
        
        repo_button = ttk.Button(repo_frame, text="Select Folder", command=lambda: self.perform_repo(repo_entry.get()))
        repo_button.pack(padx=10, pady=10)
        
        repo_frame.pack()

    def perform_repo(self, message):
        message = message.strip()
        print(message) # temporary message for development
        self.repo = git.Repo.init(message)

    def git_add(self):
        # Run the 'git add' command using GitPython
        add_window = tk.Toplevel(self)
        add_window.title("Git Add")
        
        add_frame = ttk.Frame(add_window)
        repo_name = "No Repository Selected. Please Select a Repository First"
        if(self.repo is not None): repo_name = str(self.repo.working_dir)
        add_label = ttk.Label(add_frame, text="Enter File Path Excluding Repository Path. e.g. file.py or folder/file.py" + "\nRepository Selected: " + repo_name)
        add_label.pack(padx=10, pady=10)
        
        add_entry = ttk.Entry(add_frame, width=50)
        add_entry.pack(padx=10, pady=10)
        
        add_button = ttk.Button(add_frame, text="Add", command=lambda: self.perform_add(add_entry.get()))
        add_button.pack(padx=10, pady=10)
        
        add_frame.pack()

    def perform_add(self, message):
        self.repo.index.add(message)
        print(self.repo.git.status()) # temporary message for development
    
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
