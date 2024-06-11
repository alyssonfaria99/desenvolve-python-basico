URLs = ["www.google.com&quot","www.gmail.com&quot;", "www.github.com&quot; ","www.reddit.com&quot;", "www.yahoo.com&quot;"]
dominios = []

for i in range(0, len(URLs)):
    dominio = URLs[i][4:URLs[i].index('.com')]       
    dominios.append(dominio)

print(dominios)