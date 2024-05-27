import random
from brick import Brick
from powerup import PowerUp

CHANCE = 0.08


class BrickManager:
    def __init__(self):
        self.bricks = []
        self.active_powerups = []  # Track active power-ups

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

    def check_for_powerup(self, brick_position):
        if random.random() < CHANCE:  # chance to spawn a power-up
            powerup_type = random.choice(["expand_paddle", "shrink_paddle", "extra_life", "increase_speed",
                                          "decrease_speed", "multi_ball"])
            print(f"Spawning power-up: {powerup_type} at {brick_position}")
            return PowerUp(powerup_type, brick_position)
        return None

    def remove_brick(self, brick):
        self.bricks.remove(brick)
        powerup = self.check_for_powerup(brick.position())
        if powerup:
            print(f"Power-up Created: {powerup.powerup_type} at ({powerup.xcor()}, {powerup.ycor()}")
            self.active_powerups.append(powerup)

    def clear_bricks(self):
        for brick in self.bricks:
            brick.hideturtle()
        self.bricks.clear()
