from PySimpleGUI import (
    Output,
    Window,
    WINDOW_CLOSED,
    Multiline,
    Frame,
    Button,
)
import PySimpleGUI as sg
from dataclasses import dataclass
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor


class ErrorList(ErrorListener):
    errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error: {msg} at line {line} column {column}.")


mocha_theme = {
    "BACKGROUND": "#11111b",
    "TEXT": "#cdd6f4",
    "INPUT": "#1e1e2e",
    "TEXT_INPUT": "#cdd6f4",
    "SCROLL": "##cba6f7",
    "BUTTON": ("#11111b", "#b4befe"),
    "PROGRESS": ("#11111b", "#b4befe"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}

sg.theme_add_new("mocha", mocha_theme)
sg.theme("mocha")

__all__ = ["MainWindow"]


@dataclass
class MainWindow:
    WIDHT = 900
    HEIGHT = 450

    left_input_layout = [
        [
            Multiline(
                size=(WIDHT, 22), key="-INPUT-", auto_refresh=True, auto_size_text=True
            ),
        ],
        [
            Frame(
                "",
                layout=[
                    [
                        Button(
                            button_text="Compilar",
                            key="-COMPILE-",
                            auto_size_button=True,
                        ),
                        Button(
                            button_text="Verificar",
                            key="-VERIFY-",
                            auto_size_button=True,
                        ),
                    ]
                ],
                element_justification="center",
            )
        ],
        [Multiline(size=(WIDHT, 22), key="-OUTPUT-", auto_refresh=True)],
    ]

    window = Window(
        title="Tela Principal",
        layout=[
            [
                left_input_layout,
            ]
        ],
        size=(WIDHT, HEIGHT),
        auto_size_buttons=True,
        resizable=True,
        text_justification="center",
        element_justification="center",
    )

    def run(self):
        while True:
            if self.window.was_closed():
                break
            event, values = self.window.read()
            print(event, values)
            if event in ("Exit", WINDOW_CLOSED):
                self.window.close()
            if event == "-COMPILE-":
                lexer = SimplifiedJavaLexer(InputStream(values["-INPUT-"]))
                error_lins = ErrorList()
                lexer.removeErrorListeners()
                lexer.addErrorListener(error_lins)

                stream = CommonTokenStream(lexer)
                parser = SimplifiedJavaParser(stream)

                parser.removeErrorListeners()
                parser.addErrorListener(error_lins)

                walker = ParseTreeWalker()

                tree = parser.prog()

                visitor = SimplifiedJavaVisitor()
                visitor.visit(tree)

                self.window["-OUTPUT-"].update("\n".join(error_lins.errors))


if __name__ == "__main__":
    MainWindow().run()
