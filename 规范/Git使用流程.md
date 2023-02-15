##### Git使用规范

> Github仓库:*git@github.com:caro1xxx/BaoPing-Inc..git*

###### 分支命名

* 主分支:main
* 开发分支:develop
* 功能分支:feature-[branchName]
* 分支发布:release-version
* 修复分支:bugfix-version

###### 详细分支操作

*未经单元测试的代码禁止push*

```bash
1.拉取
	git clone git@github.com:caro1xxx/BaoPing-Inc..git
	git checkout -b develop origin/develop
	
2.创建本地分支
	git checkout -b feature-[name] develop
	(禁止在本地分支push)
	
3.待开发完毕后,将本地功能分支和develop分支合并
	git checkout develop
	git pull origin develop
	git merge feature-[name] 
	git push 

视情况可以删除本地功能分支
	git branch -d feature-[name]
```

在不影响远程代码的情况下可以自由操作