2026-02-21 22:19

Status: incomplete

Tags: [[Day 45 - Web Scraping with Beautiful Soup]] 

# Code snippets and Examples
```
from bs4 import BeautifulSoup

# import lxml

  

with open("website.html") as file:

content = file.read()

  

soup = BeautifulSoup(content, "html.parser")

# print(soup.title.name) # Get the name of the element (tag name)

# print(soup.title.string) # Get the content of the element

  

# print(soup.prettify())

  

# print(soup.a) # Prints the first anchor tag

# print(soup.li) # first list tag

  

# Finding and selecting particular elements (not just the first)

# all_anchor_tags = soup.find_all(name="a") # find all anchor tags

# print(all_anchor_tags)

# for tag in all_anchor_tags:

# print(tag.getText()) # Get the content of the element

# print(tag.get("href")) # Get a specific attribute

  

# all_li_tags = soup.find_all(name="li")

# a = [tag.string for tag in all_li_tags]

  

# for tag in a:

# print(tag)

  

# heading = soup.find(name="h1", id="name") # find an element using an attribute

# print(heading.getText())

  

# section_heading = soup.find(class_="heading")

# print(section_heading.getText())

# print(section_heading.name)

# print(section_heading.get("class"))

  

company_url = soup.select_one(selector="p a") # The selector follows basic css selector rules

print(company_url.get("href"))

  

headings = soup.select(selector=".heading") # This uses class selector

print(headings)
```


### Getting the most upvoted article from ycombinator
```
from bs4 import BeautifulSoup

import requests

  

response = requests.get("https://news.ycombinator.com/news")

  
  

soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.select(".submission .title .titleline")

upvote_tags = soup.find_all(name="span", class_="score")

article_texts = [article.getText().strip() for article in article_tags]

article_links = [article.select_one("a").get("href") for article in article_tags]

article_upvotes = [int(upvote.getText().split()[0]) for upvote in upvote_tags]

  
  

index_of_max = article_upvotes.index(max(article_upvotes)) # Find the index of the largest number.

print(f"Title: {article_texts[index_of_max]}")

print(f"Link: {article_links[index_of_max]}")
```