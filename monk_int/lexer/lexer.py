"""monk_int/lexer/lexer.py"""

from monk_int.token import token
from monk_int.token.token import Token


class Lexer:
    """Represents the Lexer portion of the monkey language interpreter

    Attributes:
      input: (str) The string of text that is being read from the monkey file
      position: (int) The current position in the input (points to the current char)
      readPosition: (int) Current reading position in input (after current char)
      ch: The current character that is being looked at
    """

    def __init__(self, input: str):
        """Initializes the the instance based off of the input provided

        Args:
          input: This is the string that is provided with the code to be interpreted
        """
        self.input: str = input
        self.position: int = 0
        self.readPosition: int = 0
        self.ch = None

    def readChar(self):
        # TODO Support Unicode ontop of just ASCII
        """Sets the value of ch to the next character and increments position and
        read position by 1 in the event that there is no next character ch is
        set to 0
        """
        if self.readPosition >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.readPosition]

        self.position = self.readPosition
        self.readPosition += 1

    def newToken(self, tokenType: token.TokenType, ch: str):
        return Token(tokenType, str(ch))

    def readIdentifier(self):
        """This function assembles the variable names out of the string of characters for our lexer
        the way it does it is by recording the initial position and then iterating throug the characters
        in the string until it is no longer a letter and then returns the slice of the string that is the
        variable name
        """
        position = self.position
        while self.ch.isalpha():
            self.readChar()
        return self.input[position : self.position]

    def readNumber(self):
        position = self.position
        while self.ch.isdigit():
            self.readChar()
        return self.input[position : self.position]

    def skipWhitespace(self):
        """This function loops through all the whitespace in the file to prevent it
        from reaching the lexer and it being attempted to be tokenized
        """
        while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
            self.readChar()

    def NextToken(self):
        self.skipWhitespace()
        match self.ch:
            case "=":
                print(token.ASSIGN, self.ch)
                tok = self.newToken(token.ASSIGN, self.ch)
            case ";":
                tok = self.newToken(token.SEMICOLON, self.ch)
            case "(":
                tok = self.newToken(token.LPAREN, self.ch)
            case ")":
                tok = self.newToken(token.RPAREN, self.ch)
            case ",":
                tok = self.newToken(token.COMMA, self.ch)
            case "+":
                tok = self.newToken(token.PLUS, self.ch)
            case "{":
                tok = self.newToken(token.LBRACE, self.ch)
            case "}":
                tok = self.newToken(token.RBRACE, self.ch)
            case 0:
                tok = self.newToken(token.EOF, "")
            case _:
                if self.ch.isalpha():
                    literal = self.readIdentifier()
                    tok_type = token.LookupIdent(literal)
                    tok = self.newToken(tok_type, literal)
                    """The Early return is necessary due to the affect of readIdentifier which ends
                    with the pointer already on the next char making self.readChar() below unnesecary
                    """
                    return tok
                elif self.ch.isdigit():
                    literal = self.readNumber()
                    tok_type = token.INT
                    tok = self.newToken(tok_type, literal)
                    return tok
                else:
                    tok = self.newToken(token.ILLEGAL, self.ch)
        self.readChar()
        return tok


def New(input: str):
    lxr = Lexer(input)
    lxr.readChar()
    return lxr
