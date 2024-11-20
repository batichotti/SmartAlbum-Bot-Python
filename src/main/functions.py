import pyautogui
import time
import os

def abrir_programa(caminho_programa):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write(caminho_programa)
    pyautogui.press("enter")
    time.sleep(10)

def get_botao(image_path: str):
    """Localiza a posição central de um botão na tela baseado em uma imagem.

    Args:
        image_path (str): Caminho da imagem do botão a ser localizado.

    Returns:
        (x, y): A posição central (x, y) do botão se encontrado.
        None: Se a imagem do botão não for encontrada.
    """
    try:
        return pyautogui.locateCenterOnScreen(image_path)
    except:
        return None


def criar_novo_projeto(id, output_folder):
    botao_criar_projeto = get_botao('.\\res\\func\\bt_novo_projeto.png')
    if botao_criar_projeto:
        pyautogui.click(botao_criar_projeto)
        time.sleep(1)
    else:
        print("Botão de criar novo projeto não encontrado.")
        return

    botao_album = get_botao(".\\res\\func\\bt_album.png")
    if botao_album:
        pyautogui.click(botao_album)
        time.sleep(2)

    botao_personalizado = get_botao(".\\res\\func\\bt_personalizado.png") or get_botao(".\\res\\func\\bt_personalizado2.png")
    if botao_personalizado:
        pyautogui.click(botao_personalizado)
        time.sleep(1)
    else:
        print("Botão personalizado não encontrado.")
        return

    botao_new_preset = get_botao(".\\res\\func\\bt_new_preset.png")
    if botao_new_preset:
        pyautogui.click(botao_new_preset)
        time.sleep(1)
        botao_23x60 = get_botao(".\\res\\func\\23x60.png")
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

def importar_imagens(images_folder):
    botao_import = get_botao(".\\res\\func\\bt_importar_imagens.png")
    if botao_import:
        pyautogui.click(botao_import)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(images_folder)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")
        
        while get_botao(".\\res\\func\\load_importando_imagens.png") is not None:
            time.sleep(10)
    else:
        print("Botão de importar imagens não encontrado.")

def salvar_arquivos(caminho_exportar):
    botao_exportar = get_botao('.\\res\\func\\botao_exportar.png')
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

    for folder in os.listdir(pasta_entrada):
        id_aluno = folder.replace(' ', '_')
        
        criar_novo_projeto(id_aluno, pasta_saida)
        time.sleep(2)
        importar_imagens(f"{pasta_entrada}\\{folder}")
        
        salvar_arquivos(pasta_saida)
        break
