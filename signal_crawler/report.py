import re
import functools
from datetime import datetime
from .signal_color import SignalColor
from bs4 import BeautifulSoup

class Report:
  def __init__(self, html, year=2020):
    self.soup = BeautifulSoup(html, 'html5lib')
    self.year = year

  def signal_color(self):
    text = self.soup.find(class_ = 'shingo_title').text
    match = re.search('大阪府新型コロナ警戒信号：(.)色', text)
    return SignalColor.parse(match.group(1))

  def date(self):
    pattern = re.compile(r'\d+月\d+日')
    text = self.__detail_node().find(string=pattern)
    text = re.search(pattern, text).group(0)
    return datetime.strptime(text, '%m月%d日').date().replace(year=self.year)
  
  def 感染経路不明者の前週増加比(self):
    return float(self.__find_detail_value('①感染経路不明者の前週増加比'))

  def 感染経路不明者(self):
    text = self.__find_detail_value('②感染経路不明者数')
    match = re.search(r'([\d+\.]+)人', text)
    return float(match.group(1))

  def 確定診断検査における陽性率(self):
    text = self.__find_detail_value('③確定診断検査における陽性率')
    match = re.search(r'([\d+\.]+)%', text)
    return float(match.group(1)) * 0.01

  def 患者受入重症病床使用率(self):
    text = self.__find_detail_value('④患者受入重症病床使用率')
    match = re.search(r'([\d+\.]+)%', text)
    return float(match.group(1)) * 0.01

  def __find_detail_value(self, label):
    header = self.__detail_node().find('td', string=label)
    return header.find_next_sibling('td').string

  def __detail_node(self):
    return self.soup.find(class_ = 'shingo-meisai-waku')
