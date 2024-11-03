import tkinter as tk
from tkinter import filedialog, messagebox
from functions import processar_projetos, ler_dados_excel

def selecionar_excel(entry_excel):
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo Excel",
        filetypes=[("Arquivo Excel", "*.xlsx")],
    )
    if caminho:
        entry_excel.delete(0, tk.END)
        entry_excel.insert(0, caminho)

def selecionar_programa(entry_programa):
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo do Programa"
    )
    if caminho:
        entry_programa.delete(0, tk.END)
        entry_programa.insert(0, caminho)

def processar(entry_excel, entry_programa):
    caminho_excel = entry_excel.get()
    caminho_programa = entry_programa.get()
    
    if not caminho_excel or not caminho_programa:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return
    
    df_projetos = ler_dados_excel(caminho_excel)
    
    if df_projetos is not None:
        try:
            processar_projetos(caminho_programa, df_projetos)
            messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar: {str(e)}")

def run_interface():
    root = tk.Tk()
    root.title("SmartAlbum Bot v0.1")
    root.geometry("400x200")

    label_excel = tk.Label(root, text="Arquivo Excel:")
    label_excel.pack(pady=5)
    entry_excel = tk.Entry(root, width=40)
    entry_excel.pack(pady=5)
    btn_excel = tk.Button(root, text="Selecionar Excel", command=lambda: selecionar_excel(entry_excel))
    btn_excel.pack(pady=5)

    label_programa = tk.Label(root, text="Caminho do Programa:")
    label_programa.pack(pady=5)
    entry_programa = tk.Entry(root, width=40)
    entry_programa.pack(pady=5)
    btn_programa = tk.Button(root, text="Selecionar Programa", command=lambda: selecionar_programa(entry_programa))
    btn_programa.pack(pady=5)

    btn_processar = tk.Button(root, text="Processar", command=lambda: processar(entry_excel, entry_programa))
    btn_processar.pack(pady=20)

    root.mainloop()
