from enum import Enum, auto

class SignalColor(Enum):
  RED = auto()
  YELLOW = auto()
  GREEN = auto()

  @classmethod
  def parse(self, color_name):
    if color_name == '赤':
      return self.RED
    if color_name == '黄':
      return self.YELLOW
    if color_name == '緑':
      return self.GREEN
    raise RuntimeError('Unknown color name')
