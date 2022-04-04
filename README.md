# sam-hello-who

AWS SAMの Lambda + API Gatwayで
引数をGETメソッドとPOSTメソッドで渡すサンプル。

Python 3.9

中身は"Hello {who}\n"を出すだけです。
(whoが引数)


# デプロイ

```sh
sam build
sam deploy --guided  # --guidedは最初の1回
```

`sam deploy --guided` は

```
HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
```

以外はデフォルトでいいです。

デプロイが終わったら
```sh
./export1.sh  # 実行にはjqとyqとaws cliが必要
```

で、APIのURLを `.export.sh` に書き出してください。


# テストの実行

```sh
./get_test.sh  # GETメソッドでテスト
./post_test.sh # POSTメソッドでテスト
```


# スタックの削除

```sh
sam delete --no-prompts
```
で消えます。


# メモ

`post_test.sh`にかかれていますが、
APIゲートウエイにbody送るのには
`application/json`にする必要があります。
で、bodyはJSONで。

JSONでない場合event.bodyが空になります(NilやらNONEやら)。

API Gatewayのコンソールからテストするときも、
POSTの方は「リクエスト本文」のところにJSONを書くこと。
