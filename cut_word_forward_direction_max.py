
#正向最大匹配法构建分词器
def cut_word(sentence, word_dict):
    """
    正向最大匹配法
    sentence :待切分句子
    word_dict:字典
    """
    #寻找字典中最大词长度
    word_length_list = [len(word) for word in word_dict]
    max_length = max(word_length_list)
    #求出句子长度
    word_length = len(sentence)
    #创建一个列表用来存放切分结果
    cut_word_list = []
    #判断句子长度是否为0，若为0，则句子为空
    while word_length > 0:
        max_cut_length = min(max_length, word_length)
        #取前max_cut__length个字组成一个词
        subsentence = sentence[0:max_cut_length]
        while max_cut_length>0:
            #匹配字典
            if subsentence in word_dict:
                cut_word_list.append(subsentence)
                break
            elif max_cut_length==1:
                cut_word_list.append(subsentence)
                break
            else:
                #若字典没有词匹配，则剔除一个字，重新组成一个新词
                max_cut_length = max_cut_length-1
                subsentence = subsentence[0:max_cut_length]

        #剔除切分完的词
        sentence = sentence[max_cut_length:]
        #重新计算句子的长度
        word_length = word_length-max_cut_length
    return cut_word_list