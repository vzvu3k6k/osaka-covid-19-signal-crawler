import unittest
from ..signal_color import SignalColor

class TestSignalColor(unittest.TestCase):
  def test_stringify(self):
    self.assertEqual(SignalColor.stringify(SignalColor.RED), 'red')
    self.assertIsNone(SignalColor.stringify(None))
  
  def test_parse(self):
    self.assertEqual(SignalColor.parse('赤'), SignalColor.RED)
    with self.assertRaises(RuntimeError):
      SignalColor.parse('白')

if __name__ == '__main__':
  unittest.main()
