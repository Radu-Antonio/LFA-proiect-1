def add_tranzitie(start, end, char, msg):
    if start in noduri:
        noduri[start].append((end, char, msg))
    else:
        noduri[start] = [(end, char, msg)]


def dfs(nod, cuvant):
    global acceptat
    if len(cuvant) == 0:
        if nod in fin:
            acceptat = True
    else:
        for nod_urm, char, msg in noduri.get(nod, []):
            if cuvant[0] == char:
                traseu.append(nod_urm)
                mesaj.append(msg)
                dfs(nod_urm, cuvant[1:])
                break


g = open("output.txt", 'w')
f = open("input.txt")

noduri = {}
n, m = f.readline().split()

for _ in range(int(m)):
    start, end, char, msg = f.readline().split()
    add_tranzitie(start, end, char, msg)

init = f.readline().strip()
_, *fin = f.readline().split()
fin = set(fin)
nr_cuv = f.readline().strip()

for _ in range(int(nr_cuv)):
    cuvant = f.readline().strip()
    traseu = [init]
    mesaj = []
    acceptat = False
    dfs(init, cuvant)
    if acceptat:
        g.write("DA\n")
        g.write("".join(mesaj) + "\n")
        g.write("Traseu: " + " ".join(traseu) + "\n")
    else:
        g.write("NU\n")

f.close()
g.close()
