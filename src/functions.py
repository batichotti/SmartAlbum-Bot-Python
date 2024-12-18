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
        botao_criar_projeto = get_botao('./images/bt_novo_projeto.png')
        if botao_criar_projeto:
            pyautogui.click(botao_criar_projeto)
            sleep(1)

        botao_album = get_botao('./images/bt_album.png')
        if botao_album:
            pyautogui.click(botao_album)
            sleep(1)
        
        pyautogui.click(x=1360, y=300) # Botão Personalizado

        sleep(1)
        
        pyautogui.click(x=1106, y=403) # Botão Novo Preset
        pyautogui.click(x=1138, y=439) # Botão 23x60

        pyautogui.click(x=1661, y=954) # Proximo
        sleep(1)
        
        pyautogui.click(x=1670, y=820) # Iniciar
        sleep(3/2)
        
        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(f"{saida}")
        pyautogui.press("right")
        pyautogui.press("enter")
        sleep(1)
        
        for i in range(7):
            pyautogui.press("tab")  # Tabulating to find the writeble field
        pyautogui.write(f"{id}")
        pyautogui.press("enter")
        exception_overwrite()  #  demora + ou - 5 segundos
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
        sleep(60*minutes+15)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
        return True
    except:
        return False

def processar_projetos(pasta_entrada, pasta_saida, minutes, abrir):
    caminho_programa = "C:\\Program Files\\Pixellu SmartAlbums\\SmartAlbum.exe"
    abrir = False
    if abrir:
        abrir_programa(caminho_programa)
    for folder in os.listdir(pasta_entrada):
        
        if os.path.isdir(os.path.join(pasta_entrada, folder)):
            id_aluno = folder.replace(' ', '_')

            criar_novo_projeto(id_aluno, pasta_saida)

            importar_imagens(pasta_entrada, folder)

            salvar_arquivos(minutes)

    pyautogui.alert('Processamento finalizado com sucesso!', 'Sucesso!', button='OK')


if __name__ == "__main__":
    processar_projetos("\\\\impressora\\6 Tera\\Arquivos compartilhados\\PRE EVENTOS 2024\\TEC ENFERMAGEM IRETAMA\\PRONTAS PARA SEPARAR\\SEPARADAS", "C:\\Users\\Pablo\\Desktop\\test bot prontas", 1, False)