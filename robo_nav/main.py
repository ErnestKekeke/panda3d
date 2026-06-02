from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
import json


class WarehouseSim(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # World
        self.world = self.loader.loadModel("models/environment")
        self.world.reparentTo(self.render)
        self.world.setScale(0.1)
        self.world.setPos(-8, 42, 0)

        # Robot
        self.robot = self.loader.loadModel("models/misc/rgbCube")
        self.robot.reparentTo(self.render)
        self.robot.setScale(1)
        self.robot.setPos(0, 10, 1)

        # Goal
        self.goal = self.loader.loadModel("models/misc/sphere")
        self.goal.reparentTo(self.render)
        self.goal.setScale(1)
        self.goal.setPos(15, 30, 1)

        # Obstacles
        self.obstacles = []

        obstacle_positions = [
            (-5, 20, 1),
            (0, 20, 1),
            (5, 20, 1),
            (-8, 28, 1),
            (8, 28, 1)
        ]

        for pos in obstacle_positions:
            crate = self.loader.loadModel("models/misc/rgbCube")
            crate.reparentTo(self.render)
            crate.setScale(2)
            crate.setPos(*pos)
            self.obstacles.append(crate)

        # Camera
        self.camera.setPos(0, -20, 10)
        self.camera.lookAt(self.robot)

        # Controls
        self.keys = {
            "w": False,
            "s": False,
            "a": False,
            "d": False
        }

        for key in self.keys:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

        # Metrics
        self.distance_travelled = 0
        self.collisions = 0
        self.goal_reached = False

        # HUD
        self.stats = OnscreenText(
            text="Distance: 0",
            pos=(-1.3, 0.9),
            scale=0.05,
            mayChange=True
        )

        self.taskMgr.add(self.update, "update")

    def set_key(self, key, value):
        self.keys[key] = value

    def move_robot(self, dt):

        old_x = self.robot.getX()
        old_y = self.robot.getY()

        speed = 8

        if self.keys["w"]:
            self.robot.setY(self.robot, speed * dt)

        if self.keys["s"]:
            self.robot.setY(self.robot, -speed * dt)

        if self.keys["a"]:
            self.robot.setX(self.robot, -speed * dt)

        if self.keys["d"]:
            self.robot.setX(self.robot, speed * dt)

        dx = self.robot.getX() - old_x
        dy = self.robot.getY() - old_y

        self.distance_travelled += (dx * dx + dy * dy) ** 0.5

    def check_obstacles(self):

        for obstacle in self.obstacles:

            if self.robot.getDistance(obstacle) < 2:

                self.collisions += 1

    def check_goal(self):

        if self.robot.getDistance(self.goal) < 2:

            if not self.goal_reached:

                self.goal_reached = True

                print("GOAL REACHED!")

                self.save_results()

    def save_results(self):

        data = {
            "distance_travelled":
                round(self.distance_travelled, 2),

            "collisions":
                self.collisions,

            "goal_reached":
                self.goal_reached
        }

        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)

    def update_camera(self):

        x = self.robot.getX()
        y = self.robot.getY()

        self.camera.setPos(
            x,
            y - 20,
            10
        )

        self.camera.lookAt(self.robot)

    def update_hud(self):

        self.stats.setText(
            f"Distance: {self.distance_travelled:.1f}\n"
            f"Collisions: {self.collisions}\n"
            f"Goal: {'Yes' if self.goal_reached else 'No'}"
        )

    def update(self, task):

        dt = globalClock.getDt()

        self.move_robot(dt)

        self.check_obstacles()

        self.check_goal()

        self.update_camera()

        self.update_hud()

        return Task.cont


app = WarehouseSim()
app.run()