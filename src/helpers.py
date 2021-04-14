def read_text(filePath):
    input_file = open(filePath, 'r')
    text_lines = input_file.readlines()
    input_file.close()
    return text_lines
