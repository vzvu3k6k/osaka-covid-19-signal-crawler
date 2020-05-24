from report import Report

def prepare_report(fixture_name):
  with open(f'fixtures/{fixture_name}.html', encoding='CP932') as f:
    return Report(f.read())
