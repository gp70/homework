def score(w):
  w = w.lower()
  wscore = 0
  bank = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,
          'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,
          'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,
          'v':4,'w':4,'x':8,'y':4,'z':10}
  for l in w:
    wscore += bank[l]
  return wscore


TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))
        
def add_word_across(board,word,r,c):
    s = score(word)
    wordx = word
    word = list(word)
    for n in range(len(word)):
        if board[r - 1][c + n - 1] == 't':
            s += 2 * score(word[n])
        if board[r - 1][c + n - 1] == 'd':
            s += score(word[n])
    for n in range(len(word)):
        if board[r - 1][c + n - 1] == 'T':
            s = s * 3
        if board[r - 1][c + n - 1] == 'D':
            s = s * 2
        board[r - 1][c + n - 1] = word[n]
    print(wordx + ': ' + str(s))
    
def add_word_down(board,word,r,c):
    s = score(word)
    wordx = word
    word = list(word)
    for n in range(len(word)):
        if board[r + n - 1][c - 1] == 't':
            s += 2 * score(word[n])
        if board[r + n - 1][c - 1] == 'd':
            s += score(word[n])
    for n in range(len(word)):
        if board[r + n - 1][c - 1] == 'T':
            s = s * 3
        if board[r + n - 1][c - 1] == 'D':
            s = s * 2
        board[r + n - 1][c - 1] = word[n]
    print(wordx + ': ' + str(s))

print(score('Apple'))
# Should be 9
print(score('Tremendous'))
# Should be 13
print(score('Quiz'))
# Should be 22
print(score('Hello'))
# Should be 8

b = make_scrabble_board()
print_board(b)
add_word_across(b,'apple',3,3)
add_word_down(b, 'evil',3,7)
print()
print_board(b)