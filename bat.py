from enemy import Enemy

class Bat(Enemy):
  def __init__(self):
    super().__init__([
      "assets/enemies/bat.png",
      "assets/enemies/bat-fly.png",
    ])