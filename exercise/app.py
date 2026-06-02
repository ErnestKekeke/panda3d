from panda3d.core import loadPrcFileData, Point3
from direct.showbase.ShowBase import ShowBase


loadPrcFileData("", """
win-size 1920 1080
window-title My Game
""")


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.camera.setPos(0, -25, 0)
        self.camera.lookAt(Point3(0, 0, 0))

        env = self.loader.loadModel("models/environment")
        env.setScale(0.25, 0.25, 0.25)
        env.reparentTo(self.render)


my_game = MyGame()
my_game.run()

