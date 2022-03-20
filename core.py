import config
from bs4 import BeautifulSoup as bs
import re
import os


def Make(link: str, title: str, desc: str, click: bool = True) -> str:
    """make the link director

    Args:
        link (str): the link to be shortend.
        title (str): title in the site.
        click (bool, optional): redirect on open the link or click to open it. Defaults to True.
        name (str): uniq name for use as url
    Returns:
        str: return address of the link affter deploying out.
    """

    if click:
        path = os.path.join(config.DIR, config.CLICK_TO_OPEN)
    else:
        path = os.path.join(config.DIR, config.REDIRECT_ON_OPEN)

    with open(path, 'r') as fli:
        fli = fli.read()
        fli = re.sub('\{\{.*link.*\}\}', '"' + link + '"', fli)
        fli = re.sub('\{\{.*title.*\}\}', title, fli)
        fli = re.sub('\{\{.*description.*\}\}', desc, fli)
        print(fli)
        
        
Make('link', 'title', 'name', False)