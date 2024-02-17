from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name="fake-headers",
    version="1.0.2-dw",
    author="TheDevFromKer",
    license="MIT",
    description="Package for generate headers to http requests.",
    url="https://github.com/TheDevFromKer/Fake-Headers",
    packages=[str('fake_headers')],
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    tests_require=["bs4", "html5lib"]
)
