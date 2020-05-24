import unittest
from report import Report
from signal_color import SignalColor
from datetime import date

class TestReport(unittest.TestCase):
  def test_signal_color(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.signal_color(), SignalColor.GREEN)
  
  def test_date(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.date(), date(2020, 5, 22))

  def test_感染経路不明者の前週増加比(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.感染経路不明者の前週増加比(), 0.59)

  def test_感染経路不明者(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.感染経路不明者(), 1.43)

  def test_確定診断検査における陽性率(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.確定診断検査における陽性率(), 0.004)

  def test_患者受入重症病床使用率(self):
    report = self.__prepare_report('normal')
    self.assertEqual(report.患者受入重症病床使用率(), 0.154)

  def __prepare_report(self, fixture_name):
    with open(f'fixtures/{fixture_name}.html', encoding='CP932') as f:
      return Report(f.read())

if __name__ == '__main__':
  unittest.main()