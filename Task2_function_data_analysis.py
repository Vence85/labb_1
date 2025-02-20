import matplotlib.pyplot as plt #Importing maplotlib

def data_file_analysz(file_path):
    dna_sequences = {}
    current_id = None

    # Open the file and process it line by line
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip().lower() #cleaning the string and converts to lower case

            #creates key without ">" 
            if line.startswith(">"):
                current_id = line[1:]
                dna_sequences[current_id] = "" #Creates empty value

            else:
                dna_sequences[current_id] += line #append data as values

    # Count the frequency of each letter (a, t, c, g) in every sequence 
    all_letter_count= {}

    for seq_id, sequence in dna_sequences.items():
        letter_count = {"a": 0, "t": 0, "c": 0, "g": 0} 
        for letter in sequence:
            if letter in letter_count:
                letter_count[letter] += 1
    
        all_letter_count[seq_id] = letter_count.copy()
            
    return all_letter_count
    
def plot_data(dna_data):
    #Plot the bar chart for each DNA sequences   
    for seq, count in dna_data.items():
        plt.figure(figsize=(6,4))
        plt.bar(list(count.keys()), list(count.values()), color=['blue', 'red', 'green', 'purple'])
        plt.title(f"DNA Sequence {seq}")
        plt.xlabel("DNA Letters")
        plt.ylabel("Frequency")
        
    plt.show()