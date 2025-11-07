import tkinter as tk
from tkinter import messagebox

class DNATranslator:
    def __init__(self):
        # Genetic code dictionary using one-letter codes
        self.genetic_code = {
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
        
        self.create_gui()

    def create_gui(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("DNA to Protein Translator")
        self.window.geometry("600x400")
        
        # Create and pack widgets with padding
        title_label = tk.Label(self.window, 
                             text="DNA to Protein Translator",
                             font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        instruction_label = tk.Label(self.window,
                                   text="Enter DNA sequence (A, T, C, G only):",
                                   font=("Arial", 10))
        instruction_label.pack(pady=5)

        # Create text input with scrollbar
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.scrollbar = tk.Scrollbar(self.input_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.dna_input = tk.Text(self.input_frame, height=4, 
                                wrap=tk.WORD, 
                                yscrollcommand=self.scrollbar.set)
        self.dna_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.scrollbar.config(command=self.dna_input.yview)

        # Translate button
        self.translate_button = tk.Button(self.window,
                                        text="Translate",
                                        command=self.translate_sequence,
                                        font=("Arial", 10, "bold"))
        self.translate_button.pack(pady=10)

        # Result label
        result_label = tk.Label(self.window,
                              text="Amino Acid Sequence:",
                              font=("Arial", 10))
        result_label.pack(pady=5)

        # Result text area with scrollbar
        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.result_scrollbar = tk.Scrollbar(self.result_frame)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_text = tk.Text(self.result_frame, height=6,
                                 wrap=tk.WORD,
                                 yscrollcommand=self.result_scrollbar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.result_scrollbar.config(command=self.result_text.yview)
        
        # Make result text read-only
        self.result_text.config(state=tk.DISABLED)

    def validate_sequence(self, sequence):
        """Validate that sequence contains only valid DNA bases"""
        valid_bases = set('ATCG')
        sequence_bases = set(sequence.upper())
        return sequence_bases.issubset(valid_bases)

    def translate_dna_to_protein(self, dna_sequence):
        """Translate DNA sequence to protein sequence"""
        # Convert to uppercase for consistency
        dna = dna_sequence.upper()
        
        # Find start codon
        start_pos = dna.find('ATG')
        if start_pos == -1:
            # If no start codon found, start from beginning
            start_pos = 0
        
        # Initialize protein sequence
        protein = []
        
        # Translate codons
        i = start_pos
        while i + 2 < len(dna):
            codon = dna[i:i+3]
            if len(codon) == 3:  # Only process complete codons
                amino_acid = self.genetic_code.get(codon, '')
                if amino_acid == '*':  # Stop codon found
                    break
                if amino_acid:  # Valid codon found
                    protein.append(amino_acid)
            i += 3
            
        return ''.join(protein)

    def translate_sequence(self):
        """Handle the translation process and GUI updates"""
        # Get input sequence
        sequence = self.dna_input.get("1.0", tk.END).strip()
        
        if not sequence:
            messagebox.showerror("Error", "Please enter a DNA sequence.")
            return
            
        # Validate sequence
        if not self.validate_sequence(sequence):
            messagebox.showerror("Error", 
                               "Invalid DNA sequence! Please use only A, T, C, and G.")
            return
            
        # Translate sequence
        protein = self.translate_dna_to_protein(sequence)
        
        # Update result text
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", protein)
        self.result_text.config(state=tk.DISABLED)

    def run(self):
        """Start the application"""
        self.window.mainloop()

if __name__ == "__main__":
    app = DNATranslator()
    app.run()