# sam-hello-who

AWS SAMの動作チェック用のミニマムパッケージ。
Python 3.8

中身は"Hello world"を出すだけです。


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


## AWS Cloud Shellからのデプロイ

`sam build` するのに python 3.8 が要るので、
```sh
sudo amazon-linux-extras install -y python3.8
```

で、python 3.8をインストールしてください。


または
「sam buildずみのプロジェクトフォルダーをコピーする」
などで対処してください。



# スタックの削除

```sh
sam delete
```
で消えます。
