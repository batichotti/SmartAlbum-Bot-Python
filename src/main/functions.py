import pyautogui
from time import sleep
import os

def abrir_programa(caminho_programa):
    try:
        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.write(caminho_programa)
        pyautogui.press("enter")
        sleep(10)
    except Exception as e:
        print(f"Erro ao abrir o programa: {e}")

def get_botao(image_path):
    try:
        return pyautogui.locateCenterOnScreen(image_path)
    except Exception as e:
        print(f"Erro ao localizar botão {image_path}: {e}")
        return None

def criar_novo_projeto(id):
    try:
        botao_criar_projeto = get_botao('./res/func/bt_novo_projeto.png')
        if botao_criar_projeto:
            pyautogui.click(botao_criar_projeto)
            sleep(1)

        botao_album = get_botao('./res/func/bt_album.png')
        if botao_album:
            pyautogui.click(botao_album)
            sleep(2)

        botao_personalizado = get_botao('./res/func/bt_personalizado.png') or get_botao('./res/func/bt_personalizado2.png')
        if botao_personalizado:
            pyautogui.click(botao_personalizado)
            sleep(1)

        botao_new_preset = get_botao('./res/func/bt_new_preset.png')
        if botao_new_preset:
            pyautogui.click(botao_new_preset)
            sleep(1)
            botao_23x60 = get_botao('./res/func/23x60.png')
            if botao_23x60:
                pyautogui.click(botao_23x60)
                sleep(1)
        else:
            print("Botão de novo preset não encontrado, usando fallback.")
            pyautogui.press("enter")
            sleep(1)
            pyautogui.press("enter")
            sleep(1)
            pyautogui.write(f"{id}")
            pyautogui.press("enter")

        return True
    except:
        return False

def importar_imagens(images_folder):
    botao_import = get_botao('./res/func/bt_importar_imagens.png')
    if botao_import:
        pyautogui.click(botao_import)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(images_folder)
        pyautogui.press("right")
        pyautogui.press("enter")
        pyautogui.press("enter")
        sleep(2)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")

        while get_botao('./res/func/load_importando_imagens.png') is not None:
            sleep(10)
        return True
    else:
        return False

def salvar_arquivos(caminho_exportar):
    botao_exportar = get_botao('./res/func/botao_exportar.png')
    if botao_exportar:
        pyautogui.click(botao_exportar)
        sleep(2)
        pyautogui.write(caminho_exportar)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
        return True
    else:
        return False

def processar_projetos(caminho_programa, pasta_entrada, pasta_saida):
    # abrir_programa(caminho_programa)
    for folder in os.listdir(pasta_entrada):
        id_aluno = folder.replace(' ', '_')

        while not criar_novo_projeto(id_aluno):
            sleep(1)

        while not importar_imagens(f"{pasta_entrada}/{folder}"):
            sleep(1)
        
        while not salvar_arquivos(pasta_saida):
            sleep(1)

        break
