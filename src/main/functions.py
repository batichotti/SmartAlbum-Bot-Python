import pyautogui
import time
import os
import pandas as pd
from tkinter import messagebox


def abrir_programa(caminho_programa):
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write(caminho_programa)
    pyautogui.press('enter')
    time.sleep(10)

def verificar_login():
    if pyautogui.locateOnScreen('.\\res\\func\\tela com new project.png') is not None:
        return True
    return False

def criar_novo_projeto(nome_projeto):
    botao_criar_projeto = pyautogui.locateCenterOnScreen('botao_criar_projeto.png')
    if botao_criar_projeto:
        pyautogui.click(botao_criar_projeto)
        time.sleep(2)
        pyautogui.write(nome_projeto)
        pyautogui.press('enter')
        
def ler_dados_excel(caminho_excel):
    try:
        df = pd.read_excel(caminho_excel)
        return df
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o Excel: {str(e)}")
        return None

def exportar_arquivos(caminho_exportar):
    botao_exportar = pyautogui.locateCenterOnScreen('botao_exportar.png')
    if botao_exportar:
        pyautogui.click(botao_exportar)
        time.sleep(2)
        pyautogui.write(caminho_exportar)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')

def processar_projetos(caminho_programa, pasta_entrada, pasta_saida):
    # Montagem da pasta de ENTRADA -> ..\\ENTRADA\\{album}\\...jpegs

    abrir_programa(caminho_programa)
    while (not verificar_login()):
        time.sleep(5)

    for folder in os.listdir(pasta_entrada):
        id_aluno = folder.replace(' ', '_')
        caminho_exportar = f"{pasta_saida}\\{id_aluno}"
        
        criar_novo_projeto(id_aluno)
        time.sleep(2)
        exportar_arquivos(caminho_exportar)