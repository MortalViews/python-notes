import argparse
from pycrawler.crawler import crawl
def main():
    parser = argparse.ArgumentParser(description='Python webcrawler')
    parser.add_argument('--url','-u',help="The base url to crawl")
    parser.add_argument('--depth','-d',help="depth to crawl")
    parser.add_argument('--job','-j',help="crawl job name")
    args = parser.parse_args()
    
    crawl(url=args.url,depth=args.depth)
    