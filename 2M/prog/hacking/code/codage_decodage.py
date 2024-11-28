def chiffrer(texte, clef):
    alphabet_clair = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_code = calculer_alphabet(clef)

    texte_code = ""

    for c in texte:
        if c == ' ':
            texte_code = texte_code + ' '
        else:
            index = alphabet_clair.index(c)
            texte_code = texte_code + alphabet_code[index]
    return texte_code

def dechiffrer(texte_code, clef):
    alphabet_clair = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_code = calculer_alphabet(clef)

    texte = ""

    for c in texte_code:
        if c == ' ':
            texte = texte + ' '
        else:
            index = alphabet_code.index(c)
            texte = texte + alphabet_clair[index]
    return texte

def calculer_alphabet(clef):
    alphabet_clair = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_code = ''
    for c in alphabet_clair :
        index = alphabet_clair.index(c)
        index = ((index+clef)%26)
        alphabet_code = alphabet_code + alphabet_clair[index]
    
    return alphabet_code

def hacking(texte_code):
    alphabet_clair = 'abcdefghijklmnopqrstuvwxyz'
    distribution = []
    for i in range(26):
        distribution.append(0)
    for c in texte_code:
        if c != " ":
            index = alphabet_clair.index(c)
            distribution[index] = distribution[index] + 1
    print(distribution)
    mx = 0
    clef = 0
    for i in range(len(distribution)):
        if distribution[i] > mx:
            clef = i
            mx = distribution[i]
    print(mx,clef)
    return clef-4

message_clair = ""
message_code1 = "ifdv rekzhlv lev tzmzczjrkzfe hlz r drihlv c yzjkfziv gveurek gclj u le dzccverziv uvj yldscvj fizxzevj jli cvj izmvj ul kzsiv ifdv vjk uvmvelv lev glzjjrekv ivglsczhlv glzj le mrjkv vdgziv jfe fixrezjrkzfe gfczkzhlv srjvv jli cv jverk vk cvj tfejlcj r zejgziv uv efdsivljvj tzmzczjrkzfej cvj ifdrzej vkrzvek uv xireuj tfejkiltkvlij crzjjrek uviizviv vlo uvj dfeldvekj vdscvdrkzhlvj tfddv cv tfczjv vk cv grekyvfe cvli tlckliv dvcrexv uv kiruzkzfej vk u zewclvetvj xivthlvj r vkv kirejdzjv r kirmvij cr crexlv crkzev vk cv uifzk ifdrze cr tylkv uv c vdgziv ifdrze u fttzuvek drihlv cr wze u lev viv drzj jfe yvizkrxv gviuliv vetfiv rlafliu ylz mvlo kl hlv a raflkv gclj uv uvkrzcj jli le rjgvtk grikztlczvi uv cr ifdv rekzhlv tfddv gri vovdgcv cr mzv hlfkzuzveev uvj ifdrzej cvj tfehlvkvj dzczkrzivj uv ifdv cvj uzvlo vk cr ivczxzfe ifdrzev c rik vk c rityzkvtkliv ifdrzev"
message_code2 = "yvtl huapxbl bul jpcpspzhapvu xbp h thyxbl s opzavpyl wlukhua wsbz k bu tpssluhpyl klz obtislz vypnpulz zby slz ypclz kb apiyl yvtl lza klclubl bul wbpzzhual ylwbispxbl wbpz bu chzal ltwpyl zvu vynhupzhapvu wvspapxbl ihzll zby sl zluha la slz jvuzbsz h puzwpyl kl uvtiylbzlz jpcpspzhapvuz slz yvthpuz lahplua kl nyhukz jvuzaybjalbyz shpzzhua klyyplyl lbe klz tvubtluaz ltislthapxblz jvttl sl jvspzl la sl whuaolvu slby jbsabyl tlshunl kl ayhkpapvuz la k pumsblujlz nyljxblz h lal ayhuztpzl h ayhclyz sh shunbl shapul la sl kyvpa yvthpu sh jobal kl s ltwpyl yvthpu k vjjpklua thyxbl sh mpu k bul lyl thpz zvu olypahnl wlykbyl lujvyl hbqvbyk obp clbe ab xbl q hqvbal wsbz kl klahpsz zby bu hzwlja whyapjbsply kl sh yvtl huapxbl jvttl why leltwsl sh cpl xbvapkpluul klz yvthpuz slz jvuxblalz tpspahpylz kl yvtl slz kplbe la sh ylspnpvu yvthpul s hya la s hyjopaljabyl yvthpul"
#for i in range(26):
#    print(chiffrer(message_clair,i))

clef = hacking(message_code2)
print("Clef probable : ",clef)
print(dechiffrer(message_code2, clef))
print(len(message_code2))