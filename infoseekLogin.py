from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pickle, os, json
import urlOpen

# 設定ファイル読み込み
json_file = open("settings.json", "r", encoding="utf-8_sig")
conf = json.load(json_file)

if os.path.exists(conf["COOKIES_FILE"]):
    choice = input("クッキーは設定済みです、更新しますか [y/N]: ").lower()
    if choice in ["y", "ye", "yes"]:
        pass
    else:
        exit()

# サイトを開く
driver = urlOpen.url_open(conf)
wait = WebDriverWait(driver=driver, timeout=conf["TIMEOUT"])  # タイムアウト時間の設定

# ログイン
if driver.find_element(By.XPATH, '//*[@id="loginBox"]/p[1]/a'):
    print("Press any key to continue...")
    input()  # 任意のキーが押されるまで待機
    driver.find_elements(By.XPATH, '//*[@id="loginBox"]/p[1]/a')[0].click()  # ログインボタン押下
    print("Press any key to continue...")
    input()  # 任意のキーが押されるまで待機   
    wait.until(EC.visibility_of_all_elements_located((By.ID, "user_id")))
    texts = driver.find_element(By.ID, "user_id")
    texts.send_keys(conf["USER_ID"])
    # 次へ押下
    driver.find_elements(By.CLASS_NAME, "box-0px0px0px765px252-146-146-255-fs")[
        0
    ].click()
    wait.until(EC.visibility_of_all_elements_located((By.ID, "password_current")))
    texts = driver.find_element(By.ID, "password_current")
    texts.send_keys(conf["PASSWORD"])
    # ログイン押下
    driver.find_elements(By.CLASS_NAME, "box-0px0px0px765px252-146-146-255-fs")[
        2
    ].click()
    # クッキーを保存する
    wait.until(EC.presence_of_all_elements_located)
    wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="userBox"]/div/p'))
    )
    cookies = driver.get_cookies()
    pickle.dump(cookies, open(conf["COOKIES_FILE"], "wb"))
    print("クッキーを保存しました")
    driver.close()
