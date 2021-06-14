import requests
import bs4

def get_song_links(website):
    resp = requests.get(website)

    # print(resp.content) to print the content

    soup = bs4.BeautifulSoup(resp.content, features = "html.parser")

    #print(soup.a) #prints first element with a tag. We can use any other tag like body or title or head etc.
    #print(soup.a['href']) attribute,value pairs are stored as dictionaries

    links = soup.find_all("a", attrs = {"class":"title"}) #attrs selects the tags with specified attribute values

    #for link in links:
        #print(link) #in each link the attribute,value pairs are stored as dictionaries

        #print(link.get('href')) #or print(link[href]) 
    l_links = [link['href'] for link in links]
    return l_links

def get_lyrics(url):
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.content, features = "html.parser")

    verses = soup.find_all("p", attrs = {"class":"verse"})

    #for verse in verses:
        # print(f"{verse.text}\n\n") to print the lyrics     #print(verses) will print the lyrics along withe the html tags
    lyrics = [verse.text for verse in verses]
    return '\n\n'.join(lyrics)

def file_name(url):
    return url.split('/')[-1].replace(".html", ".txt")

def main():
    links  = get_song_links("https://www.metrolyrics.com/grateful-dead-lyrics.html")  
    for i in links:
        fname = file_name(i)
        break
    with open(fname, 'w') as f:
        f.write(get_lyrics(links[0]))
    print(get_lyrics(links[0]))
    #all_lyrics = [get_lyrics(i) for i in links] #to store each lyrics in a list
    #print(all_lyrics)

if(__name__ == "__main__"):
    main()
else:
    print("Imported not run")