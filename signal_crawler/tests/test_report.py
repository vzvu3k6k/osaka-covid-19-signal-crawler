import unittest
from datetime import date
from .common import prepare_report
from ..report import Report
from ..signal_color import SignalColor

class TestReport(unittest.TestCase):
  def test_missing_signal_color(self):
    report = prepare_report('normal')
    self.assertIsNone(report.signal_color())

  def test_signal_color(self):
    report = prepare_report('has_signal')
    self.assertEqual(report.signal_color(), SignalColor.GREEN)

  def test_date(self):
    report = prepare_report('normal')
    self.assertEqual(report.date(), date(2020, 6, 30))

  def test_感染経路不明者の前週増加比(self):
    report = prepare_report('normal')
    self.assertEqual(report.感染経路不明者の前週増加比(), 4.0)

  def test_感染経路不明者(self):
    report = prepare_report('normal')
    self.assertEqual(report.感染経路不明者(), 2.29)

  def test_確定診断検査における陽性率(self):
    report = prepare_report('normal')
    self.assertEqual(report.確定診断検査における陽性率(), 0.015)

  def test_患者受入重症病床使用率(self):
    report = prepare_report('normal')
    self.assertEqual(report.患者受入重症病床使用率(), 0.016)

  def test_unclosed_td(self):
    report = prepare_report('unclosed_td')
    self.assertEqual(report.患者受入重症病床使用率(), 0.016)

if __name__ == '__main__':
  unittest.main()
