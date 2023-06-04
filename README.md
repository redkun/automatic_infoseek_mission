# automatic_infoseek_mission
Infoseekミッションの自動化

## 使用方法
- pythonをインストールしてパスを通しておく。
- driverフォルダ内にCHROMEのバージョンに合ったchromedriverを[ここ](https://chromedriver.chromium.org/downloads)からダウンロードし入れる。
- settings.jsonに楽天のユーザIDとパスワードを記入する
 
## 実行
- python infoseek.py 引数なし:(開始する記事:1 記事の数:10 カテゴリ:ライフ)
- python infoseek.py [開始する記事(1-20)] [終了する記事(1-20)] [カテゴリ( 総合 芸能 社会 スポーツ 経済 国際 IT ライフ)]
- python infoseek.py -h or --help:(ヘルプ)


