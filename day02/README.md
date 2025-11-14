DNA_to_protein program:

Goal - The program should allow the user to input a DNA sequence, click "Translate", and see the resulting amino acid sequence or an error message if the input is invalid.

Claude sonnet 3.5 in VS copilot was used to build the prgraom

Prompt provided to VS copilot to build the progrom:
Build a Python program using Tkinter that translates a DNA sequence into its corresponding amino acid sequence.

Requirements:
1. The program should have a GUI built with Tkinter:
   - An input text box where the user can enter a DNA sequence.
   - A "Translate" button.
   - A label or text area to display the resulting amino acid sequence.
   - An error message box if invalid input is entered.

2. The input DNA sequence must contain only the characters A, T, C, and G (case-insensitive). 
   - If the input contains anything else, show an error and ask the user to enter the sequence again.

3. The program should scan the input sequence for the **start codon (ATG)**. 
   - Translation should start at the first occurrence of ATG.
   - Assign "Methionine (M)" to this codon as the first amino acid.

4. Continue translating codons (every 3 bases) according to the standard genetic code table below:

Codon → Amino Acid  
TTT F, TTC F, TTA L, TTG L,  
CTT L, CTC L, CTA L, CTG L,  
ATT I, ATC I, ATA I, ATG M,  
GTT V, GTC V, GTA V, GTG V,  
TCT S, TCC S, TCA S, TCG S,  
CCT P, CCC P, CCA P, CCG P,  
ACT T, ACC T, ACA T, ACG T,  
GCT A, GCC A, GCA A, GCG A,  
TAT Y, TAC Y, TAA STOP, TAG STOP,  
CAT H, CAC H, CAA Q, CAG Q,  
AAT N, AAC N, AAA K, AAG K,  
GAT D, GAC D, GAA E, GAG E,  
TGT C, TGC C, TGA STOP, TGG W,  
CGT R, CGC R, CGA R, CGG R,  
AGT S, AGC S, AGA R, AGG R,  
GGT G, GGC G, GGA G, GGG G.

5. If a **stop codon** (TAA, TAG, or TGA) is encountered, translation should stop immediately and output the amino acid sequence up to that point.

6. If no start or stop codons are found in the input sequence:
   - Simply start translating from the first codon to the last, ignoring incomplete codons at the end.

7. Output the amino acid sequence using **one-letter amino acid codes** (e.g., M, L, F, R, etc.).

8. Make sure the GUI is simple and user-friendly (labels, spacing, clear layout).
