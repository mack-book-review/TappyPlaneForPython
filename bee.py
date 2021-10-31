from enemy import Enemy

class Bee(Enemy):
  def __init__(self):
    super().__init__([
      "assets/enemies/bee.png",
      "assets/enemies/bee-fly.png",
    ])