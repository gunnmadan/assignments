def transcription(dna_sequence):
    complement = ''
    complement_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    for base in dna_sequence:
        if base in complement_dict:
            complement += complement_dict[base]
        else:
            complement += base  
    mrna = complement.replace('T', 'U')
    return mrna

     
def translate(mrna):
    codon_to_amino_acid = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
        "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    }
    protein = ''
    codons = [mrna[i:i+3] for i in range(0, len(mrna), 3)]
    for codon in codons: 
        protein += codon_to_amino_acid.get(codon, '')
        protein += ' '
    return protein.strip()


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

mrna = transcription(dna)
protein = translate(mrna)

print("DNA Sequence")
print(dna)

print("\nTranscribed mRNA Sequence")
print(mrna)

print("\nTranslated Protein Sequence")
print(protein)