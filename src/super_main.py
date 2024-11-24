import tkinter as tk
from tkinter import filedialog, messagebox
import os
from time import sleep
import pyautogui

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

        self.create_widgets()

    def create_widgets(self):
        # Pasta de Imagens
        tk.Label(self.root, text="Pasta Selecionada com as Imagens:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_caminho_entrada = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_caminho_entrada.pack(pady=5)
        tk.Button(self.root, text="Selecionar Pasta (Imagens)", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_pasta_programa).pack(pady=self.PADY_BUTTON)

        # Pasta de Salvamento
        tk.Label(self.root, text="Pasta de Salvamento:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        self.entry_pasta_salvamento = tk.Entry(self.root, width=self.ENTRY_WIDTH)
        self.entry_pasta_salvamento.pack(pady=5)
        tk.Button(self.root, text="Selecionar Pasta (Onde Salvar)", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.selecionar_pasta_salvamento).pack(pady=self.PADY_BUTTON)

        # Minutos de Espera
        tk.Label(self.root, text="Minutos de Espera:", bg=self.BG_COLOR, font=self.LABEL_FONT).pack(pady=self.PADY_LABEL)
        validate_command = self.root.register(self.validar_inteiro)
        self.entry_minutos = tk.Entry(self.root, width=self.ENTRY_WIDTH, validate="key", validatecommand=(validate_command, "%P"))
        self.entry_minutos.pack(pady=5)

        # Botão Processar
        tk.Button(self.root, text="Processar", font=self.BUTTON_FONT, bg=self.BUTTON_BG, fg=self.BUTTON_FG,
                  command=self.processar).pack(pady=self.PADY_BUTTON)

    def validar_inteiro(self, valor):
        if valor.isdigit() or valor == "":
            return True
        return False

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
        minutos = self.entry_minutos.get()

        if not caminho_pasta_salvamento or not caminho_pasta_entrada or not minutos:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            minutos = int(minutos)
        except ValueError:
            messagebox.showerror("Erro", "O campo 'Tempo em Minutos' deve conter um digito numerico como valor.")
            return

        texto_confirmacao = (
            "Regras para o funcionamento adequado do programa:\n\n"
            "1 - Nada de acentos nas palavras nos caminhos do computador/HD, verificar manualmente.\n\n"
            "Atendidas as regras, pressione SIM para continuar a tarefa."
        )

        resposta = messagebox.askquestion(
            "Confirmar Processamento", 
            texto_confirmacao, 
            icon="warning"
        )

        if resposta == "yes":
            processar_projetos(caminho_pasta_entrada, caminho_pasta_salvamento, minutos, False)
        else:
            return

def run_interface():
    root = tk.Tk()
    app = SmartAlbumApp(root)
    root.mainloop()

def abrir_programa(caminho_programa):
    try:
        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.write(caminho_programa)
        pyautogui.press("enter")
        sleep(10)
        return True
    except Exception as e:
        print(f"Erro ao abrir o programa: {e}")
        return False

def get_botao(image_path):
    try:
        return pyautogui.locateCenterOnScreen(image_path)
    except Exception as e:
        print(f"Erro ao localizar botão {image_path}: {e}")
        return None

def exception_overwrite():
    """ Function to select YES option when the system throws a overwrite exception """
    sleep(1)
    for i in range(2):
        botao_substituir = get_botao("./images/deseja_substituilo.png")
        if botao_substituir:
            pyautogui.press("left")
            pyautogui.press("enter")
            sleep(2)
    print("All good - Exception handled")

def criar_novo_projeto(id, saida):
    try:
        sleep(5)
        pyautogui.click(x=1760, y=200)  # Botão Novo Projeto
        pyautogui.click(x=1760, y=260)  # Botão Album

        sleep(1)
        pyautogui.click(x=1360, y=300)  # Botão Personalizado

        sleep(1)
        pyautogui.click(x=1106, y=403)  # Botão Novo Preset
        pyautogui.click(x=1138, y=439)  # Botão 23x60

        pyautogui.click(x=1661, y=954)  # Proximo
        sleep(1)
        
        pyautogui.click(x=1670, y=820)  # Iniciar
        sleep(3/2)
        
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(f"{saida}")
        pyautogui.press("right")
        pyautogui.press("enter")
        sleep(1)
        
        for i in range(7):
            pyautogui.press("tab")  # Tabulating to find the writable field
        pyautogui.write(f"{id}")
        pyautogui.press("enter")
        exception_overwrite()  # Handle exceptions (overwrite)
        sleep(1)
        return True
    except:
        return False

def importar_imagens(images_folder, id):
    try:
        sleep(4)
        pyautogui.hotkey("ctrl", "i")
        sleep(1)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(f"{images_folder}/{id}")
        pyautogui.press("right")
        pyautogui.press("enter")
        sleep(1)
        
        for i in range(4):
            pyautogui.press("tab")
        
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")
        sleep(1)
        return True
    except:
        return False


def salvar_arquivos(minutes):
    try:
        sleep(60 * minutes + 15)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
        return True
    except:
        return False

def processar_projetos(pasta_entrada, pasta_saida, minutes, abrir):
    
    pasta_entrada = pasta_entrada.replace('/', '\\')    
    pasta_saida = pasta_saida.replace('/', '\\')    
    
    for folder in os.listdir(pasta_entrada):
        if os.path.isdir(os.path.join(pasta_entrada, folder)):
            id_aluno = folder.replace(' ', '_')
            criar_novo_projeto(id_aluno, pasta_saida)
            importar_imagens(pasta_entrada, folder)
            salvar_arquivos(minutes)
    pyautogui.alert('Processamento finalizado com sucesso!', 'Sucesso!', button='OK')

if __name__ == "__main__":
    run_interface()
