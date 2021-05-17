def script(check, x, y):
    collisions, isGold = collide(check, x, y)
    if check("level") == 1:
        if isGold:
            return "take"
        elif check("wall", x+2, y):
            return "down"
        return "right"
    elif check("level") == 2:
        if isGold:
            return "take"
        elif check("gold", x, y-1):
            return "up"
        elif check("gold", x, y+1):
            return "down"
        elif check("gold", x, y-7):
            return "up"
        return "right"
    elif check("level") == 3:
        if isGold:
            return "take"
        elif collisions['left'] and not collisions['top']:
            return "up"
        elif collisions['top'] and not collisions['right']:
            return "right"
        elif collisions['right'] and not collisions['bottom']:
            return "down"
        elif collisions['bottom'] and not collisions['left']:
            return "left"
        elif check("wall", x-1, y-1):
            return "up"
        elif check("wall", x+1, y-1):
            return "right"
        elif check("wall", x-1, y+1):
            return "left"
        elif check("wall", x+1, y+1):
            return "down"
    elif check("level") == 4:
        if check("gold", x, y):
            return "take"
        elif check("wall", x+2, y+1) and collisions['left'] and not collisions['bottom'] and not check("wall", x+2, y):
            return "right"
        elif collisions['left'] and not collisions['top']:
            return "up"
        elif collisions['top'] and not collisions['right']:
            return "right"
        elif collisions['right'] and not collisions['bottom']:
            return "down"
        elif collisions['bottom'] and not collisions['left']:
            return "left"
        elif check("wall", x-1, y-1):
            return "up"
        elif check("wall", x+1, y-1):
            return "right"
        elif check("wall", x-1, y+1) and check("gold", x, y-6):
            return "up"
        elif check("wall", x-1, y+1):
            return "left"
        elif check("wall", x+1, y+1):
            return "down"
        elif check("gold", x, y-5):
            return "up"
    return "pass"


def collide(check, x, y):
    collisions = {'bottom': False, 'top': False, 'right': False, 'left': False}
    isGold = False
    if check('gold', x, y):
        isGold = True
    if check('wall', x + 1, y):
        collisions['right'] = True
    if check('wall', x - 1, y):
        collisions['left'] = True
    if check('wall', x, y + 1):
        collisions['bottom'] = True
    if check('wall', x, y - 1):
        collisions['top'] = True
    return collisions, isGold
