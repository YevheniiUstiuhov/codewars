def solution(s):
    a = []
    for i in range(0,len(s),2):
        if i!=len(s)-1:
            a.append(s[i]+s[i+1])
        else:
            a.append(s[i]+'_');
    return a
  
