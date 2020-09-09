# generate credit animation

left = 32
right = 63
width = right - left

# effect
SLIDE = 0x1
PLINK = 0x2

# directions
LEFT = 0x100
RIGHT = 0x200
UP = 0x400
DOWN = 0x800

# position
CENTRE = 0x1000

credits = [
    [SLIDE+RIGHT, 0, 10, "Sui Generics", CENTRE, 0],
#    [SLIDE+LEFT, 10, 10, "by pelrun", CENTRE, 1],
#    [SLIDE+UP, 20, 10, "for Syntax 2017", CENTRE, 2],
]

def process(entry):
    if (entry[0] & SLIDE and entry[0] & LEFT+RIGHT):
        slide_x(entry)
    elif (entry[0] & PLINK):
        plink(entry)

def plink(entry):
    pass

def slide_x(entry):
    strlen = len(entry[3])

    if (entry[0] & RIGHT):
        sx=left-strlen
        text=" "+entry[3]
    if (entry[0] & LEFT):
        sx=right
        text=entry[3]+" "
    if (entry[4] == CENTRE):
        ex=left+(width-strlen)/2
    else:
        ex=left+entry[4]

    if (sx<ex):
        step=1
    else:
        step=-1

    print [sx, ex]
    for cx in xrange(sx,ex,step):
        for elem in zip(xrange(cx,cx+strlen+1), list(text)):
            if elem[0]<left or elem[0]>right:
                continue
            


for elem in credits:
    process(elem)

