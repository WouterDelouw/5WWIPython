def dubbels(lijst):
    resultaat = []

    for element in lijst:
        if lijst.count(element) > 1 and element not in resultaat:
            resultaat.append(element)

    return resultaat
