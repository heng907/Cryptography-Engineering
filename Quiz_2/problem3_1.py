text = "UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECOHENIO DAARQ NAELA FSGNO PTE"
text = text.replace(" ", "")
vowels=['A', 'E', 'I', 'O', 'U']
#cnt = 0
#arr = []
index = 0
# # for index in range(len(text)):
#     if(ord(text[index]) < 65  or ord(text[index]) > 90):
#         index = index + 1
#         continue
#     cnt = cnt + 1
# L=cnt
L = len(text)
for i in range(1, L+1):
    if(L%int(i) == 0):
        print("For", i, "x", int(L/i) ,"rectangle, the avg of the difference is ", end='')
        vowel = L/i*0.4
        freq = [0] * i
        diff = 0.0
        for j in range(L):
            if(text[j] in vowels):
                freq[j%i] += 1
        for j in range(i):
            diff += abs(freq[j]-vowel)
        diff = diff/i # count the avg of diff
        print(diff)