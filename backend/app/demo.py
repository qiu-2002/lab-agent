def get_db():
    print("【打开数据库会话】")
    db = "模拟db连接对象"
    try:
        yield db  # ← 把db交给外面使用，函数暂停在这里！
    finally:
        print("【关闭数据库会话】")


# 手动模拟 Depends 的行为
gen = get_db()
db_obj = next(gen)
print("接口业务逻辑，使用db：", db_obj)

# 业务结束，触发finally（模拟请求结束）
try:
    next(gen)
except StopIteration:
    pass
