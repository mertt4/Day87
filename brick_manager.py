from turtle import Turtle
from brick import Brick


class BrickManager:
    def __init__(self):
        self.bricks = []

    def create_bricks(self, level):
        self.clear_bricks()
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        y_positions = [250, 220, 190, 160, 130]

        level_pattern = level % 3  # Cycle through 3 levels

        if level_pattern == 1:
            brick_layout = [[1] * 10] * 5  # Simple grid for level 1
        elif level_pattern == 2:
            brick_layout = [[1 if (i + j) % 2 == 0 else 0 for i in range(10)] for j in
                            range(5)]  # Checker pattern for level 2
        else:
            brick_layout = [[1] * 10 if j % 2 == 0 else [0] * 10 for j in range(5)]  # Every other row for level 3

        for row in range(len(brick_layout)):
            for col in range(len(brick_layout[row])):
                if brick_layout[row][col] == 1:
                    x_position = -255 + col * 55
                    y_position = y_positions[row]
                    # Create multi-hit bricks for higher levels
                    hits = 1 if level == 1 else 2  # Multi-hit bricks for higher levels
                    color = colors[row]
                    brick = Brick(position=(x_position, y_position), hits=hits, color=color)
                    self.bricks.append(brick)

    def clear_bricks(self):
        for brick in self.bricks:
            brick.hideturtle()
        self.bricks.clear()
