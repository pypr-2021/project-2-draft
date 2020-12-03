import pandas as pd
from collections import Counter


#读取工作簿和工作簿中的工作表


# pd.read_csv() 浏览Excel表
data=pd.read_csv('dft_rawcount_region_id_3.csv')

key=data.keys()

# Which local authorities manage the most number of different roads (not links)?
#获取列名为count_point_id这一列的内容, 变成 list
local_authority_name = data['local_authority_name'].tolist()
# paixun
local_authority_name.sort()

# most_common(n) 按照counter的计数，按照降序，返回前n项组成的list; n忽略时返回全部
counter = Counter(local_authority_name).most_common(1) # most number
print(counter)
