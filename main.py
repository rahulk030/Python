# Importing necessary libraries
from collections import Counter

# Defining a function to count word frequency and save a report
def generate_word_frequency_report(input_file, output_file):
    # Reading the content of the text file
    with open(input_file, 'r') as file:
        text_content = file.read()

    # Tokenizing the text into words
    words = text_content.split()

    # Counting word frequency
    word_counts = Counter(words)

    # Sorting words by frequency from most to least
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Saving the report to the output file with formatted columns for Word and Frequency 
    with open(output_file, 'w') as output:
        output.write(f'{"Word":<15}{"Frequency"}\n')
        for word, count in sorted_word_counts:
            output.write(f'{word:<15}{count}\n')

# Calling the function with the provided file names
generate_word_frequency_report('sample.txt', 'sampleReport.txt')
