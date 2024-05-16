from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def url_open(conf):
    chrome_options = Options()  # Chromeオプションの作成
    chrome_options.add_argument("--log-level=3")  # ログレベルを設定
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    driver.set_window_position(
        conf["POSITION"][0], conf["POSITION"][1]
    )  # カレントウインドウのポジション
    driver.set_window_size(
        conf["WINDOW_SIZE"][0], conf["WINDOW_SIZE"][1]
    )  # カレントウインドウのサイズ

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "zimg.jp",
                "amazon.co.jp",
                "googlesyndication.com",
                "rakuten-static.com",
                "googlesyndication.com",
                "admatrix.jp",
                "gmossp-sp.jp",
                "adnxs-simple.com",
                "ladsp.com",
                "rakuten.co.jp",
                "*.png",
                "*.jpg",
                "*.gif",
            ]
        },
    )

    driver.get(conf["WEB_URL"])

    return driver
