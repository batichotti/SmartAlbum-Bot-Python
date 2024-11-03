import tkinter as tk
from tkinter import filedialog, messagebox
from functions import processar_projetos, ler_dados_excel

class SmartAlbumApp:
    def __init__(self, root):
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 400
        self.BG_COLOR = "#f0f0f0"
        self.LABEL_FONT = ("Helvetica", 12)
        self.ENTRY_WIDTH = 50
        self.BUTTON_FONT = ("Helvetica", 10, "bold")
        self.BUTTON_BG = "#4CAF50"
        self.BUTTON_FG = "#FFFFFF"
        self.PADY_LABEL = 10
        self.PADY_BUTTON = 15

        self.root = root
        self.root.title("SmartAlbum Bot - by: Matt Cohuzer Batichotti")
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.config(bg=self.BG_COLOR)
        
        self.root.iconbitmap(".\\res\\theme\\Logo-CZR5.ico")

        self.caminho_programa = "C:\\Program Files\\Pixellu SmartAlbum\\SmartAlbums.exe"

        self.create_widgets()

    def create_widgets(self):
        # tk.Label(self.root, text="Arquivo Excel:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        # self.entry_excel = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        # self.entry_excel.pack(pady=5)
        # tk.Button(self.root, text="Selecionar Excel", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
        #           command=self.selecionar_excel).pack(pady=self.PADY_BUTTON)

        tk.Label(self.root, text="Pasta Selecionadas com as Imagens:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_caminho_entrada = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_caminho_entrada.pack(pady=5)
        tk.Button(self.root, text="Selecionar Pasta (Imagens)", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_pasta_programa).pack(pady=self.PADY_BUTTON)

        tk.Label(self.root, text="Pasta de Salvamento:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_pasta_salvamento = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_pasta_salvamento.pack(pady=5)
        tk.Button(self.root, text="Selecionar Pasta (Aonde Salvar)", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_pasta_salvamento).pack(pady=self.PADY_BUTTON)

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

    def selecionar_pasta_salvamento(self):
        caminho = filedialog.askdirectory(title="Selecione a Pasta de Salvamento")
        if caminho:
            self.entry_pasta_salvamento.delete(0, tk.END)
            self.entry_pasta_salvamento.insert(0, caminho)

    def selecionar_pasta_programa(self):
        caminho = filedialog.askdirectory(title="Selecione a Pasta do Programa")
        if caminho:
            self.entry_caminho_entrada.delete(0, tk.END)
            self.entry_caminho_entrada.insert(0, caminho)

    def processar(self):
        caminho_pasta_salvamento = self.entry_pasta_salvamento.get()
        caminho_pasta_entrada = self.entry_caminho_entrada.get()
        caminho_programa = self.caminho_programa

        if not caminho_pasta_salvamento or not caminho_programa:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return
        
        processar_projetos(caminho_programa, caminho_pasta_entrada, caminho_pasta_salvamento)

        # try:
        #     df_projetos = ler_dados_excel(caminho_excel)
        #     if df_projetos is not None:
        #         processar_projetos(caminho_programa, caminho_pasta_entrada, caminho_pasta_salvamento)
        #         messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
        #     else:
        #         messagebox.showerror("Erro", "Erro ao ler o arquivo Excel.")
        # except Exception as e:
        #     messagebox.showerror("Erro", f"Erro ao processar: {str(e)}")

def run_interface():
    root = tk.Tk()
    app = SmartAlbumApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_interface()
