import io


def read_text(filePath):
    input_file = open(filePath, 'r')
    text_lines = input_file.readlines()
    input_file.close()
    return text_lines


class TextReader:
    def __init__(self, filePath):
        self.input_text_lines = read_text(filePath)
        self.line = -1
        self.pos_in_line = -1

    def has_next_line(self):
        return self.current_line_is_valid() & self.line + 1

    def is_a_valid_line(self, number_to_check):
        return number_to_check >= 0 & number_to_check <= self.input_text_lines.__len__() - 1

    def current_line_is_valid(self):
        return self.is_a_valid_line(self.line)

    def pos_is_negative(self):
        return self.line < 0

    def get_next_line(self):
        self.line += 1
        if self.current_line_is_valid():
            return self.input_text_lines[self.line]
        elif self.pos_is_negative():
            self.line = -1
            return self.get_next_line()
        else:
            # here is EOF
            return None

    def peek_next_line(self):
        if self.current_line_is_valid():
            return self.input_text_lines[self.line + 1]
        else:
            # here is EOF
            return None

    def get_previous_line(self):
        if self.current_line_is_valid():
            self.line -= 1
            if self.pos_is_negative():
                return None
            return self.input_text_lines[self.line]
        elif self.pos_is_too_negative():
            self.line = -1
            return self.get_next_line()
        else:
            # here is EOF
            return None