# your_script.py
import sys
import re

def extract_citations(latex_text):
    citations = re.findall(r'\\cite{([^}]*)}', latex_text)
    cited_references = [reference.strip() for citation in citations for reference in citation.split(',')]
    return cited_references

def count_references(cited_references):
    reference_count = {}
    for reference in cited_references:
        if reference in reference_count:
            reference_count[reference] += 1
        else:
            reference_count[reference] = 1
    return reference_count

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        latex_text = file.read()

    cited_references = extract_citations(latex_text)
    reference_count = count_references(cited_references)

    print("List of cited references:")
    for reference, count in reference_count.items():
        print(f"{reference}: {count} times")
    
    return cited_references

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    result = process_file(input_file_path)
    print(result)






