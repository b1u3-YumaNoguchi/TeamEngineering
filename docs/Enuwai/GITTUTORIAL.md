# git のチュートリアル


## gitとは
バージョン管理システム。使用するとファイルの修正や、変更前の状態に戻るようなことが楽になる。

## gitとgithubの関係について
githubはgitのホスティングサービスで、 他にも、gitLab、bitbucketなどのような同様のサービスがある。自前のサーバーを持てば、githubのようなサービスはできる。あくまで、githubは自分のPCだけではなく、インターネット上に、保存するためのものであるとも言える。

## よく使う git コマンド集
ストーリーで。

```
[b1u3@b1u3MacBookPro] ~
% mkdir git_test
[b1u3@b1u3MacBookPro] ~
% cd git_test
[b1u3@b1u3MacBookPro] ~/git_test
% ls
[b1u3@b1u3MacBookPro] ~/git_test
% git init .
Initialized empty Git repository in /Users/b1u3/git_test/.git/
[b1u3@b1u3MacBookPro] ~/git_test
% ls -a                                                                               (git)-[master]
./         ../        .git/      test.txt   test2.txt
```

ローカルリポジトリ:git_testが初期化される。記録は.gitディレクトリに保存される。ここまではgit cloneした場合はいらなくなる。

```
[b1u3@b1u3MacBookPro] ~/git_test
% touch test.txt                                                                      (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
% ls                                                                                  (git)-[master]
test.txt
[b1u3@b1u3MacBookPro] ~/git_test
% touch test2.txt                                                                     (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
% ls                                                                                  (git)-[master]
test.txt   test2.txt
[b1u3@b1u3MacBookPro] ~/git_test
% git add test.txt                                                                    (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
% git status                                                                          (git)-[master]
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   test.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	test2.txt
```

git add で変更を記録したいものを追加する。git status で追加したやつとかしてないやつが見れる。
test2.txtは追加してないのでUntrackedになっている。

```
[b1u3@b1u3MacBookPro] ~/git_test
% git commit -m 'test.txtだけを追加した'                                              (git)-[master]
[master (root-commit) 2458b89] test.txtだけを追加した
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.txt
[b1u3@b1u3MacBookPro] ~/git_test
% git log                                                                             (git)-[master]
commit 2458b89fd0cf338f0f86a7af946ed13354e905f7
Author: b1u3 <bp16071@shibaura-it.ac.jp>
Date:   Thu Oct 25 04:05:29 2018 +0900

    test.txtだけを追加した
```

git commit をするとその時点での状態が、記録される。git log でコミット履歴が見れる。

```
[b1u3@b1u3MacBookPro] ~/git_test
% git status                                                                          (git)-[master]
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	test2.txt

nothing added to commit but untracked files present (use "git add" to track)
[b1u3@b1u3MacBookPro] ~/git_test
% cat >> test.txt                                                                     (git)-[master]
abcdefgh^D
[b1u3@b1u3MacBookPro] ~/git_test
% git status                                                                          (git)-[master]
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   test.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	test2.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

直後にステータスを見ると追ってないtest2.txtだけが見れる。そのあと、test.txtを編集すると、modifiedのところにtest.txtがでる。ただし、この状態ではtest.txtは追ってないことになっている。なので、この後addしてcommitすると記録が保存される。

```
[b1u3@b1u3MacBookPro] ~/git_test
% git add test.txt                                                                    (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
% git commit -m 'このコミットでは文字列を追加したことが保存される'                    (git)-[master]
[master 598cf92] このコミットでは文字列を追加したことが保存される
 1 file changed, 1 insertion(+)
[b1u3@b1u3MacBookPro] ~/git_test
% git log                                                                             (git)-[master]
commit 598cf921fceb4ecf26fc7a049bb90dcb2b87791b
Author: b1u3 <bp16071@shibaura-it.ac.jp>
Date:   Thu Oct 25 04:14:03 2018 +0900

    このコミットでは文字列を追加したことが保存される

commit 2458b89fd0cf338f0f86a7af946ed13354e905f7
Author: b1u3 <bp16071@shibaura-it.ac.jp>
Date:   Thu Oct 25 04:05:29 2018 +0900

    test.txtだけを追加した
```

logでは 2 つ分のコミットが出ている。ここで、文字列を追加する必要がなかったなと思ったとき、つまり、過去のコミットした時点にファイルを戻したいときは、以下のコマンドを実行する。

```
% git reset --hard 2458b89fd0cf338f0f86a7af946ed13354e905f7                           (git)-[master]
HEAD is now at 2458b89 test.txtだけを追加した
```

hardオプションだとファイルを書き戻してくれる。hardをしないと、commit記録だけがその状態に戻り、ファイルは戻らない。確認。

```
[b1u3@b1u3MacBookPro] ~/git_test
% cat test.txt                                                                        (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
%
```

ここまで、ブランチに触れていないので、masterブランチと呼ばれる"流れ"でやっていた。

```
[b1u3@b1u3MacBookPro] ~/git_test
% git branch -a                                                                       (git)-[master]
* master
[b1u3@b1u3MacBookPro] ~/git_test
% git checkout -b new_branch                                                          (git)-[master]
Switched to a new branch 'new_branch'
[b1u3@b1u3MacBookPro] ~/git_test
% git branch -a                                                                   (git)-[new_branch]
  master
* new_branch
[b1u3@b1u3MacBookPro] ~/git_test
% git checkout master                                                             (git)-[new_branch]
Switched to branch 'master'
[b1u3@b1u3MacBookPro] ~/git_test
% git branch -a                                                                       (git)-[master]
* master
  new_branch
[b1u3@b1u3MacBookPro] ~/git_test
% git checkout new_branch                                                             (git)-[master]
Switched to branch 'new_branch'
```

ブランチを作るなどしている。切り替えなど。ブランチを作ると、別のブランチに影響を及ぼすことなく、編集が可能になる。

```
[b1u3@b1u3MacBookPro] ~/git_test
% cat >> test.txt                                                                 (git)-[new_branch]
new_branchで編集
[b1u3@b1u3MacBookPro] ~/git_test
% git add test.txt                                                                (git)-[new_branch]
[b1u3@b1u3MacBookPro] ~/git_test
% git commit -m 'new_branchでの編集'                                              (git)-[new_branch]
[new_branch 5d6d477] new_branchでの編集
 1 file changed, 1 insertion(+)
[b1u3@b1u3MacBookPro] ~/git_test
% git checkout master                                                             (git)-[new_branch]
Switched to branch 'master'
[b1u3@b1u3MacBookPro] ~/git_test
% git cat test.txt  <= ミス                                                                  (git)-[master]
git: 'cat' is not a git command. See 'git --help'.

Did you mean one of these?
	clean
	mktag
	stage
	stash
	tag
	var
[b1u3@b1u3MacBookPro] ~/git_test
% cat test.txt                                                                        (git)-[master]
[b1u3@b1u3MacBookPro] ~/git_test
%
```

masterブランチはmasterブランチで編集可能になる。branchは"流れ"が枝分かれしているイメージ。
ここまでは全てローカルのPCで行われたことであって、リモートと同期しなければならない。これらをやるのがpush、pullになる。リモートはgithubが関わってくるのでまた別記事で。







