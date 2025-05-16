# PyGit - 注释梳理版本

PyGit 是一个用 Python 实现的精简版 Git 版本控制系统。这个项目旨在展示 Git 的核心概念和基本工作原理，通过较少的代码实现了 Git 的基本功能。

引用自 [https://github.com/benhoyt/pygit](https://github.com/benhoyt/pygit)

详细介绍请参见：[http://benhoyt.com/writings/pygit/](http://benhoyt.com/writings/pygit/)

## 特性

支持的 git 命令:
- 初始化仓库 (init): 创建一个新的Git仓库
- 添加文件 (add): 将文件添加到索引/暂存区
- 提交更改 (commit): 将索引中的更改提交到本地仓库
- 查看状态 (status): 查看工作目录和索引之间的差异
- 查看差异 (diff): 显示工作目录和索引中文件的具体差异
- 推送更改 (push): 将本地提交推送到远程仓库
- 查看对象 (cat-file): 查看Git对象的内容和类型