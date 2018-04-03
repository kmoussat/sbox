

def SBOX(l1,l2,l3,l4):
    box = [l1,l2,l3,l4]
    return box


def getOutput(title,value,sbox):
    print("\n\n")
    print(50 * "*")
    print(title + " " + str(value) + "\n")
    if len(str(value)) < 6:
        print("Incorrect value - Too short")
    elif len(str(value)) > 6:
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
            add_ct2 = " (meaning column 16) "
        print("\nStep 3: Get the middle 4 bits of"
              " the input value: " + str(value) + " --> " + str(cdgt))
        print("\nStep 4: Convert " + str(cdgt) + " to decimal to find the column " + str(column) + add_ct2)


        slist = getRow(row, sbox)
        out_dec,out_bin = getValue(slist,column)

        print("\nConlusion: In row " + str(row) + add_ct + ", column " + str(column) + add_ct2 + " appears " + str(out_dec) +
              ". This determines the output; " + str(out_dec) + " is binary " + addZeros(str(out_bin),4) +
              ". Hence S-BOX(" + str(value) + ") = " + addZeros(str(out_bin),4))

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
    l1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
    l2 = [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8]
    l3 = [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0]
    l4 = [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

    sbox = SBOX(l1,l2,l3,l4)
    '''
    a = getOutput("a)", '110000',sbox)
    b = getOutput("b)", '100001', sbox)
    c = getOutput("c)", '011110', sbox)
    d = getOutput("d)", '000111', sbox)
    e = getOutput("e)", '111111', sbox)
    f = getOutput("f)", '111110', sbox)
'''

    d1 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10]
    d2 = [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5]
    d3 = [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15]
    d4 = [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

    dbox = SBOX(d1,d2,d3,d4)
    print("s-BOX: \n " + str(dbox))
    q2 = getOutput("Demonstration: ", '101110',dbox)




main()
