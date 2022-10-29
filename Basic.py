 def ored_by(self, other):
    return None, self.illegal_operation(other)

  def notted(self):
  def notted(self, other):
    return None, self.illegal_operation(other)

  def execute(self, args):
    
        self.error_name = error_name
        self.details = details

    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details=''):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)


def __init__(self, idx, ln, col, fn, ftxt):
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.col = 0
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
def copy(self):
  
#######################################
# TOKENS
#######################################

TT_INT      = 'INT'
TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
def copy(self):
TT_RPAREN   = 'RPAREN'

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()


    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
def __repr__(self):

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
def make_tokens(self):
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, pos_start=self.pos))
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, f"'{char}'")
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
              def make_number(self):
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)
            return Token(TT_FLOAT, float(num_str))

#######################################
# RUN
#######################################

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    

    return tokens, error
#######################################
# MAIN
#######################################
import basic
