import http.client
from report import Report

def fetch_page():
  conn = http.client.HTTPConnection("www.pref.osaka.lg.jp")
  conn.request("GET", "/default.html")
  response = conn.getresponse()
  if (response.status != 200):
    raise RuntimeError(f"HTTP request failed (status: {response.status})")
  return response.read().decode('CP932')

