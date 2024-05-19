from turtle import Turtle


class BrickManager:
    def __init__(self):
        self.bricks = []

    def create_bricks(self, level):
        self.clear_bricks()
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        y_positions = [250, 220, 190, 160, 130]

        if level == 1:
            brick_layout = [[1] * 10] * 5  # Simple grid for level 1
        elif level == 2:
            brick_layout = [[1 if (i + j) % 2 == 0 else 0 for i in range(10)] for j in
                            range(5)]  # Checker pattern for level 2
        else:
            brick_layout = [[1] * 10 if j % 2 == 0 else [0] * 10 for j in range(5)]  # Every other row for level 3

        for row in range(len(brick_layout)):
            bricks_in_row = [col for col in range(len(brick_layout[row])) if brick_layout[row][col] == 1]
            if not bricks_in_row:
                continue

            # Calculate the starting x position to center the row
            total_bricks = len(bricks_in_row)
            row_width = total_bricks * 55
            start_x = -row_width / 2 + 25  # Pad the start position by 25 pixels

            for index, col in enumerate(bricks_in_row):
                brick = Turtle("square")
                brick.color(colors[row])
                brick.shapesize(stretch_wid=1, stretch_len=2.5)
                brick.penup()
                x_position = start_x + index * 55
                y_position = y_positions[row]
                brick.goto(x_position, y_position)
                self.bricks.append(brick)

    def clear_bricks(self):
        for brick in self.bricks:
            brick.hideturtle()
        self.bricks.clear()
