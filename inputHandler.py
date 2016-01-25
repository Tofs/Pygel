import logging




handlers = {}

keyMap = {
    "esc" : 256,
    "c" : 67
}

actionMap = {
    "Pressed" : 1,
    "Released": 0
}

modMap = {
    "none" : 0
}


def addEvent(function, key = None, mod = "None", action = "Pressed"):
    key = key.lower()
    mod = mod.lower()

    if not key in keyMap:
        logging.error("Key '{0}' not found".format(key))
        return

    if not mod in modMap:
        logging.error("Mod '{0}' not found".format(mod))
        return

    if not action in actionMap:
        loggin.error("Action '{0}' not found".format(action))

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
        logging.debug("not bound: {0}".format(dicKey))
