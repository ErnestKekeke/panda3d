from panda3d.core import Point3


class World:

    def __init__(self, base):

        self.base = base

        self.environment = base.loader.loadModel(
            "models/environment"
        )

        self.environment.reparentTo(base.render)
        self.environment.setScale(0.1)
        self.environment.setPos(-8, 42, 0)

        self.goal = base.loader.loadModel(
            "models/misc/sphere"
        )

        self.goal.reparentTo(base.render)
        self.goal.setScale(1)
        self.goal.setPos(15, 30, 1)

        self.obstacles = []

        positions = [
            Point3(-5, 20, 1),
            Point3(0, 20, 1),
            Point3(5, 20, 1),
            Point3(-8, 28, 1),
            Point3(8, 28, 1)
        ]

        for pos in positions:

            crate = base.loader.loadModel(
                "models/misc/rgbCube"
            )

            crate.reparentTo(base.render)
            crate.setScale(2)
            crate.setPos(pos)

            self.obstacles.append(crate)