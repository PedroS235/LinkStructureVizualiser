"""
link_extractor is a module that is used to extract links from a website
"""
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup as BS
import requests
import colorama
import cProfile
import re

#init the colorama module
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
internal_url = []

def is_external(href):
    """
    Checks if the given href is external
    """
    return bool(urlparse(href).netloc)

def is_valid_href(href):

    """
    Checks if the href is valid
    """
    return not href == '#' and not href == '/'
def is_a_valid_url(url):
    """
    Checks if the given url is not a broken link
    """
    if urlparse(url).scheme == 'http' or urlparse(url).scheme == 'https':
        return bool(requests.get(url))
    else:
        return False


def extract_all_webpage_links(url):
    """
    This function extracts all the internal links from URL and stores the in internal_url
    """
    soup = BS(requests.get(url).text, "html.parser") #soup contains the html code of the website
    
    for link in soup.findAll('a'):
        href = link.get('href') #gets the href inside the <a> tag
        parsed_url = urljoin(url, href) #joins the href to the url
        if is_external(href):
            print(f'{GRAY} [-] External link: {parsed_url}')
            continue
        elif is_valid_href(href) and is_a_valid_url(parsed_url):
            if not parsed_url in internal_url:
                print(f'{GREEN} [*] internal link: {parsed_url}')
                internal_url.append(parsed_url)
       
    return internal_url

def extract_all_website_links(url, max_search=10):
    """
    @params max_search: maximum iterations that this function will do
    This function extracts all the internal links of the URL in the internal_url list
    """
    count = 0
    internal_url.append(url)
    links = extract_all_webpage_links(url)
    for link in links:
        count+=1
        extract_all_webpage_links(link)
        if count == max_search:
            break

def write_to_file(url):
    """
    Temporary function that converts the internal_url list in a .txt file
    """
    file = open('InternalLinks.txt', 'w')
    #extract_all_website_links(url)
    extract_all_website_links(url)
    internal_url.sort()
    for link in internal_url:
        file.write(link+'\n')
    file.close()

#write_to_file('https://www.codewars.com/dashboard')
#print('finish')
#write_to_file('https://infallible-varahamihira-e94f86.netlify.app')

if __name__ == "__main__":
    import cProfile
    cProfile.run("write_to_file('https://wwwfr.uni.lu')")