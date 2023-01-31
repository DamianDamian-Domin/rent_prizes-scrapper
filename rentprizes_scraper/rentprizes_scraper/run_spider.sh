#!/bin/bash

#1 - spider
#2 - city

source ../../venv/Scripts/activate
scrapy crawl $2 -o results/$1/$2.json