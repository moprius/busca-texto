import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QScrollArea, QMessageBox
from PySide6.QtGui import QAction, QFont, QPixmap
from PySide6.QtCore import Qt
from search_data import search_categories

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

                # Configuração da interface e tamanho
        self.setWindowTitle("Marxism Lib - busca de textos socialistas")
        self.setMinimumSize(500, 500)
        layout = QVBoxLayout()

        # Barra de menu
        menu_bar = self.menuBar()

        # Menu de Arquivo
        file_menu = menu_bar.addMenu("&Arquivo")
        new_action = QAction("&Novo", self)
        new_action.triggered.connect(self.clear_search)
        file_menu.addAction(new_action)
        exit_action = QAction("&Sair", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Menu de Ajuda
        help_menu = menu_bar.addMenu("&Ajuda")
        about_action = QAction("&Sobre", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        license_action = QAction("&Licença", self)
        license_action.triggered.connect(self.show_license)
        help_menu.addAction(license_action)

        # Texto informativo
        info_label = QLabel("Busque trechos de livros")
        info_label.setAlignment(Qt.AlignCenter)  # Centralizar o texto

        # Configurando a fonte para ser negrito e maior
        font = info_label.font()  # Pega a fonte atual
        font.setBold(True)  # Define a fonte como negrito
        font.setPointSize(font.pointSize() * 2)  # Aumenta o tamanho da fonte
        info_label.setFont(font)

        layout.addWidget(info_label)

        # Imagem
        image_label = QLabel()
        pixmap = QPixmap('imagem.png').scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        # Configuração dos Widgets
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Digite sua busca...")
        self.search_bar.returnPressed.connect(self.on_search)
        layout.addWidget(self.search_bar)

        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.on_search)
        layout.addWidget(self.search_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Área de rolagem do texto
        self.result_label = QLabel()
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignLeft)
        self.result_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.result_label)
        layout.addWidget(scroll_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def on_search(self):
        search_query = self.search_bar.text()
        results = []

        for category in search_categories:
            category_results = category.search(search_query)
            if category_results:
                # Formatar apenas o nome da categoria em negrito
                formatted_category = f"<b>{category.name.capitalize()}</b>"
                formatted_results = "<br>".join(f"{formatted_category} - {result}" for result in category_results)
                results.append(formatted_results)

        if results:
            self.result_label.setText('\n\n'.join(results))
        else:
            self.result_label.setText("Resultado não encontrado.")

    def clear_search(self):
        # Limpa a busca
        self.search_bar.clear()
        self.result_label.clear()

    def show_about(self):
        QMessageBox.information(self, "Sobre", "Programa baseado que busca texto de livros, versão 0.1")

    def show_license(self):
        QMessageBox.information(self, "Licença", "A licença para este software é GPLv3 consulte https://www.gnu.org/licenses/")



# Execução do aplicativo
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
