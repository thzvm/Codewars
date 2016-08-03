def protein(rna):
    '''RNA to Protein Sequence Translation'''

    amino_acid_dictionary = {# Phenylalanine
                             'UUC':'F', 'UUU':'F',
                             # Leucine
                             'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
                             # Isoleucine
                             'AUU':'I', 'AUC':'I', 'AUA':'I',
                             # Methionine
                             'AUG':'M',
                             # Valine
                             'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
                             # Serine
                             'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
                             # Proline
                             'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
                             # Threonine
                             'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
                             # Alanine
                             'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
                             # Tyrosine
                             'UAU':'Y', 'UAC':'Y',
                             # Histidine
                             'CAU':'H', 'CAC':'H',
                             # Glutamine
                             'CAA':'Q', 'CAG':'Q',
                             # Asparagine
                             'AAU':'N', 'AAC':'N',
                             # Lysine
                             'AAA':'K', 'AAG':'K',
                             # Aspartic Acid
                             'GAU':'D', 'GAC':'D',
                             # Glutamic Acid
                             'GAA':'E', 'GAG':'E',
                             # Cystine
                             'UGU':'C', 'UGC':'C',
                             # Tryptophan
                             'UGG':'W',
                             # Arginine
                             'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
                             # Glycine
                             'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
                             # Stop codon
                             'UAA':'Stop', 'UGA':'Stop', 'UAG':'Stop'
                             }

    if rna:

        split_rna = []
        temp_rna = ''
        for i in range(len(rna)):

            if (i + 1) % 3 == 0 and i != 0:
                temp_rna += rna[i]
                # Stop codon
                if amino_acid_dictionary[temp_rna] != 'Stop':
                    split_rna.append(temp_rna)
                    temp_rna = ''
                else:
                    break
            else:
                temp_rna += rna[i]

        response = ''
        for elem in split_rna:
            response += amino_acid_dictionary[elem]

        return response

if __name__ == '__main__':
    print(protein('AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA'))
