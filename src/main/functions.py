import pyautogui
import time
import os


def abrir_programa(caminho_programa):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    # for char in caminho_programa:
    #     if char == " ":
    #         pyautogui.press('space')
    #     else:
    #         pyautogui.write(char) 
    pyautogui.typewrite(caminho_programa)
    pyautogui.press("right")
    pyautogui.press("enter")
    time.sleep(10)

def verifica_tela_inicial():
    if pyautogui.locateOnScreen('.\\res\\func\\tela_com_new_project.png') is not None: #não usa e ta dando b.o.
        return True
    return False

def criar_novo_projeto(id, output_folder):

    botao_criar_projeto = pyautogui.locateCenterOnScreen('.\\res\\func\\bt_novo_projeto.png')
    if botao_criar_projeto:
        pyautogui.click(botao_criar_projeto)
        time.sleep(1)
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

    try:
        botao_new_preset = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_new_preset.png")
        if botao_new_preset:
            pyautogui.click(botao_new_preset)
            time.sleep(1)
            botao_23x60 = pyautogui.locateCenterOnScreen(".\\res\\func\\23x60.png")
            if botao_23x60:
                pyautogui.click(botao_23x60)
                time.sleep(1)
    except:
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1) # LEMBRADE MUDAR ISSO PELO BVEM DA DONA MARCELA
        pyautogui.typewrite(f"{id}")
        pyautogui.press("right")
        pyautogui.press("enter")

def importar_imagens(images_folder):
    botao_import = pyautogui.locateCenterOnScreen(".\\res\\func\\bt_importar_imagens.png")
    if botao_import:
        pyautogui.click(botao_import)
        pyautogui.hotkey("ctrl","l")
        pyautogui.typewrite(images_folder)
        time.sleep(1)
        pyautogui.hotkey("crtl", "a")
        pyautogui.press("enter")
        
        while pyautogui.locateOnScreen(".\\res\\func\\load_importando_imagens.png") is not None:
            time.sleep(10) 

def salvar_arquivos(caminho_exportar):
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

    #abrir_programa(caminho_programa)
    #while (not verifica_tela_inicial()):
    #    time.sleep(5)

    time.sleep(5)
    for folder in os.listdir(pasta_entrada):
        id_aluno = folder.replace(' ', '_')
        
        criar_novo_projeto(id_aluno, pasta_saida)
        time.sleep(2)
        importar_imagens(f"{pasta_entrada}\\{folder}")
        break
        # salvar_arquivos(caminho_exportar)