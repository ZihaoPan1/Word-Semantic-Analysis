## Semantic Model

### 1. 项目构想

&emsp;英文单词在不同语境下有不同的含义，在剑桥词典中，pool可以翻译**“a small area of usually still water”**, 也可以翻译成**“a number of people or a quantity of a particular thing, such as money, collected together for shared use by several people or organizations”**，错误的翻译会极大阻碍你对阅读文章的流畅度。本项目希望设计一款NLP模型，能够快速找寻正确词义。

### 2.项目进度

&emsp;项目设计在chatGPT之前，因此整体效果不如GPT，目前最终目标是通过极少的个人资源逼近GPT的效果。

&emsp;数据方面的尝试全部在*building_models/data* 文件夹中，尝试添加剑桥词典第三版，柯林斯第八版，朗文词典和牛津第八版资源，也尝试了不同的文本清洗策略比较对结果的影响程度。更加具体的细节保存在*“editing_data_summary.md”*。

&emsp;模型方面尝试全在*building_models/models* 文件夹中，包含bert-small和bert-base观察增加模型参数对整体性能的影响，也尝试了不同的比较策略，如一开始的策略是设置0/1来简单提示模型在training过程中是否匹配上正确的词义，调整后尝试0/1/2进行进一步细分匹配结果，以及通过Jaccard相似算法新增特征值来进一步提升loss数值提升准确性。

&emsp;最终结果保存在*“summary.xlsx”*，但是最后添加新token结果存在一些问题，还会进行修改。

&emsp;后续也会进一步更新尝试更新的模型框架(双塔模型等)以及新的资源填充，label标注时候的选择提升性能。
