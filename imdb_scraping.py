import urllib2 as ur
from bs4 import BeautifulSoup
import csv

url='https://www.imdb.com/search/title?title_type=feature&release_date=2005-01-01,2018-01-01&user_rating=1.0,10.0&num_votes=5000,500000&count=250&sort=moviemeter,asc'




with open('movie_rating.csv', mode='w') as f:
	writer=csv.writer(f)
	writer.writerow(['Title','Year','Type','Runtime','Genre','Rating','Director','No_of_ratings','Gross'])



first_run=True

for x in range(1,20):

    connection= ur.urlopen(url)
    html=connection.read()
    connection.close()

    soup=BeautifulSoup(html,'html.parser')

    base_url='https://www.imdb.com/search/title'


    if first_run:
    	link=base_url+soup.findAll('div',{'class':'lister list detail sub-list'})[0].findAll('div',{'class':'desc'})[0].findAll('a')[0].get('href')
        url=link
        first_run=False

    else:
    	link=base_url+soup.findAll('div',{'class':'lister list detail sub-list'})[0].findAll('div',{'class':'desc'})[0].findAll('a')[1].get('href')
        url=link
       

    
    for movie in soup.findAll('div',{'class':'lister-item-content'}):


        title=movie.findAll('a')[0].text

        year =movie.findAll('span')[1].text.strip('(').strip('I').strip(')').strip(' ').strip('(')

        try:
    	   type1=movie.findAll('span',{'class':'certificate'})[0].text
        except IndexError:
    	                 type1='NaN' 

    	
    	try:
    	   runtime=movie.findAll('span',{'class':'runtime'})[0].text
        except IndexError:
    	                 runtime='NaN' 
        


        try:
    	   genre=movie.findAll('span',{'class':'genre'})[0].text.strip(' ')
        except IndexError:
    	                 genre='NaN'


        try:
    	   rating=movie.findAll('div',{'class':'inline-block ratings-imdb-rating'})[0].get('data-value')
        except IndexError:
    	                 rating='NaN'


        try:
    	   director=movie.findAll('p',{'class':""})[1].contents[1].text
        except IndexError:
    	                 director='NaN'


        try:
    	   no_of_ratings=movie.findAll('span',{'name':'nv'})[0].get('data-value')
        except IndexError:
    	                 no_of_ratings='NaN'

        

        try:
    	   gross=movie.findAll('span',{'name':'nv'})[1].text
        except IndexError:
    	   gross='NaN'
    	

        with open('movie_rating.csv', mode='a') as f:

    	    writer=csv.writer(f)
    	    writer.writerow([title.encode('utf-8'),year.encode('utf-8'),type1.encode('utf-8'),runtime.encode('utf-8'),genre[1:].encode('utf-8'),rating.encode('utf-8'),director.encode('utf-8'),no_of_ratings.encode('utf-8'),gross.encode('utf-8')])



