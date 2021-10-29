def reverse(string):
    ans=""
    index=0+1
    while index<=len(string):
        ans+=string[-index]
        index+=1
    return ans
    
string="icecream.like.this.program.very.much"
reverse_str=""
words=string.count(".")
index=1
while index-1<=len(string)-2:
    temp=""
    while string[-index]!="." and words>0:
        temp+=string[-index]
        index+=1
    reverse_str+=reverse(temp)
    reverse_str+="."
    words-=1
    if words==0: break
    index+=1
reverse_str+=string[0:-index]
print(reverse_str)