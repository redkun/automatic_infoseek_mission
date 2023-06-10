import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import sys, pickle, os, json
import urlOpen
import subprocess
from subprocess import PIPE


def main():
    # 設定ファイル読み込み
    json_file = open("settings.json", "r", encoding="utf-8_sig")
    conf = json.load(json_file)

    # 引数取得処理
    article_conf = argument()

    # サイトを開く
    driver = urlOpen.url_open(conf)
    wait = WebDriverWait(driver=driver, timeout=conf["TIMEOUT"])  # タイムアウト時間の設定
    wait_article = WebDriverWait(driver=driver, timeout=2)  # タイムアウト時間の設定

    # クッキーファイルの有無
    if os.path.exists(conf["COOKIES_FILE"]):
        cookies = pickle.load(open(conf["COOKIES_FILE"], "rb"))  # クッキーを読み込む
        for c in cookies:  # クッキーを設定する
            driver.add_cookie(c)
    else:
        # ログイン処理
        subprocess.run(["python", "infoseekLogin.py"], stdout=PIPE, stderr=PIPE)

    # 一覧へ遷移
    wait.until(EC.presence_of_all_elements_located)
    wait.until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="ranking-category-all"]/div[2]/a')
        )
    )

    # 一覧へ押下
    driver.find_element(By.XPATH, '//*[@id="ranking-category-all"]/div[2]/a').click()

    # トピック選択
    wait.until(
        EC.visibility_of_all_elements_located((By.LINK_TEXT, article_conf["category"]))
    )
    driver.find_element(By.LINK_TEXT, article_conf["category"]).click()

    # URLの一覧を取得
    URLs = []
    for articleNo in range(
        article_conf["start_article"],
        article_conf["end_article"],
    ):
        wait.until(EC.presence_of_all_elements_located)
        URL = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[3]/div/section/section/div/ul/li["
            + str(articleNo)
            + "]/div[2]/a",
        ).get_attribute("href")
        URLs.append(URL)

    # X番目の記事を開く
    articleNo = article_conf["start_article"]
    for u in URLs:
        driver.get(u)
        print("「{}」カテゴリの {}番目の記事".format(article_conf["category"], articleNo))
        articleNo += 1

        # 一番下までスクロール
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

        try:
            wait_article.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, '//*[@id="mission-window-during"]/div[1]/p[1]')
                )
            )
            isNext = False
            while not isNext:
                wait.until(EC.presence_of_all_elements_located)

                # ポイント獲得ページへ
                getPoint = driver.find_element(
                    By.XPATH,
                    '//*[@id="mission-completed"]/a',
                )
                # 次の記事を探す
                nextArticle = driver.find_element(
                    By.XPATH, '//*[@id="mission-next-article-button"]/a/span'
                )

                if getPoint.is_displayed():
                    getPoint.click()  # ポイント獲得ページへ遷移
                    time.sleep(3)

                    # バツボタン画像
                    getBatsuButton = driver.find_element(
                        By.XPATH,
                        '//*[@id="gn_interstitial_close_icon"]',
                    )
                    if getBatsuButton.is_displayed():
                        getBatsuButton.click()

                        # ポイント獲得
                        getPointGetButton = driver.find_element(
                            By.XPATH,
                            "/html/body/div[1]/div/div[3]/div/section/section[1]/div[2]/ul/li/div[2]/a",
                        )
                        if getPointGetButton.is_displayed():
                            getPointGetButton.click()

                    print("ポイントを確認してください。")
                    os.system("PAUSE")
                    exit()
                elif nextArticle.is_displayed():
                    isNext = nextArticle.is_displayed()

        except TimeoutException as te:
            print("押下済み")

    driver.close()


def argument():
    ret = {}
    ret["start_article"] = 1
    ret["end_article"] = 11
    ret["category"] = "ライフ"  # カテゴリ 総合 芸能 社会 スポーツ 経済 国際 IT ライフ
    args = sys.argv
    if len(args) == 2:
        if args[1] == "--help" or args[1] == "-h":
            print(
                "python infoseek.py [開始する記事(1-20)] [終了する記事(1-20)] [カテゴリ( 総合 芸能 社会 スポーツ 経済 国際 IT ライフ)]\npython infoseek.py 引数なし(開始する記事:1 記事の数:20 カテゴリ:ライフ)"
            )
            exit()
    elif len(args) == 4:
        ret["start_article"] = int(args[1])  # 開始する記事
        ret["end_article"] = int(args[2]) + 1  # 記事の数
        ret["category"] = args[3]  # カテゴリ
        if ret["start_article"] >= ret["end_article"]:
            print("記事の開始終了を確認してください")
            exit()
    return ret


if __name__ == "__main__":
    main()
