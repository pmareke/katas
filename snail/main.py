from typing import List


class Snail:
    @staticmethod
    def process(input: List[List[int]]) -> List[int]:
        snail: List[int] = [input[0][0]]
        width = len(input)
        right, down = True, True
        x, y = 0, 0
        while True:
            # right -> down -> left -> up -> right -> ...
            if x + 1 < width and right:
                x += 1
            elif y + 1 < width and down:
                right = False
                y += 1
            elif x - 1 >= 0 and not right:
                down = False
                x -= 1
            elif y - 1 >= 0 and not down:
                right = True
                y -= 1
            if input[y][x] in snail:
                break
            snail.append(input[y][x])
        return snail
