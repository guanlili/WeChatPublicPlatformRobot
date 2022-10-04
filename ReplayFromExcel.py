import ReadAndWriteExcel

def excel_reply(msg):
    """关键字回复"""
    keyword_read = ReadAndWriteExcel.OpenExcel(file_name="static/shcool_stundent.xlsx", sheet_id=0)
    print("keyword_read",keyword_read)
    for i in range(0,keyword_read.get_lines()):
        if msg in keyword_read.get_value(i,0):
            return keyword_read.get_value(i,1)
    if '你叫啥' in msg or '你叫啥名字' in msg:
        return '沃德天·维森莫·拉莫帅·帅德布耀'
    elif '我爱你' in msg:
        return  "我也爱你"
    elif '早安'in msg:
        return "早安啊，朋友"
    else:
        return '我没有听懂你在说什么，\n或许我休息一天，\n明天就能智商上线了~'
    pass