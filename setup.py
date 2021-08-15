from setuptools import setup


with open("readme.md") as f:
    setup(name='clrfterm',
          version='1.0',
          description=f.read(),
          packages=['clrfterm'],
          author_email='erastovka1933@gmail.com',
          zip_safe=False)
