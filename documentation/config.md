# config

to config the project you should open up `config.py` file which all the
config represenct there.

the config include *Theme* and *Deployment*

## Theme

> `DIR = "theme/carbon_default"`
> 
> in the theme section, to choose any other theme, leave the theme path directy in the qutes

> BASE = "base.html"
> 
> the base is a html file which all other html exept index will inherit it.
> for example if base have tag `<header> </header>`, the `redirect` and
> `click_to_open` will be push in to it.


> `CLICK_TO_OPEN = "click_to_open.html"`
> 
> the redirection html file which will ask user to click on a button to open
> the actual link.


> `REDIRECT_ON_OPEN = "redirect.html"`
> 
> html theme file which will redirect user immediatly.


> `INDEX = "index.html"`
>
> will specify the index file of the site.

## Deployment

> `BASE_URL = "https://shabane.github.io/carbon"`
>
> use your own github pages link in this variable.

> `PUBLISH_DIR = "docs"`
> 
> each generated file will copy here, github pages will look here for the html files.

> `MAX_URL_LENGTH = 4`
> 
> max length is a number which tell the core to generate links up to how much chars
> for example if you choose 4, it will limited to 4 chars to for each file name.

> `CHARS = []`
> 
> list of characters wich will use to generate a link, you can leave it with numbers
> or just alpha characters, or combine theme, or may you want to use **words** in it.
> to count how much word can be generate from the list,
> power length of list with Max_Url_length. 
> for example if we have a list with length of 10 and the max lengh is 4
> (10^4 = 10,000) we will have 10,000 different links

*kind of links*

- ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

- ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',...]

- ['ear', 'fear', 'pear', 'gear', 'tear', 'dear', 'bear', 'hear', 'near']
