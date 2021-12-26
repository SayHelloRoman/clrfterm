from setuptools import setup
import os.path


if os.path.exists('./readme.md'):
    with open("readme.md") as f:
        description = f.read()

else:
    description = ""

setup(name='clrfterm',
      version='1.1.0',
      description="Module that decorates your console",
      packages=['clrfterm'],
      long_description=description,
      long_description_content_type='text/markdown',
      url="https://github.com/SayHelloRoman/clrfterm",
      zip_safe=False,
      install_requires=[
          "wheel"
      ]
      )
