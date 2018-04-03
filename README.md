# sbox

s-BOX: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]



**************************************************
Demonstration:  101110

Binary Input Value ==> 101110

Step 1: Get first and last bit of the input value: 101110 --> 10

Step 2: Convert 10 to decimal to find the row 2

Step 3: Get the middle 4 bits of the input value: 101110 --> 0111

Step 4: Convert 0111 to decimal to find the column 7

Conlusion: In row 2, column 7 appears 8. This determines the output; 8 is binary 1000. Hence S-BOX(101110) = 1000
