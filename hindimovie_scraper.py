import urllib.request
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# BeautifulSoup setup
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
url = "https://uae.voxcinemas.com/movies/whatson"
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
html = client = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, "html.parser")

# Scraping movies, checking language and adding to movie list
movies = soup.find_all("article",attrs={'class':'movie-summary'})
hindi_movies = []

for movie in movies:
    movie_title = movie.find("h3").text
    lang = movie.find("p").find_next_sibling().text
    lang = lang[10:]
    
    if lang == "Hindi":
        hindi_movies.append(movie_title)


# Sending mail with extracted movie list        
from_addr, to_addr = "my_email", "mom_email"
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "This Week's Movies!"
body = "Hey mom! These are the movies playing this week: " + ", ".join(hindi_movies) + "."  
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(from_addr,'my_password')
content = msg.as_string()
server.sendmail(from_addr, to_addr, content)
server.quit()    

