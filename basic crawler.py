import urllib2

page = urllib2.urlopen("").read()## specify url between " "
def next_link(page):
    s_link = page.find('<a href=')
    if s_link == -1:
        return None, 0
    else:
        s_quote = page.find('"', s_link)
        e_quote = page.find('"', s_quote + 1)
        url = page[s_quote + 1:e_quote]
        return url, e_quote
url, end_position = next_link(page)
def all_links(page):
    while page:
        url, end_position = next_link(page)
        if url:
            n = "\n"
            saved_links = open("saved links.txt","a")
            saved_links.write(url+n)
            page = page[end_position:]
        else:
            saved_links.write("End of links"+n)
            print "End of links"
            saved_links.close()
            break
print all_links(page)
