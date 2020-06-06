import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signal_crawler",
    version="0.0.1",
    author="vzvu3k6k",
    author_email="vzvu3k6k@gmail.com",
    description="A scraper for http://www.pref.osaka.lg.jp/default.html",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vzvu3k6k/osaka-covid-19-signal-crawler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
