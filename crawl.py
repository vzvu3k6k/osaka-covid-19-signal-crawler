import http.client
from report import Report

# TODO: エラーチェック
conn = http.client.HTTPConnection("www.pref.osaka.lg.jp")
conn.request("GET", "/default.html")
response = conn.getresponse()

r = Report(response.read().decode('CP932'))
print(r.日付())
print(r.患者受入重症病床使用率())
