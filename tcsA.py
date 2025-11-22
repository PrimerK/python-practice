def get_token(a,dik,lisr,liso):
    su=0
    if a in lisr:
        mark=-1
        for k in range(len(lisr)):
            if lisr[k]==a:
                mark=k
        for l in range(len(liso[mark])):
            su+=get_token(liso[mark][l],dik,lisr,liso)
        su+=len(liso[mark])-1
        if a in dik:
            dik[a]=min(dik[a],su)
        else:
            dik[a]=su
        return dik[a]
    else:
        dic[a]=0
        return 0



n=int(input())
con=input()
lines=[]
for i in range(n):
    line=list(map(str,input().split('=''+')))
    lines.append(line)
    con=input()
goal=input()

ress=[]
os=[]
for i in range(n):
    line=str(lines[i])
    res=''
    ori=''
    tem=''
    oris=[]
    for j in range(len(line)):

        if line[j]=='=':
            res=tem
            tem=''
            ress.append(res)
        elif line[j]=='+':
            ori=tem
            tem=''
            oris.append(ori)
        elif line[j]=='['or line[j]==']'or line[j]=="'":
            continue
        else:
            tem+=line[j]
    ori=tem
    oris.append(ori)
    os.append(oris)


lis=[]
dic={}

for i in range(len(ress)):
    if ress[i] not in dic:
        dic[ress[i]]=get_token(ress[i],dic,ress,os)
    else:
        dic[ress[i]]=min(dic[ress[i]],get_token(ress[i],dic,ress,os))

print(dic[goal])


'''for i in range(len(os)):
    for j in range(len(os[i])):
        if os[i][j] not in ress:
            dic[os[i][j]] = 0
for i in range(len(ress)):
    if ress[i] not in dic:
        summ=0
        for j in range(len(os[i])):
            summ+=dic[os[i][j]]
        summ+=len(os[i])-1
        dic[ress[i]]=summ
    else:
        summ=0
        for j in range(len(os[i])):
            summ+=dic[os[i][j]]
        summ+=len(os[i])-1
        dic[ress[i]]=min(summ,dic[ress[i]])
print(dic[goal])

def get_token(a,dik,lisr,liso):
    su=0
    if a in lisr:
        mark=-1
        for k in range(len(lisr)):
            if lisr[k]==a:
                mark=k
        for l in range(len(liso[mark])):
            su+=get_token(liso[mark][l],dik,lisr,liso)
        su+=len(liso[mark])-1
        if a in dik:
            dik[a]=su
        else:
            dik[a]=min(dik[a],su)
        return dik[a]
    else:
        dic[a]=0
        return 0'''








