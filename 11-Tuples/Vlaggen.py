def vlag(geometrie, kleuren):
    uitvoer = ''
    if geometrie == 'verticaal':
        for i in range(len(kleuren)):
            if i + 1 == len(kleuren):
                uitvoer += kleuren[i]
            else:
                uitvoer += kleuren[i] + ' | '
        return uitvoer
    elif geometrie == 'horizontaal':
        for i in range(len(kleuren)):
            if i + 1 == len(kleuren):
                uitvoer += kleuren[i]
            else:
                uitvoer += kleuren[i] + '\n'
                uitvoer += '-' + '\n'
        return uitvoer
