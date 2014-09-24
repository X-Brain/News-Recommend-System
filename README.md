News-Recommend-System
=========================================================================================
##Global_param中设置参数说明：
      number_jieba：控制提取关键词的数量
      number_day:从第一天开始，要预测的天数
      hot_rate:预测集预测的新闻热度，数值越大热度越高

##代码流程：

#####首先我们从main()看起。

#####1.首先Get_day_data.TransforData(i)函数，找到最后一次浏览的是第i天的新闻的用户行为，存放在test/train_lastday_set目录下。

#####2.Get_day_data.TransforDataset(i)函数，区分每一天的新闻，存放在test/train_date_set1目录下

#####3.Get_keywords.Get_keywords(i)函数，调用jieba库，挑出每一天最火的分层，存放在test/key_words下

#####4.Get_keynews.Get_keynews(i)函数，通过每一个用户最后一次浏览的新闻，比对看有没有出现当天的热门keywords。如果出现，就推荐当天包含这个keywords的其它新闻。循环Global_param.number_day天，生成test/result.txt文件.  
   
#####5. Delete_Repeat.Delete_Repeat()函数，去除result中的重复项，生成test/result_no_repeat.txt
   
#####6.Get_hot_result.get_hot_result(Global_param.hot_rate)函数，因为上面生成result_no_repeat函数可能出现，每个用户推荐过多的情况，影响准确率。所以用这个函数控制数量，每个用户只推荐新闻热度相对高的候选项。最终结果集test/result_no_repeat_hot.txt


##详情可见：http://blog.csdn.net/buptgshengod
