# nima azri 
# 401 217 0066

s = ']JK[RT)VRPJV5)Nb)LXMNK[NJTN[)KXcX[P*)]X)VXJVJbN)VJ)[J)QJU)TJ[MR)_J)YJbJV6N)VJTQOR)[J)[JVcPX\QJNN)TJ[MR*)QJUJ)KN)YR\Q)KX[X)_J)LXMN6N)TQXMN])[J)MJ[)[NYX\R]X[b6N)VJTQOR)N[\JU)TXW*)\JOJ[6N)]X)]JcN)\QX[^)\QXMN*)UX]OJW)LXMN6N)TQXM)[J)KN)\X[J]6N)Y^UU)[NZ^N\])MJ[)33Q]]Y\C88PR]Q^K7LXV8LN6\QJQNM8\J[NWJTQ6VJ][R\33)N[\JU)TXWRM)_J)KN)LXVV^WR]b6N)LXMNK[NJTN[QJ)KNYNb_JWMRM7_J)OJ[JVX\Q)WJTXWRM)TN)WJV6N)TQXM)_J)LXMN6R)MJWN\QSXXNR)[J)MJ[)LXMN6R)TN)N[\JU)VRTXWRM)PQJ[J[)MJQRM7'

def symbol_probelity(text):

    x = list( set(s) )              
    
    symbol = {}
    for i in x:
        symbol[i] = text.count(i)

    return symbol
def print_dic(code):
    # print(code)
    l = list(code.items())
    # print(l)
    l.sort(key= lambda x: x[1], reverse=True)

    for i,j in l:
        print(f'{i}: {j}')
d = symbol_probelity(s)
print_dic(d)


# ) -> ' '             41 -> 32
f = ''
for i in s:
    x = ord(i) - 9
    f = f + chr(x)

print(f)

