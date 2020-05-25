import unittest
from .common import prepare_report
from ..report_json_presenter import ReportJsonPresenter

class TestReportJsonPresenter(unittest.TestCase):
  def setUp(self):
    report = prepare_report('normal')
    self.presenter = ReportJsonPresenter(report)

  def test_filename(self):
    self.assertEqual(self.presenter.filename(), '2020-05-22.json')

  def test_content(self):
    self.assertEqual(self.presenter.content(), '''\
{
  "date": "2020-05-22",
  "signal_color": "green",
  "感染経路不明者の前週増加比": 0.59,
  "感染経路不明者": 1.43,
  "確定診断検査における陽性率": 0.004,
  "患者受入重症病床使用率": 0.154
}''')

if __name__ == '__main__':
  unittest.main()
