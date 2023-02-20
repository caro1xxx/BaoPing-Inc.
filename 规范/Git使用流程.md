##### Git使用规范

> Github仓库:*git@github.com:caro1xxx/BaoPing-Inc..git*

**禁止push到主分支**

> 请clone **develop**分支
>
> git clone -b develop git@github.com:caro1xxx/BaoPing-Inc..git

##### 分支命名

* 主分支:main
* 开发分支:develop
* 功能分支:feature-[branchName]
* 分支发布:release-version
* 修复分支:bugfix-version

##### 详细分支操作

1. 获取develop分支最新代码

```shell
# 获取 dev 分支最新代码
git checkout dev
git pull
```

2. 新建分支

```shell
# 新建一个特性分支
git branch feature-xxx
# 切换到该特性分支，进行开发
git checkout feature-xxx
```

3. 提交分支

```shell
#在该特性分支下开发完毕后,即可提交分支
# current branch 'develop'
git add .
git commit -m 'message'
#在该分支下首次提交,需要携带origin,后续该分支下即可直接push
git push -u origin feature/xxx
```

4. 保持与develop分支同步

```shell
# 获取 dev 分支最新代码
git checkout develop
git pull

# 切换回当前开发的特性分支
git checkout feature-xxx
# 合并 dev 分支到当前分支
git merge develop
```

5. Pull Request

```shell
#在完成该功能分支,并且已经与develop主干同步后,就可以pull request请求合并

#重复步骤3,4

#前往github创建 Pull Request
```

6. 最后

```shell
#在功能分支开发完毕,并且合并后,删除该功能分支
git checkout develop

# 删除远程功能分支
git push origin -d feature-xxx

# 删除本地特性分支
git branch -d feature-xxx

#切记先删远程再删本地
```

