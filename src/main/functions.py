import pyautogui
import time
import os

def abrir_programa(caminho_programa):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write(caminho_programa)
    pyautogui.press("enter")
    time.sleep(10)

def verifica_tela_inicial():
    # Aqui, você pode usar uma condição para garantir que a tela está visível
    return pyautogui.locateOnScreen('.\\res\\func\\tela_com_new_project.png') is not None

def criar_novo_projeto(id, output_folder):
    botao_criar_projeto = pyautogui.locateCenterOnScreen('.\\res\\func\\bt_novo_projeto.png')
    if botao_criar_projeto:
        pyautogui.click(botao_criar_projeto)
        time.sleep(1)
    else:
        print("Botão de criar novo projeto não encontrado.")
        return

    botao_album = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_album.png")
    if botao_album:
        pyautogui.click(botao_album)
        time.sleep(2)

    try:
        botao_personalizado = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_personalizado.png")
    except:
        time.sleep(1)
        try:
            botao_personalizado = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_personalizado2.png")
        except:
            botao_personalizado = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_personalizado.png")

    if botao_personalizado:
        pyautogui.click(botao_personalizado)
        time.sleep(1)
    else:
        print("Botão personalizado não encontrado.")
        return

    try:
        botao_new_preset = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_new_preset.png")
        if botao_new_preset:
            pyautogui.click(botao_new_preset)
            time.sleep(1)
            botao_23x60 = pyautogui.locateCenterOnScreen(".\\res\\func\\23x60.png")
            if botao_23x60:
                pyautogui.click(botao_23x60)
                time.sleep(1)
        else:
            print("Botão de novo preset não encontrado, usando fallback.")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.write(f"{id}")
            pyautogui.press("enter")
    except Exception as e:
        print(f"Erro ao tentar criar novo projeto: {e}")

def importar_imagens(images_folder):
    botao_import = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_importar_imagens.png")
    if botao_import:
        pyautogui.click(botao_import)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(images_folder)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")
        
        while pyautogui.locateOnScreen(".\\res\\func\\load_importando_imagens.png") is not None:
            time.sleep(10)  # Espera enquanto as imagens estão sendo importadas
    else:
        print("Botão de importar imagens não encontrado.")

def salvar_arquivos(caminho_exportar):
    botao_exportar = pyautogui.locateCenterOnScreen('.\\res\\func\\botao_exportar.png')
    if botao_exportar:
        pyautogui.click(botao_exportar)
        time.sleep(2)
        pyautogui.write(caminho_exportar)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
    else:
        print("Botão de exportar não encontrado.")

def processar_projetos(caminho_programa, pasta_entrada, pasta_saida):
    # abrir_programa(caminho_programa)
    
    # while not verifica_tela_inicial():
    #     time.sleep(5)

    for folder in os.listdir(pasta_entrada):
        id_aluno = folder.replace(' ', '_')
        
        criar_novo_projeto(id_aluno, pasta_saida)
        time.sleep(2)
        importar_imagens(f"{pasta_entrada}\\{folder}")
        
        salvar_arquivos(pasta_saida)
        break
