#(1) 平均分
score = {"Tom":75, "Jack":98, "Lucy":86, "Andy":92}
score_list = list(score.values())
x = len(score_list)
i = 0
sum = 0
for i in range(0, x):
    sum = sum + score_list[i]
    i = i+1
average = sum / x
print("The average is " + str(average) + ".")

#(2) 最高分的同学+分数
rank = zip(score.values(), score.keys()) #把dict转化为tuple,
sorted_rank = sorted(rank)
print("Highest: " + str(sorted_rank[x-1]))     #输出排序完之后list的最大值

#(3) 90+的同学+分数




