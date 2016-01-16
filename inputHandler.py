
handlers = {}

keyMap = {
    "Esc" : 256
}

actionMap = {
    "Pressed" : 1,
    "Released": 0
}

modMap = {
    "None" : 0
}


def addEvent(function, key = None, mod = "None", action = "Pressed"):
    keyCode = keyMap[key]
    modCode = modMap[mod]
    actionCode = actionMap[action]


    key = (keyCode, modCode, actionCode)

    if not key in handlers:
        handlers[key] = []
    handlers[key].append(function)

def keyboardListner(window, key, scancode, action, mods):
    print "key: {0} scancode: {1} mods: {2} action: {3}".format(key, scancode,mods, action)
    dicKey  = (key, mods, action )
    if dicKey in handlers:
        for command in handlers[dicKey]:
            command()
    else:
        print dicKey
