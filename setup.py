from setuptools import setup, find_packages

setup(name='scrapy-autoextract-demo',
      version='0.1',
      description='AutoExtract Page Objects interface for Scrapy demo',
      url='https://github.com/ivanprado/scrapy-autoextract-demo',
      author='Iván de Prado Alonso',
      author_email='prado@scrapinghub.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'scrapy-autoextract>=0.5.2',
          'scrapy>=2.4.1',
      ],
      zip_safe=False)