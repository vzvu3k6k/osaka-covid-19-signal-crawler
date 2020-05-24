import json

class ReportJsonPresenter:
  def __init__(self, report):
    self.report = report

  def filename(self):
    return f"{self.report.date()}.json"

  def content(self):
    content = {
      "date": self.report.date().isoformat(),
      "signal_color": self.report.signal_color().name,
      "感染経路不明者の前週増加比": self.report.感染経路不明者の前週増加比(),
      "感染経路不明者": self.report.感染経路不明者(),
      "確定診断検査における陽性率": self.report.確定診断検査における陽性率(),
      "患者受入重症病床使用率": self.report.患者受入重症病床使用率()
    }
    return json.dumps(content, indent=2, ensure_ascii=False)
