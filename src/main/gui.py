import tkinter as tk
from tkinter import filedialog, messagebox
from functions import processar_projetos, ler_dados_excel

class SmartAlbumApp:
    def __init__(self, root):
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 350
        self.BG_COLOR = "#f0f0f0"
        self.LABEL_FONT = ("Helvetica", 12)
        self.ENTRY_WIDTH = 50
        self.BUTTON_FONT = ("Helvetica", 10, "bold")
        self.BUTTON_BG = "#4CAF50"
        self.BUTTON_FG = "#FFFFFF"
        self.PADY_LABEL = 10
        self.PADY_BUTTON = 15

        self.root = root
        self.root.title("SmartAlbum Bot v0.1")
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.config(bg=self.BG_COLOR)
        
        self.root.iconbitmap("src\\res\\theme\\Logo-CZR5.ico")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Arquivo Excel:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_excel = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_excel.pack(pady=5)
        tk.Button(self.root, text="Selecionar Excel", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_excel).pack(pady=self.PADY_BUTTON)

        tk.Label(self.root, text="Caminho do Programa:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_programa = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_programa.pack(pady=5)
        tk.Button(self.root, text="Selecionar Programa", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_programa).pack(pady=self.PADY_BUTTON)

        # Botão de processar
        tk.Button(self.root, text="Processar", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.processar).pack(pady=self.PADY_BUTTON)

    def selecionar_arquivo(self, entry, tipo_arquivo, extensao):
        caminho = filedialog.askopenfilename(
            title=f"Selecione o {tipo_arquivo}",
            filetypes=[(f"Arquivo {tipo_arquivo}", extensao)],
        )
        if caminho:
            entry.delete(0, tk.END)
            entry.insert(0, caminho)

    def selecionar_excel(self):
        self.selecionar_arquivo(self.entry_excel, "Excel", "*.xlsx")

    def selecionar_programa(self):
        self.selecionar_arquivo(self.entry_programa, "Programa", "*.*")

    def processar(self):
        caminho_excel = self.entry_excel.get()
        caminho_programa = self.entry_programa.get()

        if not caminho_excel or not caminho_programa:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            df_projetos = ler_dados_excel(caminho_excel)
            if df_projetos is not None:
                processar_projetos(caminho_programa, df_projetos)
                messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
            else:
                messagebox.showerror("Erro", "Erro ao ler o arquivo Excel.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar: {str(e)}")

def run_interface():
    root = tk.Tk()
    app = SmartAlbumApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_interface()
