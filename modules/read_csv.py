import csv

def read_csv_line_by_line(file_path):
    """
    Generator function to read a CSV file line by line.
    
    :param file_path: Path to the CSV file.
    :param use_dict: If True, yield rows as dictionaries; otherwise as lists.
    :return: Yields each row in the CSV file.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                yield row
