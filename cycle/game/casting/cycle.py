import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color, location):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        self._prepare_body(location)
        

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        self._segments[0].move_next()

        tail = Actor()
        tail.set_color(self._segments[0].get_color())
        tail.set_text("#")
        tail.set_position(self._segments[0].get_position())
        self._segments.append(tail)
        # update velocities
        

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, location):

        if location == "LEFT":
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 2)
        elif location == "RIGHT":
            x = int(constants.MAX_X / 4 * -1)
            y = int(constants.MAX_Y / 2)

        """
        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
        """
        head = Actor()
        head.set_position(Point(x,y))
        head.set_color(constants.RED if location == "LEFT" else constants.GREEN)
        head.set_text("@")
        self._segments.append(head)