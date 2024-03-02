'''
The Stew.py module is intended for Beautiful Soup 
implenentations in the Help Desk Assistant app. 
main() should be for development only, not for user side execution.
'''

# region IMPORTS ======================================== #
from bs4 import BeautifulSoup as bs
import requests

# endregion ============================================= #



# region EXAMPLES ======================================= #

# Example using Requests module
# to obtain html content of a site
url = "https://www.google.com"
raw = requests.get(url)
data = raw.text

# Uncomment to see output
# print(data)



# Example of Beautiful Soup reading data from the site url
# then removing tags and spitting out clean data for parsing
html_content = """
<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a test paragraph.</p>
        <div>More <span>text</span> here.</div>
    </body>
</html>
"""
# Parsing the HTML content with BeautifulSoup
soup = bs(html_content, 'html.parser')
# Extracting all text from the parsed HTML
text_only = soup.get_text()
# Uncomment to see output
#print(text_only.strip())

# endregion ============================================== #



# region __name__ ======================================= #

'''Code Here'''

# main for testing

class KnowledgeBase:

    # Static KB information #

    # Help desk phone number
    PHONE_NUMBER = ""
    # Z's sacred 6 points
    SIX_POINTS = ""
    

    # Functions #

    # takes a string and searches the specified URL
    # for a list of RC contact information. 
    # returns a string 
    def rc_contact(entry) -> str:
        '''Search url "https://services.pitt.edu/TDClient/33/Portal/KB/ArticleDet?ID=218" for the specified RC escalation contacts'''




def main():
    '''Code Here'''

if __name__ == "__main__":
    main()

# endregion =============================================










