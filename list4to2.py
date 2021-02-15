list = [
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"],
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"],
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"],
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"],
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"],
    ["EXP+1％","【EXP+1％】ピートフェイス","エラー","fa11k7"]
]

desired_list = [
    ["EXP+1％","fa11k7"],
    ["EXP+1％","fa11k7"],
    ["EXP+1％","fa11k7"],
    ["EXP+1％","fa11k7"],
    ["EXP+1％","fa11k7"]
]

codebook = [[item[0], item[3]] for item in list]

for each in codebook:
    print(each)
