import requests from bs4 import BeautifulSoupimport reimport pprintres = requests.get('https://news.ycombinator.com/')soup = BeautifulSoup(res.text, 'html.parser')links = soup.select('.storylink')subtext = soup.select('.subtext')#print(links[0])def create_custom_hn(links, votes):     # hn = []    # link_li = []    # regex = re.compile('(<a.*href=")(.*)(">)(.*)(<\/a>)')    # for link in links:    #     m = regex.search(str(link))            #     if m:     #         hn.append(m.group(4))    #         link_li.append(m.group(2))    #         #print(m.group(2))                # print(hn)    # print(link_li)           hn = []    for idx, item in enumerate(links):         title = links[idx].getText()        href = links[idx].get('href', None)        vote = subtext[idx].select('.score')        if len(vote):             #print(vote)            points = int(vote[0].getText().replace(' points', ''))            if points > 100:             #print(points)                hn.append({'title': title, 'link': href, 'points': points})         #hn.append({'title': title, 'link': href, 'points': 0})                            return hn                    pprint.pprint(create_custom_hn(links, subtext))        