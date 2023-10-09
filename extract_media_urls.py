import requests
import re
from bs4 import BeautifulSoup
import logging

log_filename = "logger.py"

unique_media_urls = set()

def extract_media_urls(): 
  try:
    rss_feed_url = input("Enter the RSS feed URL: ")   
    r = requests.get(rss_feed_url)
    logging.info("Visited URL: %s", rss_feed_url) 
    
    soup = BeautifulSoup(r.content, features='xml')
        
    items = soup.find_all('item')
    
    if not items:
      print("No items found in the RSS feed.")
    
    else:
      for item in items:
        content = str(item)
        quoted_url_pattern = r'(?<=")(https?://[^\s]+)(?=")'
        urls = re.findall(quoted_url_pattern, content)
        
        unquoted_urls = re.findall(r'<url>(https?://[^\s]+)</url>', content)
        
        all_urls = urls + unquoted_urls
        
        for url in all_urls:
          if '.jpg' in url or '.png' in url or '.mp4' in url or '.gif' in url:
            unique_media_urls.add(url)
            logging.info("Media URLs uploaded: %s", url) 
    
# check
    for url in unique_media_urls:
      print(url)
  
    return unique_media_urls
  
  except Exception as e:
    logging.error("An error occurred: %s", e)
    return set()
    
    
  
