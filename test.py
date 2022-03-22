"""
this is a test, run this test if you are developing the theme.
if you want to be cofortable on the theme developing, just
use this command. `watch -n 1 'python3 test.py'`
this command will run the test and make two test html page each one second
"""
from core import Make
import shutil


shutil.copy('theme/carbon_default/style.css', 'docs/style.css')

desk = """
hi, if you are seeing this link, you are so lucky to see it.
well, you should click on the button due to open the actual link :)
"""  # desk ? desc!

Make('https://google.com', 'go to google.com', desc=desk, click=True, name='click')
Make('https://google.com', 'go to google.com', desc='redirect you...', click=False, name='redirect')