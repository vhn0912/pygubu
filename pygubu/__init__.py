# encoding: utf-8

__all__ = [
    "Builder",
    "TkApplication",
    "BuilderObject",
    "register_widget",
    "register_property",
    "register_custom_property",
    "remove_binding",
    "ApplicationLevelBindManager",
]

import warnings

from pygubu.binding import ApplicationLevelBindManager, remove_binding
from pygubu.builder import Builder
from pygubu.builder.builderobject import (
    BuilderObject,
    register_custom_property,
    register_property,
    register_widget,
)

__version__ = "0.23.1"


class TkApplication:
    def __init__(self, master=None):
        warnings.warn(
            "TkApplication is deprecated and it will be removed in the future. Use a Toplevel instance in the ui file.",
            category=DeprecationWarning,
        )
        self.master = master
        self.toplevel = master.winfo_toplevel()

        self.toplevel.withdraw()
        self._init_before()
        self._create_ui()
        self._init_after()
        self.toplevel.deiconify()

    def _init_before(self):
        pass

    def _create_ui(self):
        pass

    def _init_after(self):
        pass

    def run(self):
        """Ejecute the main loop."""

        self.toplevel.protocol("WM_DELETE_WINDOW", self.__on_window_close)
        self.toplevel.mainloop()

    def set_resizable(self):
        self.toplevel.rowconfigure(0, weight=1)
        self.toplevel.columnconfigure(0, weight=1)

    def set_title(self, title):
        """Set the window title."""
        self.toplevel.title(title)

    def set_menu(self, menu):
        """Set the main menu."""
        self.toplevel.config(menu=menu)

    def __on_window_close(self):
        """Manage WM_DELETE_WINDOW protocol."""
        if self.on_close_execute():
            self.toplevel.destroy()

    def on_close_execute(self):
        """Determine if if the application is ready for quit,
        return boolean."""
        return True

    def quit(self):
        """Exit the app if it is ready for quit."""
        self.__on_window_close()

    def set_size(self, geom):
        self.toplevel.geometry(geom)
