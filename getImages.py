from PIL import Image, ImageTk
def getImages(size):
    images = {}
    images['P'] = ImageTk.PhotoImage(Image.open("chesspieces/whitepawn.png").resize((size,size), Image.ANTIALIAS))
    images['B'] = ImageTk.PhotoImage(Image.open("chesspieces/whitebishop.png").resize((size,size), Image.ANTIALIAS))
    images['N'] = ImageTk.PhotoImage(Image.open("chesspieces/whiteknight.png").resize((size,size), Image.ANTIALIAS))
    images['R'] = ImageTk.PhotoImage(Image.open("chesspieces/whiterook.png").resize((size,size), Image.ANTIALIAS))
    images['Q'] = ImageTk.PhotoImage(Image.open("chesspieces/whitequeen.png").resize((size,size), Image.ANTIALIAS))
    images['K'] = ImageTk.PhotoImage(Image.open("chesspieces/whiteking.png").resize((size,size), Image.ANTIALIAS))
    images['p'] = ImageTk.PhotoImage(Image.open("chesspieces/blackpawn.png").resize((size,size), Image.ANTIALIAS))
    images['b'] = ImageTk.PhotoImage(Image.open("chesspieces/blackbishop.png").resize((size,size), Image.ANTIALIAS))
    images['n'] = ImageTk.PhotoImage(Image.open("chesspieces/blackknight.png").resize((size,size), Image.ANTIALIAS))
    images['r'] = ImageTk.PhotoImage(Image.open("chesspieces/blackrook.png").resize((size,size), Image.ANTIALIAS))
    images['q'] = ImageTk.PhotoImage(Image.open("chesspieces/blackqueen.png").resize((size,size), Image.ANTIALIAS))
    images['k'] = ImageTk.PhotoImage(Image.open("chesspieces/blackking.png").resize((size,size), Image.ANTIALIAS))
    images['e'] = ImageTk.PhotoImage(Image.open("chesspieces/empty.png").resize((size,size), Image.ANTIALIAS))
    return images