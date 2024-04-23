# • Implementar un algoritmo que indique si es una cadena de ADN, ARN o proteínas.
import random

DNA_components = {"A", "C", "G", "T"}
RNA_components = {"A", "C", "G", "U", "E"}


def generate_random_sequence(length, sequence_type):
    if sequence_type == "DNA":
        bases = "ACGT"
    elif sequence_type == "RNA":
        bases = "ACGU"
    elif sequence_type == "protein":
        bases = "ACDEFGHIKLMNPQRSTVWY"  # This represents the 20 standard amino acids

    return "".join(random.choice(bases) for _ in range(length))


def es_adn(cadena):
    return all(i in DNA_components for i in cadena)


def es_arn(cadena):
    return all(i in RNA_components for i in cadena)


def identify(cadena):
    if es_adn(cadena):
        return "La cadena ingresada es ADN."
    elif es_arn(cadena):
        return "La cadena ingresada es ARN."
    else:
        return "La cadena ingresada es proteina."


length = 15
num_strings = 10

dna_sequences = []
rna_sequences = []
protein_sequences = []

# Generating randomly the strings
for i in range(num_strings):
    dna_sequences.append(generate_random_sequence(length, "DNA"))
    rna_sequences.append(generate_random_sequence(length, "RNA"))
    protein_sequences.append(generate_random_sequence(length, "protein"))




# • Implementar algoritmos para la transcripción de cadenas (de ADN a ARN).
def transcribe_to_rna(dna_sequence):
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence
with open("sequence_message.txt", "w") as file:
    for dna_i in dna_sequences:
        file.write(f"La siguiente secuencia: {dna_i} es: {identify(dna_i)}\n")
    for rna_i in rna_sequences:
        file.write(f"La siguiente secuencia: {rna_i} es: {identify(rna_i)}\n")
    for protein_i in protein_sequences:
        file.write(f"La siguiente secuencia: {protein_i} es: {identify(protein_i)}\n")
    
    file.write(f"\n\n TRANSCRIPCION DE ADN -> ARN\n")
    for dna_i in dna_sequences:
        file.write(f"ADN: {dna_i} -> ARN: {transcribe_to_rna(dna_i)}\n")
