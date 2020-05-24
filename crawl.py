import os
import http.client
import github
from report import Report
from report_json_presenter import ReportJsonPresenter

def fetch_page():
  conn = http.client.HTTPConnection("www.pref.osaka.lg.jp")
  conn.request("GET", "/default.html")
  response = conn.getresponse()
  if (response.status != 200):
    raise RuntimeError(f"HTTP request failed (status: {response.status})")
  return response.read().decode('CP932')

def get_repository(token, repository):
  return github.Github(token).get_repo(repository)

def save_json(repository, report, committer):
  return repository.create_file(
    path=f"v1/{report.filename()}",
    content=report.content(),
    message="Update",
    branch="gh-pages",
    committer=committer,
  )

html = fetch_page()
report = Report(html)

repository = get_repository(
  os.environ.get("GITHUB_TOKEN"),
  os.environ.get("GITHUB_REPOSITORY")
)
committer = github.InputGitAuthor(
  os.environ.get("GIT_COMMITTER_NAME"),
  os.environ.get("GIT_COMMITTER_EMAIL")
)
save_json(repository, ReportJsonPresenter(report), committer)
