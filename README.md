## **项目结构**

```bash
├── apis/                 # API 路由模块
├── website/              # 核心功能模块
├── .env.dev              # 环境变量文件
├── .gitignore            # Git 忽略文件
├── README.md             # 项目说明文档
├── config.py             # 项目配置文件
├── requirements.txt      # 项目依赖文件
├── run_dev.py            # 项目启动文件
```

### **1. 克隆项目**

使用 Git 克隆项目到本地：

```bash
git clone https://github.com/jiujiu0/Car-api.git
cd Car-api
```

### **2. 配置虚拟环境**

创建并激活 Python 虚拟环境：

```bash
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境 (Linux/Mac)
source myenv/bin/activate

# 激活虚拟环境 (Windows)
myenv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

### **3. 启动项目**

使用以下命令启动开发环境：

```bash
python run_dev.py
```



## **项目依赖**

项目的依赖已在 `requirements.txt` 中列出，可通过以下命令查看和安装：

```bash
pip install -r requirements.txt
```

