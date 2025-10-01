#!/usr/bin/env python3
"""
A feature-rich calculator implementation using Tkinter.

This module provides a robust calculator with a graphical user interface built using Tkinter.
It follows best practices for code organization, error handling, and accessibility.

Features:
- Basic arithmetic operations (+, -, *, /)
- Clear entry and all clear functionality
- Error handling for division by zero and invalid inputs
- Keyboard support for improved accessibility
- Clean and modern interface

Usage example:
    $ python tkinter_calculator.py
    # Use mouse or keyboard to perform calculations
    # Keyboard shortcuts:
    # - Numbers: 0-9
    # - Operators: +, -, *, /
    # - Enter: Calculate result
    # - Escape: Clear all
    # - Backspace: Clear entry

Author: Siddhesh Suryawanshi
Date: October 1, 2025
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
import re
from typing import Callable, Dict, Optional
from decimal import Decimal, InvalidOperation


class CalculatorApp:
    """Main calculator application class implementing the GUI and logic."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize calculator with GUI elements and event bindings.

        Args:
            root: The main Tkinter window instance
        """
        self.root = root
        self.root.title("Modern Calculator")
        self.root.resizable(False, False)

        # Configure style
        self.style = ttk.Style()
        self.style.configure("Calculator.TButton", padding=10)
        self.style.configure("Display.TEntry", font=("Helvetica", 14))

        # Initialize variables
        self.current_number: str = ""
        self.stored_number: Optional[Decimal] = None
        self.current_operator: Optional[str] = None
        self.last_button_was_operator: bool = False

        self._setup_gui()
        self._setup_bindings()

    def _setup_gui(self) -> None:
        """Set up the calculator's graphical interface."""
        # Display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            justify="right",
            style="Display.TEntry",
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.display_var.set("0")

        # Button layout
        button_layout = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("AC", 5, 1)
        ]

        for (text, row, col) in button_layout:
            button = ttk.Button(
                self.root,
                text=text,
                style="Calculator.TButton",
                command=lambda t=text: self._handle_button_click(t)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            if text == "=":
                button.grid(columnspan=2)

        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def _setup_bindings(self) -> None:
        """Set up keyboard bindings for improved accessibility."""
        self.root.bind("<Key>", self._handle_keypress)
        self.root.bind("<Return>", lambda e: self._handle_button_click("="))
        self.root.bind("<Escape>", lambda e: self._handle_button_click("AC"))
        self.root.bind("<BackSpace>", lambda e: self._handle_button_click("C"))

    def _handle_keypress(self, event: tk.Event) -> None:
        """Handle keyboard input events.

        Args:
            event: Tkinter event object containing key information
        """
        if event.char in "0123456789.+-*/=":
            self._handle_button_click(event.char)

    def _handle_button_click(self, button_text: str) -> None:
        """Process button clicks and update calculator state.

        Args:
            button_text: The text/symbol of the button clicked
        """
        if button_text in "0123456789.":
            self._handle_number_input(button_text)
        elif button_text in "+-*/":
            self._handle_operator(button_text)
        elif button_text == "=":
            self._calculate_result()
        elif button_text == "C":
            self._clear_entry()
        elif button_text == "AC":
            self._clear_all()

    def _handle_number_input(self, digit: str) -> None:
        """Handle numeric input including decimal point.

        Args:
            digit: The number or decimal point to be processed
        """
        if self.last_button_was_operator:
            self.current_number = ""
            self.last_button_was_operator = False

        # Prevent multiple decimal points
        if digit == "." and "." in self.current_number:
            return

        # Handle first decimal point
        if digit == "." and not self.current_number:
            self.current_number = "0"

        self.current_number += digit
        self.display_var.set(self.current_number)

    def _handle_operator(self, operator: str) -> None:
        """Process arithmetic operator input.

        Args:
            operator: The arithmetic operator (+, -, *, /)
        """
        if self.current_number:
            if self.stored_number is not None:
                self._calculate_result()
            try:
                self.stored_number = Decimal(self.current_number)
                self.current_operator = operator
                self.last_button_was_operator = True
            except InvalidOperation:
                self.display_var.set("Error")
                self._clear_all()

    def _calculate_result(self) -> None:
        """Calculate and display the result of the current operation."""
        if not self.stored_number or not self.current_operator:
            return

        try:
            current = Decimal(self.current_number or "0")
            if self.current_operator == "/" and current == 0:
                raise ZeroDivisionError

            operations: Dict[str, Callable[[Decimal, Decimal], Decimal]] = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y
            }

            result = operations[self.current_operator](self.stored_number, current)
            self.display_var.set(str(result))
            self.stored_number = result
            self.current_number = str(result)
            self.current_operator = None

        except ZeroDivisionError:
            self.display_var.set("Cannot divide by zero")
            self._clear_all()
        except (InvalidOperation, ValueError):
            self.display_var.set("Error")
            self._clear_all()

    def _clear_entry(self) -> None:
        """Clear the current entry while preserving stored operations."""
        self.current_number = ""
        self.display_var.set("0")

    def _clear_all(self) -> None:
        """Reset calculator to initial state."""
        self.current_number = ""
        self.stored_number = None
        self.current_operator = None
        self.last_button_was_operator = False
        self.display_var.set("0")


def main() -> None:
    """Create and run the calculator application."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()