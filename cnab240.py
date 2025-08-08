import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
import os

def load_stylesheet():
    
    style_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
    try:
        with open(style_path, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo de estilo não encontrado: {style_path}")
        return ""
    except Exception as e:
        print(f"Erro ao carregar estilo: {str(e)}")
        return ""

def main():
    app = QApplication(sys.argv)
    
    # Carrega o estilo antes de criar a janela principal
    stylesheet = load_stylesheet()
    if stylesheet:
        app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()