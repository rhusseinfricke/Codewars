#Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).


def DNA_strand(dna):
    dna = dna.upper()
    comp_dna =[]
    for base in list(dna.upper()):
        if base == "A":
            comp_dna.append("T")
        if base == "T":
            comp_dna.append("A")
        if base == "G":
            comp_dna.append("C")
        if base == "C":
            comp_dna.append("G")
    return ''.join(comp_dna)
 