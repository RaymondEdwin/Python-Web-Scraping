def StartUp():
    import requests as req
    from bs4 import BeautifulSoup as bs
    global soup
    useragentid = {
        "aser-agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x644) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    Url = "https://www.bbc.co.uk/news/england"

    Raw_HTML = req.get(Url, headers=useragentid)
    StatusCode = int(Raw_HTML.status_code)
    if StatusCode == 200:
        print("Successfully grabbed")
    else:
        print("Unable to access BBC NEWS")
    Content = req.get(Url, headers=useragentid).content
    soup = bs(Content, features="html.parser")


def Title():
    global first_header
    global TitLength
    first_header = soup.find_all("h3", attrs={"class": "gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text"})
    first_header = str(first_header)
    first_header = first_header.split("</h3>, ")
    first_header = str(first_header)
    first_header = (first_header).replace(
        """<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">""", " ")
    first_header = str(first_header)
    first_header = (first_header).replace("'", "")
    first_header = (first_header).replace("\\", "")
    first_header = (first_header).replace("[", "")
    first_header = (first_header).replace("]", "")
    first_header = (first_header).replace("</h3>", "")
    first_header = (first_header).replace("&amp; ", "")
    first_header = (first_header).split(",  ")
    myFinallist = []
    for i in first_header:
        if i not in myFinallist:
            myFinallist.append(i)
    Len = len(myFinallist)
    x = 0
    Lists2 = []
    Lists3 = []
    while Len != x:
        C = (myFinallist[x])
        C1 = (C[0])
        if C1 == " ":
            Lists2.append(C[1:])
            x = x + 1
        elif C1 != " ":
            Lists2.append(C)
            x = x + 1
    for i in Lists2:
        if i not in Lists3:
            Lists3.append(i)
    LengthOfL3 = len(Lists3)
    z = 0
    while z != LengthOfL3:
        print(Lists3[z])
        print("")
        z = z + 1


StartUp()
Title()
def Start():
    from time import sleep
    while 0==0:
        StartUp()
        Title()
        time.sleep
