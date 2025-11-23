"""GUI for DNA to Protein Translator.

Provides a Tkinter interface for translating DNA sequences to protein sequences.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from logic import validate_sequence, translate_dna_to_protein


class DNATranslatorGUI:
    """Tkinter GUI for DNA to Protein translation."""

    def __init__(self, root: tk.Tk):
        """Initialize the GUI.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title('DNA to Protein Translator')
        self.root.geometry('650x420')
        self.root.resizable(True, True)

        self._build_ui()

    def _build_ui(self):
        """Build the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding='10')
        main_frame.grid(row=0, column=0, sticky='nsew')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame,
            text='DNA to Protein Translator',
            font=('Helvetica', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Input label
        ttk.Label(main_frame, text='DNA Sequence (A, T, C, G):').grid(
            row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0)
        )

        # Input frame with scrollbar
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(0, weight=1)

        input_scrollbar = ttk.Scrollbar(input_frame)
        input_scrollbar.grid(row=0, column=1, sticky='ns')

        self.input_text = tk.Text(
            input_frame,
            height=6,
            width=40,
            wrap='word',
            yscrollcommand=input_scrollbar.set
        )
        self.input_text.grid(row=0, column=0, sticky='nsew')
        input_scrollbar.config(command=self.input_text.yview)
        self.input_text.bind('<Return>', lambda e: self._on_translate())

        # Translate button
        translate_btn = ttk.Button(
            main_frame,
            text='Translate',
            command=self._on_translate
        )
        translate_btn.grid(row=3, column=0, columnspan=2, pady=15, sticky='ew')

        # Output label
        ttk.Label(main_frame, text='Amino Acid Sequence:').grid(
            row=4, column=0, sticky='w', padx=(0, 10), pady=(10, 0)
        )

        # Output frame with scrollbar
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=(0, 10))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

        output_scrollbar = ttk.Scrollbar(output_frame)
        output_scrollbar.grid(row=0, column=1, sticky='ns')

        self.output_text = tk.Text(
            output_frame,
            height=8,
            width=40,
            wrap='word',
            state='disabled',
            yscrollcommand=output_scrollbar.set
        )
        self.output_text.grid(row=0, column=0, sticky='nsew')
        output_scrollbar.config(command=self.output_text.yview)

        # Configure row weights for proper resizing
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(5, weight=2)

    def _on_translate(self):
        """Handle translate button click."""
        seq = self.input_text.get('1.0', 'end').strip()

        if not seq:
            messagebox.showerror('Input Error', 'Please enter a DNA sequence.')
            return

        if not validate_sequence(seq):
            messagebox.showerror(
                'Invalid Sequence',
                'Invalid DNA sequence! Use only A, T, C, and G.'
            )
            return

        # Translate
        protein = translate_dna_to_protein(seq)

        # Display result
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', 'end')
        self.output_text.insert('1.0', protein)
        self.output_text.config(state='disabled')

    def run(self):
        """Start the GUI event loop."""
        self.root.mainloop()


def main():
    """Launch the application."""
    root = tk.Tk()
    app = DNATranslatorGUI(root)
    app.run()


if __name__ == '__main__':
    main()
