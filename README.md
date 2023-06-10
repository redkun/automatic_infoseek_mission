# automatic_infoseek_mission
Infoseekミッションの自動化

## 使用方法
- pythonをインストールしてパスを通しておく。
- Seleniumをインストールする。
- driverフォルダ内にCHROMEのバージョンに合ったchromedriverを[ここ](https://chromedriver.chromium.org/downloads)からダウンロードし入れる。
- settings_sample.jsonをsettings.jsonに変更し楽天のユーザIDとパスワードを記入する
 
## 実行
- python infoseek.py 引数なし:(開始する記事:1 記事の数:10 カテゴリ:ライフ)
- python infoseek.py [開始する記事(1-20)] [終了する記事(1-20)] [カテゴリ( 総合 芸能 社会 スポーツ 経済 国際 IT ライフ)]
- python infoseek.py -h or --help:(ヘルプ)

## サイト
- [Infoseekミッションの自動化](https://diy-r.hatenablog.jp/entry/2023/06/04/Infoseek%E3%83%9F%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E8%87%AA%E5%8B%95%E5%8C%96)


