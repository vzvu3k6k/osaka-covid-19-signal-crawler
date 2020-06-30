import unittest
from .common import prepare_report
from ..report_json_presenter import ReportJsonPresenter

class TestReportJsonPresenter(unittest.TestCase):
  def test_filename(self):
    presenter = self.prepare_presenter('normal')
    self.assertEqual(presenter.filename(), '2020-06-30.json')

  def test_content(self):
    presenter = self.prepare_presenter('normal')
    self.assertEqual(presenter.content(), '''\
{
  "date": "2020-06-30",
  "signal_color": null,
  "感染経路不明者の前週増加比": 4.0,
  "感染経路不明者": 2.29,
  "確定診断検査における陽性率": 0.015,
  "患者受入重症病床使用率": 0.016
}''')

  def test_content_with_signal(self):
    presenter = self.prepare_presenter('has_signal')
    self.assertEqual(presenter.content(), '''\
{
  "date": "2020-05-22",
  "signal_color": "green",
  "感染経路不明者の前週増加比": 0.59,
  "感染経路不明者": 1.43,
  "確定診断検査における陽性率": 0.004,
  "患者受入重症病床使用率": 0.154
}''')

  @staticmethod
  def prepare_presenter(fixture_name):
    report = prepare_report(fixture_name)
    return ReportJsonPresenter(report)

if __name__ == '__main__':
  unittest.main()
