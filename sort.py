import os

def read_files_in_directory(directory):
    file_data = []
    
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file_data.append((file_name, lines))
    
    return file_data

def sort_files_by_line_count(file_data):
    return sorted(file_data, key=lambda x: len(x[1]))

def write_to_result_file(sorted_file_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for file_name, lines in sorted_file_data:
            file.write(f"{file_name}\n")
            file.write(f"{len(lines)}\n")
            file.writelines(lines)
            file.write('\n')  

def combine_files(directory, output_file):
    file_data = read_files_in_directory(directory)
    sorted_file_data = sort_files_by_line_count(file_data)
    write_to_result_file(sorted_file_data, output_file)

directory_path = 'text'  
output_file_path = 'result.txt'  

combine_files(directory_path, output_file_path)