from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_jobs(job_title):
    url = f"https://in.indeed.com/jobs?q={job_title}&l=&from=searchOnDesktopSerp&vjk=a875c99b50f1d8f9"

    
    driver = webdriver.Chrome() 
    driver.get(url)
    
    time.sleep(5) 

    html = driver.page_source
    driver.quit()
    bs = BeautifulSoup(html, "html.parser")
    
    job_cards_div = bs.find('div', id='mosaic-provider-jobcards')
    job_list = job_cards_div.find('ul', {'class': 'css-1faftfv eu4oa1w0'})
    jobs=job_list.findAll('div',{'class':'job_seen_beacon'})
    info=[]
    
    for job in jobs:
        title=job.find('h2',{'class':'jobTitle'})
        jtitle=title.text
        link=title.find('a').attrs['data-jk']
        url=f"https://in.indeed.com/viewjob?jk={link}&tk=1icitk8k1h31h82p&from=serp&vjs=3"
        company_name=job.find('span',{'class':'css-1h7lukg eu4oa1w0'}).text
        company_location=job.find('div',{'class':'css-1restlb eu4oa1w0'}).text
        data={
            'title':jtitle,
            'company name':company_name,
            'company location':company_location,
            'apply link':url
        }
        info.append(data)
        print(info)
        

if __name__ == "__main__":
    job_title="software developer"
    scrape_jobs(job_title)
    