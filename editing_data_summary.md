| dictionary  | files | words | sentences |sentences len_1|sentences len_2|
| :---------: | :---: | :---: | :-------: | :-------: | :-------: |
| collins_8th | 366   | 34646 | 620725    |a|a|
|collins_online|397|39675|372314|907392-a|928123-a|
|cambrige_4th（error）|677|64640|271522|208377|x|
|cambrige_3th|1|49405|350483|302716|347505|
|Longman|528| 52749 | 390678 |348281|302003|

**trn_file**

- collins_8th

- collins_online

**val_file**

- Longman

**tes_file**

- cambrige_3th



**len_1**

- 通过split(' ')后删除长度>1的单词

**len_2**

- 在筛选句子对时重写了每个dict的筛选代码， 通过split(' ')后删除长度>1的单词， 删除 (*-crazed* ，*'d*)不以字符开头的单词

len_3

- 删除带（...）的句子，防止主谓宾成分不全造成的影响

len_3.2

- 在len_3基础上，删除collins不同字典之间相同的句子对，用cosine_similarity>=0.8

len_4

- 在len_3的基础上，将trn和val进行组合打乱，拆分成1:9

len_4.2

- 在len_4基础上，删除collins不同字典之间相同的句子对，用cosine_similarity>=0.8

len_5

- trn字典增加oxford_9th

len_6

- trn字典增加Merriam_2th
