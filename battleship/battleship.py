def are_ships_destroyed(ships_map, hits_map):
    shipPos = []
    hitPos = []
    for n in range(len(ships_map)):
        if ships_map[n] == 'B':
            shipPos.append(n)
        if hits_map[n] == 'X':
            hitPos.append(n)
    if set(shipPos) == set(hitPos):
        return True
    else:
        return False
