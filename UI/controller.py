import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handleCaricaCorsiDD(self):
        for corso in self._model.get_corsi().values():
            self._view.ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def handleCercaIscritti(self, e):
        selezione = self._view.ddCorso.value
        result = self._model.cercaIscritti(selezione)
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(result)} iscritti al corso:"))
        for element in result:
            self._view.txt_result.controls.append(ft.Text(element))
        self._view.update_page()
