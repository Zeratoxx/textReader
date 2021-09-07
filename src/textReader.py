from helpers import read_text


class TextReader:
    def __init__(self, filePath):
        self.input_text_lines = read_text(filePath)
        self.line = -1
        self.pos_in_line = -1

    # ------ big checkers ------
    def is_a_valid_line(self, line):
        return 0 <= line < self.input_text_lines.__len__()

    def is_a_valid_line_and_a_valid_pos_in_line(self, line, pos_in_line):
        if self.is_a_valid_line(line):
            return 0 <= pos_in_line < self.input_text_lines[line].__len__()
        else:
            return False

    # ------ checkers ------
    def cur_line_is_valid(self):
        return self.is_a_valid_line(self.line)

    def cur_pos_and_cur_line_are_valid(self):
        return self.is_a_valid_line_and_a_valid_pos_in_line(self.line, self.pos_in_line)

    def has_next_line(self):
        return self.is_a_valid_line(self.line + 1)

    def has_previous_line(self):
        return self.is_a_valid_line(self.line - 1)

    def cur_line_is_negative(self):
        return self.line < 0

    def cur_line_is_too_far(self):
        return self.input_text_lines.__len__() <= self.line

    def get_next_line(self):
        if self.cur_line_is_valid() and self.has_next_line():
            self.line += 1
            return self.input_text_lines[self.line]
        elif self.cur_line_is_negative():
            self.line = 0
            return self.input_text_lines[self.line]
        else:
            # here is EOF
            return None

    def peek_next_line(self):
        if self.cur_line_is_valid() and self.has_next_line():
            return self.input_text_lines[self.line + 1]
        else:
            # here is EOF
            return None

    def get_previous_line(self):
        if self.cur_line_is_valid() and self.has_previous_line():
            self.line -= 1
            return self.input_text_lines[self.line]
        elif self.cur_line_is_too_far():
            self.line = self.input_text_lines.__len__() - 1
            return self.input_text_lines[self.line]
        else:
            # here is BOF (begin of file)
            return None

    def peek_previous_line(self):
        if self.cur_line_is_valid() and self.has_previous_line():
            return self.input_text_lines[self.line - 1]
        else:
            # here is BOF (begin of file)
            return None
