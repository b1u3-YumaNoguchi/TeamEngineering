# Pull Request

# cloneすらしていない場合

```
%git clone https://github.com/b1u3-YumaNoguchi/TeamEngineering.git
```

# コマンドラインの場合
まず、新しいブランチを作る。hogehogeはブランチ名。

```
%git checkout -b hogehoge
```

ブランチがhogehogeになったことを確認する。ブランチ名の横に アスタリスクがついて入れば大丈夫。

```
%git branch -a
```

何か修正や、改良を加えてコミット、プッシュ。新しくファイルを追加した場合は、add忘れずに。

```
%git commit -m '改良したところなどのコメント'
%git push origin hogehoge
```

そうすると、ブラウザ上のhogehogeブランチに変更が反映される。
ブラウザ上でhogehogeブランチにして、ブランチ選択の横のnew pull requestでプルリクをする。
意味はmasterブランチに追加できる状態だからmasterブランチと統合してくれという感じ。





