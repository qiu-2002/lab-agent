# lab-agent

实验室管理平台，前端基于 **Vue 3 + Vite**，后端基于 **FastAPI + SQLAlchemy + MySQL**。

## 项目结构

```text
lab-agent/
├── backend/                 # 后端服务
│   ├── app/
│   │   ├── config.py        # 配置加载（读取 backend/.env）
│   │   ├── database.py      # SQLAlchemy 引擎、会话与 Base 模型
│   │   ├── demo.py          # 依赖注入 / 会话生命周期示例
│   │   └── main.py          # FastAPI 应用入口
│   └── requirements.txt
├── frontend/                # 前端应用
│   ├── src/
│   │   ├── layout/          # 管理端布局
│   │   ├── views/           # Login / Register / home / lab 页面
│   │   ├── router/          # 路由配置
│   │   └── assets/          # 样式与图片
│   └── package.json
└── .gitignore
```

## 环境要求

| 组件 | 版本 |
| --- | --- |
| Node.js | >= 22.18（或 >= 24.12） |
| Python | >= 3.10 |
| MySQL | 8.x |

## 后端启动

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env    # 然后填入自己的数据库连接
uvicorn app.main:app --reload
```

启动后接口文档地址：<http://127.0.0.1:8000/docs>

## 前端启动

```bash
cd frontend
npm install
npm run dev
```

默认访问 <http://localhost:5173>，根路径会重定向到 `/manager/home`；登录页 `/login`，注册页 `/register`。

生产构建：

```bash
npm run build
```

## 配置说明

数据库连接统一通过 `backend/.env` 中的 `DATABASE_URL` 配置，格式为：

```text
mysql+pymysql://用户名:密码@主机:3306/lab_agent?charset=utf8mb4
```

`backend/.env` 已被 `.gitignore` 忽略，**不要提交真实密码**；新增配置项时请同步更新 `backend/.env.example`。
