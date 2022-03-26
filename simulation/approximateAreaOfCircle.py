from random import random

from .simulation import Simulation


class ApproximateAreaOfCircle(Simulation):
    def __init__(self):
        Simulation.__init__(self, 3, 3)
        self.area_of_square = 2 * 2
        self.center_circle = {'x': 0, 'y': 0}
        self.number_of_points_to_randomize = 1000000

    def distance_from_centre(self, x, y):
        return (((x - self.center_circle['x']) ** 2) + ((y - self.center_circle['y']) ** 2)) ** 0.5

    def simulate(self):
        """
          Uses the Buffon-Laplace Method using a 2x2 with centre in the centre of the 2x2 square (area of 4) and a
          circle with radius of 1. This has the premise that a point that is randomized uniformly and selected n times
          in the circle enclosed 2x2 square will uphold the following ratio

          number of points in the circle        area of the circle
          ------------------------------   ==  --------------------
          number of points randomized           area of the square
        :return: the  Buffon-Laplace estimation over self.number_of_points_to_randomize randomized points
        """

        point_in_circle_count = 0

        for i in range(0, self.number_of_points_to_randomize):
            # no need to consider negative points for x or y since we are calculating the distance
            # (i.e. values are squared)
            x = random()  # randomize x between [0, 1)
            y = random()  # randomize x between [0, 1)

            # if the euclidean distance is less than one we are with the radius of the circle
            if self.distance_from_centre(x, y) <= 1:
                point_in_circle_count += 1

        return 4 * (point_in_circle_count / self.number_of_points_to_randomize)
