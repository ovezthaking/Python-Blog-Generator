# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from blog_generator import generate_blog
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BlogGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Blogów AI")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Configure style
        self.setup_styles()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="🤖 Generator Blogów AI", 
            style="Title.TLabel"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Topic input
        ttk.Label(main_frame, text="Temat artykułu:", style="Heading.TLabel").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5)
        )
        
        self.topic_entry = ttk.Entry(main_frame, font=("Arial", 12), width=50)
        self.topic_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Generate button
        self.generate_btn = ttk.Button(
            main_frame,
            text="🚀 Generuj Artykuł",
            command=self.generate_blog_thread,
            style="Generate.TButton"
        )
        self.generate_btn.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Result area
        ttk.Label(main_frame, text="Wygenerowany artykuł:", style="Heading.TLabel").grid(
            row=4, column=0, sticky=(tk.W, tk.N), pady=(0, 5)
        )
        
        # Text area with scrollbar
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=("Arial", 11),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        self.result_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=7, column=0, columnspan=2, pady=(0, 10))
        
        # Copy button
        self.copy_btn = ttk.Button(
            buttons_frame,
            text="📋 Skopiuj",
            command=self.copy_to_clipboard,
            state="disabled"
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Save button
        self.save_btn = ttk.Button(
            buttons_frame,
            text="💾 Zapisz",
            command=self.save_to_file,
            state="disabled"
        )
        self.save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = ttk.Button(
            buttons_frame,
            text="🗑️ Wyczyść",
            command=self.clear_all
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Gotowy do generowania")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief="sunken",
            style="Status.TLabel"
        )
        status_bar.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Bind Enter key to generate
        self.topic_entry.bind('<Return>', lambda event: self.generate_blog_thread())
        
        # Focus on topic entry
        self.topic_entry.focus()
    
    def setup_styles(self):
        style = ttk.Style()
        
        # Title style
        style.configure("Title.TLabel", 
                       font=("Arial", 18, "bold"),
                       foreground="#2c3e50")
        
        # Heading style
        style.configure("Heading.TLabel",
                       font=("Arial", 12, "bold"),
                       foreground="#34495e")
        
        # Generate button style
        style.configure("Generate.TButton",
                       font=("Arial", 12, "bold"))
        
        # Status style
        style.configure("Status.TLabel",
                       font=("Arial", 9),
                       foreground="#7f8c8d")
        
        # Progress bar style
        style.configure("Custom.Horizontal.TProgressbar",
                       troughcolor="#ecf0f1",
                       background="#3498db")
    Dobra jak sprawić, żeby przy importowaniu generate_blog do innych plików pythonowych nie była wykonywana reszta kodu od "working = True..." a było to wykonywane tylko i wyłącznie przy uruchomieniu blog_generator.py
    def generate_blog_thread(self):
        # Run generation in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self.generate_blog_content)
        thread.daemon = True
        thread.start()
    
    def generate_blog_content(self):
        topic = self.topic_entry.get().strip()
        
        if not topic:
            messagebox.showwarning("Uwaga", "Proszę podać temat artykułu!")
            return
        
        # Check if API key exists
        if not os.getenv('OPENAI_API_KEY'):
            messagebox.showerror(
                "Błąd", 
                "Brak klucza API!\nUpewnij się, że masz plik .env z OPENAI_API_KEY"
            )
            return
        
        # Disable button and show progress
        self.generate_btn.config(state="disabled")
        self.progress.start()
        self.status_var.set("Generuję artykuł...")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Generowanie w toku...\n\nProszę czekać...")
        
        try:
            # Generate blog content
            blog_content = generate_blog(topic)
            
            # Update GUI in main thread
            self.root.after(0, self.update_result, blog_content, True)
            
        except Exception as e:
            error_msg = str(e)
            if "insufficient_quota" in error_msg or "429" in error_msg:
                error_msg = ("Przekroczono limit kosztów API OpenAI.\n\n"
                           "Sprawdź swoje konto na platform.openai.com:\n"
                           "• Dodaj środki do konta\n"
                           "• Sprawdź miesięczny limit wydatków\n"
                           "• Sprawdź czy klucz API jest aktywny")
            elif "401" in error_msg:
                error_msg = "Nieprawidłowy klucz API. Sprawdź plik .env"
            else:
                error_msg = f"Wystąpił błąd: {error_msg}"
            
            self.root.after(0, self.update_result, error_msg, False)
    
    def update_result(self, content, success):
        # Stop progress and enable button
        self.progress.stop()
        self.generate_btn.config(state="normal")
        
        # Clear and update text
        self.result_text.delete(1.0, tk.END)
        
        if success:
            self.result_text.insert(tk.END, content)
            self.status_var.set("Artykuł wygenerowany pomyślnie!")
            self.copy_btn.config(state="normal")
            self.save_btn.config(state="normal")
        else:
            self.result_text.insert(tk.END, f"❌ Błąd:\n\n{content}")
            self.status_var.set("Wystąpił błąd podczas generowania")
            self.copy_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
    
    def copy_to_clipboard(self):
        content = self.result_text.get(1.0, tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.status_var.set("Skopiowano do schowka!")
            # Reset status after 2 seconds
            self.root.after(2000, lambda: self.status_var.set("Gotowy do generowania"))
    
    def save_to_file(self):
        content = self.result_text.get(1.0, tk.END).strip()
        if not content:
            return
        
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Pliki tekstowe", "*.txt"),
                ("Pliki Markdown", "*.md"),
                ("Wszystkie pliki", "*.*")
            ],
            title="Zapisz artykuł"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.status_var.set(f"Zapisano do: {filename}")
                # Reset status after 3 seconds
                self.root.after(3000, lambda: self.status_var.set("Gotowy do generowania"))
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{str(e)}")
    
    def clear_all(self):
        self.topic_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.copy_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        self.status_var.set("Gotowy do generowania")
        self.topic_entry.focus()

def main():
    root = tk.Tk()
    app = BlogGeneratorGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_reqwidth() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_reqheight() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
