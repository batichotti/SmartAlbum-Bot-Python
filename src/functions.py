fx: {
from tkinter import messagebox
from time import sleep
import pyautogui
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

def exception_overwrite():
    sleep(1)
    for i in range(2):
        botao_substituir = get_botao(".\\res\\func\\deseja_substituilo.png")
        if botao_substituir:
            pyautogui.press("left")
            pyautogui.press("enter")
            sleep(2)

def criar_novo_projeto(id, saida):
    try:
        sleep(5)
        botao_criar_projeto = get_botao('./res/func/bt_novo_projeto.png')
        if botao_criar_projeto:
            pyautogui.click(botao_criar_projeto)
            sleep(1)

        botao_album = get_botao('./res/func/bt_album.png')
        if botao_album:
            pyautogui.click(botao_album)
            sleep(1)

        botao_personalizado = get_botao('./res/func/bt_personalizado3.png')
        while not botao_personalizado:
            sleep(1)
            botao_personalizado = get_botao('./res/func/bt_personalizado.png')
            if not botao_personalizado:
                botao_personalizado = get_botao('./res/func/bt_personalizado2.png')
            if not botao_personalizado:
                botao_personalizado = get_botao('./res/func/bt_personalizado3.png')
            
        if botao_personalizado:
            pyautogui.click(botao_personalizado)
            sleep(1)

        
        sleep(2)
        botao_always_exist = get_botao('./res/func/23x60_always_there_2.png')
        botao_new_preset = get_botao('./res/func/bt_new_preset.png')
        while (not botao_always_exist) and (not botao_new_preset):
            
            botao_always_exist = get_botao('./res/func/23x60_always_there_2.png')
            if not botao_always_exist:
                botao_always_exist = get_botao('./res/func/23x60_always_there_3.png')
            if not botao_always_exist:
                botao_always_exist = get_botao('./res/func/23x60_always_there.png')
                
            botao_new_preset = get_botao('./res/func/bt_new_preset.png')
            
        if botao_always_exist:
            pyautogui.press("enter")
            sleep(1)
            pyautogui.press("enter")
            sleep(1)
            pyautogui.hotkey("ctrl", "l")
            pyautogui.write(f"{saida}")
            pyautogui.press("right")
            pyautogui.press("enter")
            for i in range(7):
                pyautogui.press("tab")
            pyautogui.write(f"{id}")
            pyautogui.press("enter")
            exception_overwrite()
        else:
            if botao_new_preset:
                pyautogui.click(botao_new_preset)
                sleep(1)
                botao_23x60 = get_botao('./res/func/23x60.png')
                
                while not botao_23x60:
                    sleep(1)
                    botao_23x60 = get_botao('./res/func/23x60.png')
            
                if botao_23x60:
                    pyautogui.click(botao_23x60)
                    sleep(1)
            

        botao_proximo = get_botao('./res/func/bt_proximo.png')
        if botao_proximo:
            pyautogui.click(botao_proximo)
            sleep(1)
            
        return True
    except:
        return False

def importar_imagens(images_folder):
    
    if get_botao(".\\res\\func\\smartalbum_aberto_padrao.png"):
        sleep(1)
        pyautogui.click(x=300,  y=300)
        pyautogui.hotkey("ctrl", "i")
        sleep(1)
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(images_folder)
        pyautogui.press("right")
        pyautogui.press("enter")
        sleep(1)
        
        for i in range(4):
            pyautogui.press("tab")
        
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")
        sleep(1)
        
        exception_overwrite()
        return True
    else:
        return False


def salvar_arquivos():
    try:
        while not get_botao(".\\res\\func\\was_imported.png"):
            sleep(1)
        sleep(1)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
        return True
    except:
        return False

def processar_projetos(pasta_entrada, pasta_saida):
    caminho_programa = "C:\\Program Files\\Pixellu SmartAlbums\\SmartAlbum.exe"
    # abrir_programa(caminho_programa)
    for folder in os.listdir(pasta_entrada):
        if os.path.isdir(os.path.join(pasta_entrada, folder)):
            id_aluno = folder.replace(' ', '_')

            while not criar_novo_projeto(id_aluno, pasta_saida):
                sleep(1)

            while not importar_imagens(os.path.join(pasta_entrada, folder)):
                sleep(1)

            while not salvar_arquivos():
                sleep(1)
    messagebox.showinfo(f"Processamento do Album encontrado em {pasta_entrada} finalizado com sucesso.")


if __name__ == "__main__":
    processar_projetos("", "C:\\Users\\Pablo\\Desktop\\test bot separadas", "C:\\Users\\Pablo\\Desktop\\test bot prontas")
}

gui  {

}