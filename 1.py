with open("1.txt","r") as f, open("1.txt","r") as g,open("1.txt","r") as l:
    for h in f:
        g.seek(0)
        for j in g:
            l.seek(0)
            for b in l:
                if h.strip() and j.strip() and b.strip() and (int(h)+int(j)+int(b))==2020:
                    print("%s %s %s %s" % (h.strip(),j.strip(),b.strip(),int(h)*int(j)*int(b)))
