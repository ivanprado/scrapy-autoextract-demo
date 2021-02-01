AutoExtract Page Objects interface for Scrapy demo
--------------------------------------------------

Simple project to show how to use the Page Objects interface to extract
data from http://blog.scrapinghub.com using AutoExtract.

Remember to configure the environmental variable ``SCRAPINGHUB_AUTOEXTRACT_KEY``
before running the project. 

Requirements
============
* python >= 3.7

Installation
============
    
    cd <project-folder>
    virtualenv -p python3.7 venv
    source venv/bin/activate
    pip install -e .

Run
===

    SCRAPINGHUB_AUTOEXTRACT_KEY=<your-key> scrapy crawl blog_scrapinghub

    