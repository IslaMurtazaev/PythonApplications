def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == '':
        return aStr
    return reverseString(aStr[1:]) + aStr[0]

def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if not x or x == word: return True
    if len(x) > len(word): return False
    elif x[0] == word[0]: return x_ian(x[1:], word[1:])
    return x_ian(x, word[1:])

def insertNewlinesRec(text, lineLength):
    """
    Helper function for insertNewlines
    Helps separate lines by WORDS, not by symbols

    text: a string containg the text to wrap
    lineLength: the number of characters to include on a line before wrapping the next word
    returns -> updated lineLength
    """
    if len(text) <= lineLength: return lineLength
    if text[lineLength-1] == ' ': return lineLength 
    else: return insertNewlinesRec(text, lineLength+1)

def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength:
        return text
    return text[:insertNewlinesRec(text, lineLength)] + '\n' + insertNewlines(text[insertNewlinesRec(text, lineLength):],lineLength)
print(insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20))