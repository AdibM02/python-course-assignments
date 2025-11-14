#!/usr/bin/env python3
"""
Improved DNA -> Protein GUI using ttkbootstrap (modern theming) and Biopython
for translation logic.

This module exposes a helper `translate_sequence_from_text(seq_text)` which the
GUI uses. The GUI itself is only created when running the module as __main__.
"""
from typing import Optional
import re

try:
    import ttkbootstrap as tb
    from ttkbootstrap.constants import LEFT, RIGHT
except Exception:
    #!/usr/bin/env python3
    """
    Improved DNA -> Protein GUI using ttkbootstrap (modern theming) and Biopython
    for translation logic.

    This module exposes a helper `translate_sequence_from_text(seq_text)` which the
    GUI uses. The GUI itself is only created when running the module as __main__.
    """
    import re
    from typing import Optional

    try:
        import ttkbootstrap as tb
    except Exception:
        tb = None  # fallback to tkinter if ttkbootstrap is not installed
#!/usr/bin/env python3
"""DNA -> Protein translator GUI and helper.

This module provides:
- translate_sequence_from_text(sequence: str) -> str
- DNATranslatorGUI: small Tkinter/ttkbootstrap GUI wrapper

The GUI is only constructed when the module is run as __main__.
"""

from typing import Optional
import re

# Optional UI/theme library (nice but not required)
try:
    import ttkbootstrap as tb
except Exception:
    tb = None

# Optional Biopython for robust translation
try:
    from Bio.Seq import Seq
except Exception:
    Seq = None

GENETIC_CODE_REGEX = re.compile(r'^[ATCGatcg]+$')


def validate_sequence(sequence: str) -> bool:
    """Return True if sequence contains only A,T,C,G (case-insensitive)."""
    if not sequence:
        return False
    return bool(GENETIC_CODE_REGEX.fullmatch(sequence.strip()))


def translate_sequence_from_text(sequence: str) -> str:
    """Translate DNA sequence according to requirements.

    Rules:
    - Only A/T/C/G characters allowed (caller should validate first).
    - Find first ATG; if present start from it, otherwise start from beginning.
    - Translate in-frame codons (3 bases).
    - Stop at the first stop codon (TAA, TAG, TGA).
    - Use one-letter amino acid codes; incomplete trailing codons are ignored.
    """
    if not sequence:
        return ""

    dna = sequence.upper().strip()
    start = dna.find('ATG')
    if start == -1:
        start = 0

    coding = dna[start:]

    # Prefer Biopython if available (handles translation reliably)
    if Seq is not None:
        try:
            return str(Seq(coding).translate(to_stop=True))
        except Exception:
            # Fall through to local translator on any unexpected error
            pass

    # Local fallback genetic code
    genetic_code = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    protein = []
    i = 0
    while i + 2 < len(coding):
        codon = coding[i:i+3]
        aa = genetic_code.get(codon, '')
        if aa == '*':
            break
        if aa:
            protein.append(aa)
        i += 3

    return ''.join(protein)


class DNATranslatorGUI:
    """Small GUI wrapper using ttkbootstrap when available."""

    def __init__(self):
        if tb is not None:
            self.root = tb.Window(title='DNA to Protein Translator')
        else:
            import tkinter as tk
            self.root = tk.Tk()

        self.root.geometry('650x420')
        self._build()

    def _build(self):
        if tb is not None:
            Frame = tb.Frame
            Label = tb.Label
            Button = tb.Button
            Text = tb.Text
            Scrollbar = tb.Scrollbar
        else:
            import tkinter as tk
            Frame = tk.Frame
            Label = tk.Label
            Button = tk.Button
            Text = tk.Text
            Scrollbar = tk.Scrollbar

        title = Label(self.root, text='DNA to Protein Translator', font=('Helvetica', 16, 'bold'))
        title.pack(pady=14)

        instr = Label(self.root, text='Enter DNA sequence (A, T, C, G only):')
        instr.pack(pady=6)

        input_frame = Frame(self.root)
        input_frame.pack(padx=20, pady=8, fill='x')

        self.input_text = Text(input_frame, height=6, wrap='word')
        self.input_text.pack(side='left', fill='x', expand=True)

        sb = Scrollbar(input_frame, command=self.input_text.yview)
        sb.pack(side='right', fill='y')
        self.input_text.config(yscrollcommand=sb.set)

        btn = Button(self.root, text='Translate', command=self.on_translate)
        btn.pack(pady=12)

        out_label = Label(self.root, text='Amino Acid Sequence:')
        out_label.pack(pady=6)

        out_frame = Frame(self.root)
        out_frame.pack(padx=20, pady=6, fill='both', expand=True)

        self.output_text = Text(out_frame, height=8, wrap='word')
        self.output_text.pack(side='left', fill='both', expand=True)
        out_sb = Scrollbar(out_frame, command=self.output_text.yview)
        out_sb.pack(side='right', fill='y')
        self.output_text.config(yscrollcommand=out_sb.set)
        self.output_text.config(state='disabled')

    def on_translate(self):
        import tkinter.messagebox as messagebox

        seq = self.input_text.get('1.0', 'end').strip()
        if not seq:
            messagebox.showerror('Error', 'Please enter a DNA sequence.')
            return
        if not validate_sequence(seq):
            messagebox.showerror('Error', 'Invalid DNA sequence! Use only A, T, C and G.')
            return

        protein = translate_sequence_from_text(seq)
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', 'end')
        self.output_text.insert('1.0', protein)
        self.output_text.config(state='disabled')

    def run(self):
        self.root.mainloop()


def main():
    app = DNATranslatorGUI()
    app.run()


if __name__ == '__main__':
    main()