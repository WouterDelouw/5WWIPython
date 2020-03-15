def yiq(rgb):
    yiq = (round((0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]), 4), round((0.596 * rgb[0] - 0.274 * rgb[1] - 0.322 * rgb[2]), 4), round((0.211 * rgb[0] - 0.523 * rgb[1] + 0.312 * rgb[2]), 4))
    return yiq


