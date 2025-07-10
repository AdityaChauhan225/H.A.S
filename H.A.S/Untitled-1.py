def list_to_string(lst):
    # Convert list elements to strings and join them with commas
    return ','.join(str(item) for item in lst)

def append_list_to_file(file_path, my_list):
    line_to_append = list_to_string(my_list) + '\n'

    with open(file_path, 'a') as file:
        file.writelines(line_to_append)

# Example usage:
file_path = 'data.txt'
my_list = [1, 'Task 1', '2023-07-25', True]

append_list_to_file(file_path, my_list)
