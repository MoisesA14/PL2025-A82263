import re

obras= open("obras.csv", "r", encoding="utf8")

comps = list()
obras_p_periodo = dict()
periodo_p_obras = dict()

string = obras.read()

for linha in re.findall(r"(?:[^;]+;){6}[^;\n]+", string):
    if linha!='nome;desc;anoCriacao;periodo;compositor;duracao;_id':
        obra = re.split(r";", linha, 0)
        if(obra[4] not in comps):
            comps.append(obra[4])
        if(obra[3] not in obras_p_periodo.keys()):
            obras_p_periodo[obra[3]] = 1
            periodo_p_obras[obra[3]] = list()
            periodo_p_obras[obra[3]].append(re.sub("\n", "", obra[0], 0))
        else:
            obras_p_periodo[obra[3]] += 1
            periodo_p_obras[obra[3]].append(re.sub("\n", "", obra[0], 0))

comps.sort()
for periodo in periodo_p_obras.keys():
    periodo_p_obras[periodo].sort()

print(comps)
print(obras_p_periodo)
print(periodo_p_obras)

obras.close()