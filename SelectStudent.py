import pandas as pd
def excel_reply(name):
    """关键字回复"""
    df = pd.read_excel('static/candidates2024.xlsx')
    df = df.applymap(lambda x: str(x).strip())
    # print(df)
    # print(df["候选人姓名"].values)

    # df.set_index("候选人姓名")
    df_data = df[['候选人姓名', '简历筛选状态']]
    # 判断名字是否在内推的名单中
    if name in df["候选人姓名"].values:
        print("查找的候选人存在")
        # 通过名字查询候选人信息
        candidates = df[df_data["候选人姓名"] == name]
        print("简历筛选状态=",candidates['简历筛选状态'].values)
        if candidates['简历筛选状态'].values=="未发送":
            msg = name + "您好，您当前在航旅纵横校招内推的进度为待hr筛选，请耐心等待！"
            return msg
        if candidates['简历筛选状态'].values == "未通过":
            msg = name + "您好，您当前在航旅纵横校招内推的进度为未通过简历筛选，后续依然有招聘机会，期待您的继续关注！"
            return msg
        if candidates['简历筛选状态'].values == "通过" or candidates['简历筛选状态'].values =="已筛选，待定":
            msg = name + "您好，您当前在航旅纵横校招内推的进度为通过简历筛选，请等待后续的流程通知！"
            return msg
        if candidates['简历筛选状态'].values == "已发送，待筛选":
            msg = name + "您好，您当前在航旅纵横校招内推的进度为正在业务部门进行筛选，请耐心等待！"
            return msg
        else:
            msg = "您查找的候选人" + name + "不存在，请确认" + name + "是否内推成功。\nPS:李梨同学目前只支持通过姓名查询哦！"
            return msg
    else:
        msg = "您查找的候选人"+name+"不存在，请确认"+name+"是否内推成功。\nPS:李梨同学目前只支持通过姓名查询哦！"
        return msg

#
# if __name__ == '__main__':
#     excel_reply("石楠")
