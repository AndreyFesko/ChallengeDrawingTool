import sys


class Drawing():
    """
    Class Drawing.
    The init takes the length and height, which creates an empty matrix of specified sizes.
    """
    def __init__(self, length, height):
        self.length = int(length)
        self.height = int(height)
        self.matrix = [[' ' for _ in range(self.length+2)] for _ in range(self.height+2)]
        self.commands = {
            'L': self.line,
            'R': self.rectangle,
            'B': self.bucket_fill
        }

    def create_border(self):
        """The method draws border."""
        # Upper and lower bound.
        for i in range(self.length+2):
            self.matrix[0][i] = '-'
            self.matrix[self.height+1][i] = '-'

        # Left and right side.
        for i in range(self.height+1)[1:]:
            self.matrix[i][0] = '|'
            self.matrix[i][self.length+1] = '|'

    def line(self, *args):
        """The method draw lines."""
        try:
            for arg in args:
                if arg[0] == arg[2]:
                    # Draw horizontal line.
                    cursor = arg[1]
                    while arg[3] >= cursor:
                        self.matrix[cursor][arg[0]] = 'x'
                        cursor += 1
                else:
                    # Draw vertical line.
                    cursor = arg[0]
                    while arg[2] >= cursor:
                        self.matrix[arg[1]][cursor] = 'x'
                        cursor += 1
        except IndexError:
            sys.exit('Invalid values!')

    def rectangle(self, *args):
        """The method draws rectangle."""
        try:
            for arg in args:
                # Upper and lower bound.
                cursor = arg[0]
                while cursor <= arg[2]:
                    self.matrix[arg[1]][cursor] = 'x'
                    self.matrix[arg[3]][cursor] = 'x'
                    cursor += 1

                # Left and right side.
                cursor = arg[1]
                while cursor <= arg[3]:
                    self.matrix[cursor][arg[0]] = 'x'
                    self.matrix[cursor][arg[2]] = 'x'
                    cursor += 1
        except IndexError:
            sys.exit('Invalid values!')

    def bucket_fill(self, *args):
        """
        The method floods with a symbol.
        Recursion is used.
        """
        try:
            for arg in args:
                if self.matrix[arg[1]][arg[0]] == ' ':
                    self.matrix[arg[1]][arg[0]] = arg[2]
                    self.bucket_fill([arg[0]+1, arg[1], arg[2]])
                    self.bucket_fill([arg[0]-1, arg[1], arg[2]])
                    self.bucket_fill([arg[0], arg[1]+1, arg[2]])
                    self.bucket_fill([arg[0], arg[1]-1, arg[2]])
        except IndexError:
            sys.exit('Invalid values!')

    def write_current_matrix(self):
        """The method writes to the file the current state of the picture"""
        with open('output.txt', 'a+') as file:
            for line in self.matrix:
                line = map(str, line)
                line = ''.join(line)
                file.write(line + '\n')


def main():
    try:
        with open('input.txt', 'r') as file:
            for line in file:
                line = line.rstrip().split(' ')
                for idx, token in enumerate(line):
                    if token.isdigit():
                        line[idx] = int(token)
                if line[0] == 'C':
                    obj = Drawing(line[1], line[2])
                    obj.create_border()
                    continue
                try:
                    obj.commands[line[0]](line[1:])
                    obj.write_current_matrix()
                except UnboundLocalError:
                    sys.exit('First you need to create a canvas!')
    except OSError:
        sys.exit('File issues!')


if __name__ == '__main__':
    main()
