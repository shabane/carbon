# Theme

theme is made from **4** html file and one single style.

i start to breake down the concepts from scrach.

## Tags

- {{ link }}
  every where you use this tag, user *URL* will gona replace in this tag.

- {{ title }}
  every where you use this tag, user *title* will gona replace in this tag.
  
- {{ description }}
  every where you use this tag, user *description* will gona replace in this tag.
  
- {{ content }}
  this tag is just **used** in `base.html` file.
  two redirection file will replace with this tag in the base.


## base.html

probebly you should add <html>, <head>, <footer> tag in this file.
other two html file(redirect.html, click_to_open.html) will include in base.html and
will save with a new name for each page.
in the base you should use the style and favicon and or maybe meta tags


## index.html

this is the index file which will represent on the head of the domain.
this file is just for circulate the 404 status code.
each time you run carbon this file will copy to PUBLISH_DIR.

## redirect.html

each URL goes here! and whenever this file open, it will redirect you to the URL.

## click_to_open.html

URLs which user should click on button due to open, goes here.