from core import Make
import shutil


shutil.copy('theme/carbon_default/style.css', 'docs/style.css')
# Make('', 'title', 'description', name='1')

# Make('https://google.com', 'go to google', """
# this link is just for fun which direct you to gogle.com     
# """, name='1')
desk = """
hi, if you are seeing this link, you are so lucky to see it.
well, you should click on the button due to open the actual link :)
"""  # desk ? desc!

Make('https://google.com', 'go to google.com', desc=desk, click=True, name='click')
Make('https://google.com', 'go to google.com', desc=desk, click=False, name='redirect')