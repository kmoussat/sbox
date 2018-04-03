

def SBOX(l1,l2,l3,l4):
    box = [l1,l2,l3,l4]
    return box


def getOutput(title,value,sbox):
    print("\n\n")
    print(50 * "*")
    print(title + " " + str(value) + "\n")
    if len(str(value)) < 4:
        print("Incorrect value - Too short")
    elif len(str(value)) > 4:
        print("Incorrect value = Too long")
    else:
        print("Binary Input Value ==> " + str(value))
        rdgt = str(value)[:1] +  str(value)[-1:]
        row = int(str(rdgt),2)
        add_ct = ""
        if row == 0:
            add_ct = " (meaning row 4) "
        print("\nStep 1: Get first and last bit of"
              " the input value: " + str(value) + " --> " + str(rdgt))
        print("\nStep 2: Convert " + str(rdgt) + " to decimal to find the row " + str(row) + add_ct)


        cdgt = str(value)[1:-1]
        column = int(str(cdgt),2)
        add_ct2 = ""
        if column == 0:
            add_ct2 = " (meaning column 4) "
        print("\nStep 3: Get the middle 2 bits of"
              " the input value: " + str(value) + " --> " + str(cdgt))
        print("\nStep 4: Convert " + str(cdgt) + " to decimal to find the column " + str(column) + add_ct2)


        slist = getRow(row, sbox)
        out_dec,out_bin = getValue(slist,column)

        print("\nConclusion: In row " + str(row) + add_ct + ", column " + str(column) + add_ct2 + " appears " + str(out_dec) +
              ". This determines the output; " + str(out_dec) + " is binary " + addZeros(str(out_bin),2) +
              ". Hence S-BOX(" + str(value) + ") = " + addZeros(str(out_bin),2))

        #print("\n" + 50 * "*")

        return out_bin

def getValue(list,col):
    dec_value = list[col-1]
    bin_value = bin(dec_value)
    bin_value = str(bin_value)[2:]

    return dec_value,bin_value


def getRow(line, sbox):
    flist = []
    if line == 0:
        flist = sbox[3]
    elif line == 1:
        flist = sbox[0]
    elif line == 2:
        flist = sbox[1]
    elif line == 3:
        flist = sbox[2]


    return flist

def addZeros(str,l):
    nstring = str
    if len(str) < l:
        m = l - len(str)
        nstring =  (m * '0') + str

    return nstring

def main():

    #sbox = SBOX(l1,l2,l3,l4)
    '''
    a = getOutput("a)", '110000',sbox)
    b = getOutput("b)", '100001', sbox)
    c = getOutput("c)", '011110', sbox)
    d = getOutput("d)", '000111', sbox)
    e = getOutput("e)", '111111', sbox)
    f = getOutput("f)", '111110', sbox)
'''

    d1 = [3,2,1,2]
    d2 = [3,3,3,0]
    d3 = [1,0,0,2]
    d4 = [2,2,0,3]

    dbox = SBOX(d1,d2,d3,d4)
    print("s-BOX: \n " + str(dbox))
    q4 = getOutput("c) Example 4-to-2 S-Box : ", '1010',dbox)




main()
