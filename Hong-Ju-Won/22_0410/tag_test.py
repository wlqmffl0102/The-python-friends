f = open("C:/Users/ghdek/Documents/GitHub/The-python-friends/Hong-Ju-Won/22_0410/sample.txt", 'r')
f2 = open("C:/Users/ghdek/Documents/GitHub/The-python-friends/Hong-Ju-Won/22_0410/sample.html", 'w')

while True:
    line = f.readline()
    if not line: break
    f2.write(line)
f.close()
f2.close()
