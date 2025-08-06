from selenium.webdriver.common.by import By


class ServerAuthEle():

    server_auth_button = (By.XPATH, "//span[text()='服务授权']")
    gene_server_qcode = (By.XPATH, "//span[text()='产生服务授权码']")
    now_stop = (By.XPATH, "//span[text()='立即停用']")
    stop_server_confirm = (By.XPATH, "//span[contains(text(),'确定')]")
    select_days = (By.XPATH, "//p[text()='有效时长']/following-sibling::nz-select[1]")
    selected_days = (By.XPATH, "//div[text()='一个月']")
    gene_code = (By.XPATH, "//span[text()='产生服务授权码']")
    assert_server_qcode = (By.XPATH, "//span[text()='授权码产生成功']")
    #点击body

    proxy_auth = (By.XPATH, "//span[text()='Athena代理授权']")
    long_time = (By.XPATH, "//a[text()='展延']")
    end_time = (By.XPATH, "(//input[@placeholder='请选择'])[2]")
    agree_agreement = (By.XPATH, "//span[text()='已阅读并同意']")
    gene_code_button = (By.XPATH, "//span[text()='产生代理授权码']")
    assert_back_gene = (By.XPATH, "//span[text()='代理授权码']")


