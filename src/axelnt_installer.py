#!/usr/bin/env python3
import sys
import pytermgui as ptg

def main(argv: list[str] | None = None) -> None:
    """Runs the application."""

    with ptg.WindowManager() as manager:
        manager.layout = _define_layout()

        header = ptg.Window(
            "[app.header] Welcome to PyTermGUI ",
            box="EMPTY",
        )

        # Since header is the first defined slot, this will assign to the correct place
        manager.add(header)

        footer = ptg.Window(ptg.Button("Quit", lambda *_: manager.stop()), box="EMPTY")

        # Since the second slot, body was not assigned to, we need to manually assign
        # to "footer"
        manager.add(footer, assign="footer")

        manager.add(ptg.Window("My sidebar"), assign="body_right")
        manager.add(ptg.Window("My body window"), assign="body")

    ptg.tim.print("[!gradient(210)]Goodbye!")

def start_installer():
    main()

if __name__ == "__main__":
    start_installer()