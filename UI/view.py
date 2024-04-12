import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1 with some controls
        # DropDown dei corsi e bottone per cercare gli iscritti
        self.ddCorso = ft.Dropdown(value="Selezionare un corso",
                                   label="Selezionare un corso",
                                   expand=1)

        self._controller.handleCaricaCorsiDD()

        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handleCercaIscritti)
        row1 = ft.Row([self.ddCorso, self.btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW 2
        # Text field per matricola, nome e cognome
        self.tfMatricola = ft.TextField(value="matricola")
        self.tfNome = ft.TextField(value="nome", read_only=True)
        self.tfCognome = ft.TextField(value="cognome", read_only=True)
        row2 = ft.Row([self.tfMatricola, self.tfNome, self.tfCognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW 3
        # Bottoni per cercare corsi, studenti e iscrivere
        self.btnCercaStudente = ft.ElevatedButton(text="Cerca studente")
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi")
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi")
        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the result is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
