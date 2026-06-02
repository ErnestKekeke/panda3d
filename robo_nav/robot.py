class Robot:

    def __init__(self, base):

        self.base = base

        self.model = base.loader.loadModel(
            "assets/robot.glb"
        )

        self.model.reparentTo(base.render)

        self.model.setScale(1)
        self.model.setPos(0, 10, 1)

        self.speed = 8