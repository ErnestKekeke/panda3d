import json


class Metrics:

    def __init__(self):

        self.distance_travelled = 0
        self.collisions = 0
        self.goal_reached = False

    def save(self):

        data = {
            "distance_travelled":
                self.distance_travelled,

            "collisions":
                self.collisions,

            "goal_reached":
                self.goal_reached
        }

        with open(
            "results.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )