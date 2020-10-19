Huffman ( [a1,f1],[a2
,f2],…,[an,fn])
if n=1 then
code[a1] ←
else
let fi,fj be the 2 smallest f’
s
Huffman ( [ai,fi+fj],[a1,f1],…,[an,fn] )
omits ai,aj
code[aj] ← code[ai] + “0”
code[ai] ← code[ai] + “1” 
