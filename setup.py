import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="proliferate",
  version="0.9.0",
  author="Sebastian Schuster",
  author_email="sebschu@gmail.com",
  description="command line tool to interface with a Proliferate server",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/sebschu/proliferate-client",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=[
    "httpsig>=1.3",
    "requests>=2.24"
  ],
  scripts=["proliferate"]
)