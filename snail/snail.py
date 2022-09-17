from typing import List


class Snail:
    @staticmethod
    def process(input_list: List[List[int]]) -> List[int]:
        snail: List[int] = [input_list[0][0]]
        width = len(input_list)
        right, down = True, True
        x_coordinate, y_coordinate = 0, 0
        while True:
            # right -> down -> left -> up -> right -> ...
            if x_coordinate + 1 < width and right:
                x_coordinate += 1
            elif y_coordinate + 1 < width and down:
                right = False
                y_coordinate += 1
            elif x_coordinate - 1 >= 0 and not right:
                down = False
                x_coordinate -= 1
            elif y_coordinate - 1 >= 0 and not down:
                right = True
                y_coordinate -= 1
            if input_list[y_coordinate][x_coordinate] in snail:
                break
            snail.append(input_list[y_coordinate][x_coordinate])
        return snail
