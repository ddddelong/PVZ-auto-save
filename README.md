玩过植物大战僵尸杂交版的都知道，闪退是真折磨啊！！

这是一个简单的保存和切换植物大战僵尸杂交版存档的脚本，用于自动复制和管理游戏存档。

## 功能

- 将游戏存档从一个目录复制到另一个指定目录。
- 管理存档目录，保持目录下存档文件夹的最大数量。
- 自动检测最新的存档并进行处理。

## 配置

项目包括以下文件：

- `config.py`: 用于设置源文件夹、目标文件夹以及存档的最大数量等配置。
- `saveGame.py`: 包含复制和管理存档的功能函数。
- `switchGameSave.py`: 实现存档切换功能。

## 使用方法

1.修改 `config.py` 中的配置设置，如目标文件夹路径、源文件夹路径和最大文件夹数量。

2.运行 `switchGameSave.py` 来切换游戏存档。

bash

```bash
python ./src/switchGameSave.py  # 切换游戏存档
python  ./src/saveGame.py   # 保存游戏存档
```

3.当提示时，根据程序的引导进行操作。
