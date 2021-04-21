import pandas as pd
from collections import Counter

# 이전에 생성해둔 submission용 csv 파일들을 가져온다
output1 = pd.read_csv("./output1.csv")
output2 = pd.read_csv("./output2.csv")
output3 = pd.read_csv("./output3.csv")
output4 = pd.read_csv("./output4.csv")
output5 = pd.read_csv("./output5.csv")

submission = pd.read_csv('./info.csv') # 앙상블 결과를 저장할 csv 파일
all_ans = []

for i in range(len(output1)):
    outputs = [output1["ans"][i], output2["ans"][i], output3["ans"][i], output4["ans"][i], output5["ans"][i]]
    ensemble_ans = Counter(outputs).most_common(1)
    all_ans.append(ensemble_ans[0][0])

submission["ans"] = all_ans
submission.to_csv("./submission.csv")