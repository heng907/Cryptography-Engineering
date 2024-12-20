vowels=['A', 'E', 'I', 'O', 'U']
text = "UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECOHENIO DAARQ NAELA FSGNO PTE"
text = text.replace(" ", "")
# rectangle 7*14
# 把字存進來
rec_7x14=[]
idx=0
for i in range(14):
    rec_7x14.append([])
    for j in range(7):
        #if the word is not the uppercase letter, then skip
        # if(ord(text[idx]) < 65  or ord(text[idx]) > 90):
        #     idx += 1
        #if the  word is from A to Z
        rec_7x14[i].append(text[idx])
        idx += 1
        
print("for rectangle 7 X 14:")
diff_7x14=0
for i in range(7):
    vowelNum=0
    for j in range(14):
        #count the number of vowels in every rows
        if(rec_7x14[j][i] in vowels):
            vowelNum += 1
        print(rec_7x14[j][i], end=' ')
    diff=round(abs(vowelNum - 0.4 * 14), 2)
    diff_7x14 += diff
    print("\tdifference: " + str(diff))
print("average difference: " + str(diff_7x14/7))

# rectangle 14*7
rec_14x7=[]    
idx=0
for i in range(7):
    rec_14x7.append([])
    for j in range(14):
        # if(ord(text[idx]) < 65  or ord(text[idx]) > 90):
        #     idx += 1
        rec_14x7[i].append(text[idx])
        idx += 1  
        
print("\nfor rectangle 14 x 7:")         
diff147=0
for i in range(14):
    vowelNum=0
    for j in range(7):
        if(rec_14x7[j][i] in vowels):
            vowelNum += 1
        print(rec_14x7[j][i], end=' ')
    diff=round(abs(vowelNum - 0.4 * 7), 2)
    diff147 += diff
    print("\tdifference: " + str(diff))   
print("average difference: " + str(diff147/14))
    
print("\nThe plain text:")
for i in range(14):
        print(rec_14x7[4][i], end=' ')
        print(rec_14x7[1][i], end=' ')
        print(rec_14x7[5][i], end=' ')
        print(rec_14x7[6][i], end=' ')
        print(rec_14x7[0][i], end=' ')
        print(rec_14x7[3][i], end=' ')
        print(rec_14x7[2][i])