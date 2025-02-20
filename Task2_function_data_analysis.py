import matplotlib.pyplot as plt

def data_file_analysz(file_path):
    dna_sequences = {}
    current_id = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip().lower()

            if line.startswith(">"):
                current_id = line[1:]
                dna_sequences[current_id] = ""
            
            else:
                dna_sequences[current_id] += line
      
    all_letter_count= {}

    for seq_id, sequence in dna_sequences.items():
        letter_count = {"a": 0, "t": 0, "c": 0, "g": 0} 
        for letter in sequence:
            if letter in letter_count:
                letter_count[letter] += 1
    
        all_letter_count[seq_id] = letter_count.copy()
            
    return all_letter_count
    
def plot_data(dna_data):
    
    for seq, count in dna_data.items():
        plt.figure(figsize=(6,4))
        plt.bar(list(count.keys()), list(count.values()), color=['blue', 'red', 'green', 'purple'])
        plt.title(f"DNA Sequence {seq}")
        plt.xlabel("DNA Letters")
        plt.ylabel("Frequency")
        
    plt.show()