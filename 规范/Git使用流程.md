##### Git使用规范

> Github仓库:*git@github.com:caro1xxx/BaoPing-Inc..git*

**禁止push到主分支**

> 请clone **develop**分支
>
> git clone -b develop git@github.com:caro1xxx/BaoPing-Inc..git

##### 分支命名

* 主分支:main
* 开发分支:develop
* 功能分支:feature-[branchName] (**仅出现在本地**)
* 分支发布:release-version

##### 详细分支操作

1. 克隆develop分支

```shell
git clone -b develop git@github.com:caro1xxx/BaoPing-Inc..git
```

2. 新建分支

```shell
# 创建并进入feature-xxx分支
git checkout -b feature-xxx
```

3. 待开发完毕后提交分支

```shell
#回到develop分支
git checekout main
```

4. 保存本地代码

```shell
git add .
git commit -m 'message'
#注意这里没有push
```

5. 获取最新develop(保持同步)

```shell
git pull origin develop
```

6. 将第4不保存的代码,push到develop

```shell
#当前分支develop
git push origin develop
```

7. 删除本地功能分支(可选)

```shell
# 删除本地特性分支
git branch -d feature-xxx
```

