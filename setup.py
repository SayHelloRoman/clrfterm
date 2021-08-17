from setuptools import setup

with open("readme.md") as f:
    description = f.read()

setup(name='clrfterm',
      version='0.2',
      description="Module that decorates your console",
      packages=['clrfterm'],
      long_description=description,
      long_description_content_type='text/markdown',
      url="https://github.com/SayHelloRoman/clrfterm",
      zip_safe=False
      )
