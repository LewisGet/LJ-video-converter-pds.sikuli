def create(value, s, e, layout, color, size):
    setStart(s)
    setLayout(layout)
    createBlock(color)
    setText(value, size)
    setEnd(e)

def createBlock(color):
    if (color == "blue"):
        rightClick(Pattern("blocks.png").targetOffset(173,-97))
    else:
        rightClick(Pattern("blocks.png").targetOffset(25,-97))

    click(Pattern("rightClick.png").targetOffset(-51,-93))
    wait("modifiesPanel-2.png")

def setStart(s):
    click(Pattern("timeController.png").targetOffset(-42,-15))
    doubleClick(Pattern("timeController.png").targetOffset(41,-14))
    type(s[0])
    type(s[1])
    type(s[2])
    type(Key.ENTER)

def setEnd(e):
    wait(Pattern("modifiesPanel.png").targetOffset(-31,1))
    click(Pattern("modifiesPanel-1.png").targetOffset(100,1))
    doubleClick(Pattern("endTime.png").targetOffset(-10,-14))
    type(e[0])
    type(e[1])
    type(e[2])
    click(Pattern("endTime.png").targetOffset(2,33))

def setText(value, font):
    click(Pattern("modifiesPanel.png").targetOffset(-31,1))
    wait("textModifies.png")
    doubleClick(Pattern("textModifies-1.png").targetOffset(-65,-26))
    type("a", Key.CTRL)
    paste(value.decode("utf8"))
    setFontSize(font)
    click(Pattern("updateModifiesPanel.png").targetOffset(77,13))

def setLayout(value):
    if (value == 1):
        click(Pattern("zIndex.png").targetOffset(-14,-209))
    if (value == 2):
        click(Pattern("zIndex.png").targetOffset(-11,-171))
    if (value == 3):
        click(Pattern("zIndex.png").targetOffset(-14,-134))
    if (value == 4):
        click(Pattern("zIndex.png").targetOffset(-14,-100))
    if (value == 5):
        click(Pattern("zIndex.png").targetOffset(-12,-61))
    if (value == 6):
        click(Pattern("zIndex.png").targetOffset(-14,-23))
    if (value == 7):
        click(Pattern("zIndex.png").targetOffset(-13,12))
    if (value == 8):
        click(Pattern("zIndex.png").targetOffset(-12,50))

def setFontSize(value):
    doubleClick(Pattern("fontSize.png").targetOffset(-14,-29))
    type(value)

# test
#create("中文", ["00", "00", "17"], ["00", "02", "15"], 1, "main", "16")
#create("中文2", ["00", "00", "17"], ["00", "03", "00"], 2, "main", "18")