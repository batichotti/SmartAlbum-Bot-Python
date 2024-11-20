import pyautogui
from time import sleep
import os

TEMPO_ESPERA = 1

def esperar_elemento(image_path, timeout=10):
    """
    Aguarda um elemento aparecer na tela dentro de um tempo limite.
    
    Args:
        image_path (str): Caminho para a imagem do elemento a localizar.
        timeout (int): Tempo máximo em segundos para aguardar o elemento.

    Returns:
        tuple: Coordenadas do centro do elemento se encontrado.
        None: Caso o elemento não seja encontrado dentro do tempo limite.
    """
    for _ in range(timeout):
        elemento = pyautogui.locateCenterOnScreen(image_path)
        if elemento:
            return elemento
        sleep(1)
    return None

def abrir_programa(caminho_programa):
    """
    Abre um programa especificado usando o comando "Executar" do Windows.
    
    Args:
        caminho_programa (str): Caminho ou comando para abrir o programa.

    Returns:
        bool: True se o programa foi aberto com sucesso, False em caso de erro.
    """
    try:
        pyautogui.hotkey("win", "r")
        sleep(TEMPO_ESPERA)
        pyautogui.write(caminho_programa)
        pyautogui.press("enter")
        sleep(10)
        return True
    except:
        return False

def clicar_botao(image_path, timeout=10):
    """
    Localiza e clica em um botão identificado por uma imagem.
    
    Args:
        image_path (str): Caminho para a imagem do botão.
        timeout (int): Tempo máximo em segundos para localizar o botão.

    Returns:
        bool: True se o botão foi clicado com sucesso, False em caso de falha.
    """
    botao = esperar_elemento(image_path, timeout)
    if botao:
        pyautogui.click(botao)
        return True
    return False

def criar_novo_projeto(id_projeto):
    """
    Cria um novo projeto em um programa com base no ID fornecido.
    
    Args:
        id_projeto (str): Identificador único do projeto.

    Returns:
        bool: True se o projeto foi criado com sucesso, False em caso de erro.
    """
    try:
        if not clicar_botao('./res/func/bt_novo_projeto.png'):
            return False

        clicar_botao('./res/func/bt_album.png')
        if not clicar_botao('./res/func/bt_personalizado.png') and \
           not clicar_botao('./res/func/bt_personalizado2.png'):
            pass

        if not clicar_botao('./res/func/bt_new_preset.png'):
            pyautogui.write(id_projeto)
            pyautogui.press("enter")
        return True
    except:
        return False

def importar_imagens(pasta_imagens):
    """
    Importa imagens de uma pasta específica para o projeto.
    
    Args:
        pasta_imagens (str): Caminho da pasta contendo as imagens a serem importadas.

    Returns:
        bool: True se as imagens foram importadas com sucesso, False em caso de erro.
    """
    try:
        if not clicar_botao('./res/func/bt_importar_imagens.png'):
            return False

        pyautogui.hotkey("ctrl", "l")
        pyautogui.write(pasta_imagens)
        pyautogui.press("enter")
        sleep(TEMPO_ESPERA)

        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")

        while esperar_elemento('./res/func/load_importando_imagens.png'):
            sleep(5)
        return True
    except:
        return False

def salvar_projeto(caminho_exportar):
    """
    Salva e exporta o projeto para um caminho especificado.
    
    Args:
        caminho_exportar (str): Caminho para salvar o projeto exportado.

    Returns:
        bool: True se o projeto foi salvo e exportado com sucesso, False em caso de erro.
    """
    try:
        if not clicar_botao('./res/func/botao_exportar.png'):
            return False

        pyautogui.write(caminho_exportar)
        pyautogui.press("enter")
        sleep(TEMPO_ESPERA)

        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('alt', 'f4')
        return True
    except:
        return False

def processar_projetos(caminho_programa, pasta_entrada, pasta_saida):
    """
    Processa múltiplos projetos de uma pasta de entrada e exporta os resultados
    para uma pasta de saída.

    Args:
        caminho_programa (str): Caminho ou comando para abrir o programa.
        pasta_entrada (str): Caminho da pasta contendo as subpastas de projetos.
        pasta_saida (str): Caminho da pasta onde os projetos serão exportados.

    Returns:
        None
    # """
    
    # while not abrir_programa(caminho_programa):
    #     sleep(TEMPO_ESPERA)

    for pasta in os.listdir(pasta_entrada):
        caminho_pasta = os.path.join(pasta_entrada, pasta)
        id_projeto = pasta.replace(' ', '_')

        while not criar_novo_projeto(id_projeto):
            sleep(TEMPO_ESPERA)

        while not importar_imagens(caminho_pasta):
            sleep(TEMPO_ESPERA)

        while not salvar_projeto(os.path.join(pasta_saida, id_projeto)):
            sleep(TEMPO_ESPERA)
