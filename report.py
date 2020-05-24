import re
import functools
from datetime import datetime
from signal_color import SignalColor
from bs4 import BeautifulSoup

class Report:
  def __init__(self, html, year=2020):
    self.soup = BeautifulSoup(html, 'html5lib')
    self.year = year

  def signal_color(self):
    text = self.soup.find(class_ = 'shingo_title').text
    match = re.compile('大阪府新型コロナ警戒信号：(.)色').search(text)
    return SignalColor.parse(match.group(1))

  def date(self):
    text = self.__details().group('date')
    return datetime.strptime(text, '%m月%d日').date().replace(year=self.year)
  
  def 感染経路不明者の前週増加比(self):
    return float(self.__details().group('感染経路不明者の前週増加比'))

  def 感染経路不明者(self):
    text = self.__details().group('感染経路不明者')
    match = re.search(r'([\d+\.]+)人', text)
    return float(match.group(1))

  def 確定診断検査における陽性率(self):
    text = self.__details().group('確定診断検査における陽性率')
    match = re.search(r'([\d+\.]+)%', text)
    return float(match.group(1)) * 0.01

  def 患者受入重症病床使用率(self):
    text = self.__details().group('患者受入重症病床使用率')
    match = re.search(r'([\d+\.]+)%', text)
    return float(match.group(1)) * 0.01

  def __details(self):
    details = self.soup.find(class_ = 'shingo-meisai-waku').prettify()
    pattern = r'''<div class="shingo-meisai-waku">
 <table>
  <tbody>
   <tr>
    <th(?:.+?)>
     大阪モデル・モニタリング指標
    </th>
    <th(?:.+?)>
     (?P<date>.+)
     <br/>
     現在
    </th>
    <th(?:.+?)>
     自粛要請等の基準
    </th>
    <th(?:.+?)>
     自粛解除の基準
    </th>
   </tr>
   <tr>
    <th(?:.+?)>
     分析事項
    </th>
    <th(?:.+?)>
     内容\(※\)
    </th>
   </tr>
   <tr>
   </tr>
   <tr>
    <td(?:.+?)>
     （１）市中での感染拡大状況
    </td>
    <td>
     ①感染経路不明者の前週増加比
    </td>
    <td(?:.+?)>
     (?P<感染経路不明者の前週増加比>.+)
    </td>
    <td(?:.+?)>
     1以上
    </td>
    <td(?:.+?)>
     －
    </td>
   </tr>
   <tr>
    <td>
     ②感染経路不明者数
    </td>
    <td(?:.+?)>
     (?P<感染経路不明者>.+)
    </td>
    <td(?:.+?)>
     5から10人以上
    </td>
    <td(?:.+?)>
     10人未満
    </td>
   </tr>
   <tr>
    <td>
     （２）新規陽性患者の発生状況
     <br/>
     ・検査体制のひっ迫状況
    </td>
    <td>
     ③確定診断検査における陽性率
    </td>
    <td(?:.+?)>
     (?P<確定診断検査における陽性率>.+)
    </td>
    <td(?:.+?)>
     7%以上
    </td>
    <td(?:.+?)>
     7%未満
    </td>
   </tr>
   <tr>
    <td>
     （３）病床のひっ迫状況
    </td>
    <td>
     ④患者受入重症病床使用率
    </td>
    <td(?:.+?)>
     (?P<患者受入重症病床使用率>.+)
    </td>
    <td(?:.+?)>
     －
    </td>
    <td(?:.+?)>
     60%未満
    </td>
   </tr>
  </tbody>
 </table>
 <div(?:.+?)>
  ※病床使用率以外の指標は７日間移動平均。
  <br/>
 </div>'''
    return re.search(pattern, details)
