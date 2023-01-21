def flood_fill(image, sr, sc, color):
    if image == None or image[sr][sc] == color:
        return image
    fill(image, sr, sc, image[sr][sc], color)
    return image
    
def fill(image, sr, sc, initial_color, color):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initial_color:
        return
    image[sr][sc] = color
    fill(image, sr + 1, sc, initial_color, color)
    fill(image, sr, sc + 1, initial_color, color)
    fill(image, sr - 1, sc, initial_color, color)
    fill(image, sr, sc - 1, initial_color, color)
    



image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

sr = 1
sc = 1
color = 2

result = flood_fill(image, sr, sc, color)
print(result)

should_be = [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1]
]