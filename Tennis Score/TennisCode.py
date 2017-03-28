##new beginning 
l=[]
final={}
player=[]
k=0
while(True):
    s=input()
    if s.strip() == '':
        break
    s=s.split(':')
    k=0
    if s[0] not in player:
        player.append(s[0])
    if s[1] not in player:
        player.append(s[1])
    s[2]=s[2].split(',')
    l.append(s)
for i in player:
    bo3=0
    bo5=0
    nosw=0
    nogw=0
    nosl=0
    nogl=0
    for j in l:
        if(i==j[0]):
            if len(j[2])<=3:
                bo3+=1
            else:
                bo5+=1
            for k in j[2]:
                k=k.split('-')
                a=int(k[0])
                b=int(k[1])
                if(a>b):
                    nosw+=1
                else:
                    nosl+=1
                nogw+=a
                nogl+=b
        if(i==j[1]):
            for k in j[2]:
                k=k.split('-')
                a=int(k[0])
                b=int(k[1])
                if(a<b):
                    nosw+=1
                else:
                    nosl+=1
                nogw+=b
                nogl+=a
    final[i]=[bo5,bo3,nosw,nogw,nosl,nogl]
c=len(player)
m=f=c
r=0
rank={}
l=0
i=0
r=0
q=0
pl=player[:]
miniu=player[0]
maxiu=player[0]
prevmax=prevmin=-999
pl2=[]
l=0
while(player!=[]):
    maxi=-999
    maxiu=player[0]
    miniflag=0
    maxiflag=0
    p=0
    q=0
    t=0
    if pl2==[]:
        l=0
    if l==0:
        for j in range(m):
            k=final[player[j]][l]
            if maxi<k:
                maxi=k
                maxiflag=1
                maxiu=player[j]
                
        for j in range(m):
            if final[player[j]][l]==maxi:
                pl2.append(player[j])
                
                t+=1
        if t==1:
            rank[r]=maxiu
            if maxiu in player[:]:
                player.remove(maxiu)  
                pl2.remove(maxiu)
                
                prevmax=-999
                r+=1
                m-=1
        else:
            l+=1
        
    else:
        maxi=-999
        mini=1000
        if l==4 or l==5:
            if pl2!=[]:  
                h=len(pl2)
                for j in range(h):
                    k=final[pl2[j]][l]
                    if mini>k:
                        mini=k
                        miniu=pl2[j]
                        
                for j in pl2[:]:
                    if final[j][l]==mini:
                        
                        q+=1
                    else:
                        pl2.remove(j)
            
        else:
            if pl2!=[]: 
                for j in pl2:   
                    h=len(pl2)
                    for j in range(h):
                        k=final[pl2[j]][l]
                        if maxi<k:
                            maxi=k
                            maxiflag=1
                            maxiu=pl2[j]
         
                for j in pl2[:]:
                    if final[j][l]==maxi:
                        
                        t+=1
                    else:
                        
                        pl2.remove(j)
        if q==1:  
            
            rank[r]=miniu
            if maxiu in player:
                player.remove(miniu)  
                pl2.remove(miniu)
                
            prevmax=-999
            r+=1
            m-=1
        else:
            l+=1  
        if t==1:
            
            rank[r]=maxiu
            if maxiu in player:
                player.remove(maxiu)  
                pl2.remove(maxiu)
                prevmax=-999
            r+=1
            m-=1
        else:
            l+=1       
for i in range(f):
    print(rank[i],end=' ')
    for j in final[rank[i]]:
        if(j==final[rank[i]][-1]):
            break
        print(j,end=' ')    
    print(j)
