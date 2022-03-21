import config
import re
import os
import random


def Namer() -> str:
    """generate a random name for us as file name to for url.
    name will end with .html

    Returns:
        str: name of the file
    """

    file_name = None
    while not file_name and not os.path.exists(os.path.join(config.DIR, str(file_name))):
        for i in range(1, random.randint(1, config.MAX_URL_LENGTH + 1)):

            if not file_name:
                file_name = ''

            file_name += random.choice(config.CHARS)

    return file_name+'.hmlt'


def Make(link: str, name: str, title: str, desc: str, click: bool = True) -> str:
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

        if not os.path.exists(config.PUBLISH_DIR):
            os.mkdir(config.PUBLISH_DIR)
        # TODO check the name of the file is empy str or not, if so save it as random, if not, save it as the given name
        with open(os.path.join(config.PUBLISH_DIR, Namer()), 'w') as fliw:
            fliw.write(fli)


# Make('link', 'title', 'name', 'desc', False)
print(Namer())