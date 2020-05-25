import os
from ..report import Report

def prepare_report(fixture_name):
  path = os.path.join(os.path.dirname(__file__), 'fixtures', f'{fixture_name}.html')
  with open(path, encoding='CP932') as f:
    return Report(f.read())
