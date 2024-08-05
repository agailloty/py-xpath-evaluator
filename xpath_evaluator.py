import tkinter as tk
from tkinter import filedialog, messagebox
from lxml import etree

class XPathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XPath Evaluator")
        self.root.geometry("800x600")
        self.root.config(bg="white")
        
        # Menu
        menu = tk.Menu(root)
        root.config(menu=menu)
        
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=root.quit)
        
        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="À propos", menu=help_menu)
        help_menu.add_command(label="À propos", command=self.show_about)
        
        # Main Frame
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # XPath Entry
        self.xpath_entry = tk.Entry(self.frame, width=50)
        self.xpath_entry.pack(pady=10)
        
        # Evaluate Button
        self.eval_button = tk.Button(self.frame, text="Évaluer XPath", command=self.evaluate_xpath)
        self.eval_button.pack(pady=5)
        
        # Results Listbox
        self.results_listbox = tk.Listbox(self.frame, width=50, height=20)
        self.results_listbox.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.results_listbox, orient="vertical")
        self.scrollbar.config(command=self.results_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_listbox.config(yscrollcommand=self.scrollbar.set)
        
        # Loaded HTML Document
        self.html_doc = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    self.html_doc = etree.HTML(file.read())
                    messagebox.showinfo("Succès", "Fichier chargé avec succès")
                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier: {e}")

    def evaluate_xpath(self):
        if not self.html_doc:
            messagebox.showwarning("Avertissement", "Veuillez charger un fichier HTML d'abord")
            return
        
        xpath_query = self.xpath_entry.get()
        if not xpath_query:
            messagebox.showwarning("Avertissement", "Veuillez entrer une requête XPath")
            return
        
        try:
            results = self.html_doc.xpath(xpath_query)
            self.results_listbox.delete(0, tk.END)
            for result in results:
                self.results_listbox.insert(tk.END, str(result.text))
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'évaluation XPath: {e}")

    def show_about(self):
        messagebox.showinfo("À propos", "Application d'évaluation XPath avec Tkinter\n© 2024 Axel-Cleris")

if __name__ == "__main__":
    root = tk.Tk()
    app = XPathApp(root)
    root.mainloop()
