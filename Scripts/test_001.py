import allure
from selenium import webdriver


class Test001:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    @allure.step("第二步")
    def abc(self):
        print("1234")

    @allure.step("第一步")
    def test001(self):
        self.abc()
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(),"新浪",allure.attachment_type.PNG)
        print("\n hello python")
