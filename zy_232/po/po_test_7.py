from selenium.webdriver.common.by import By
from base.base_page import Base
class Po_7(Base):
    # 页面属性
    keqing1 = (By.ID, "1")
    keqing2 = (By.XPATH, '//iframe[@scrolling="yes"]')
    keqing3 = (By.ID, 'ext-gen1150')
    keqing4 = (By.XPATH, "//*[text()='out_net7']")
    keqing5 = (By.ID, "ext-gen1165")
    keqing6 = (By.XPATH, '//*[text()="IPv4"]')
    keqing7 = (By.ID, "textfield-1060-inputEl")
    keqing8 = (By.ID, 'ext-gen1174')
    keqing9 = (By.XPATH, '//*[text()="1G"]')
    keqing10 = (By.XPATH, '//*[@id="button-1074-btnIconEl"]')
    keqing11 = (By.XPATH, '//iframe[@scrolling="yes"]')
    keqing12 = r"G:\untitled\zy_232\picture\out_net7_1.png"
    keqing13 = (By.XPATH, '//*[text()="帧速率/数据速率"]')
    keqing14 = r"G:\untitled\zy_232\picture\out_net7_2.png"
    keqing15 = (By.XPATH, '//*[text()="帧速率/数据速率"]')
    # 页面方法
    def caozuo7(self, value1, time1, time2, zhi):
        self.click(Po_7.keqing1)
        self.iframe(Po_7.keqing2)
        self.click(Po_7.keqing3)
        self.click(Po_7.keqing4)
        self.click(Po_7.keqing5)
        self.click(Po_7.keqing6)
        self.send_keys(Po_7.keqing7, value1)
        self.click(Po_7.keqing8)
        self.click(Po_7.keqing9)
        self.click(Po_7.keqing10)
        self.out_iframe()
        self.iframe(Po_7.keqing11)
        self.sleep(time1)
        self.jietu(Po_7.keqing12)
        self.click(Po_7.keqing13)
        self.jietu(Po_7.keqing14)
        self.sleep(time2)
        self.alert()
        self.assert1(Po_7.keqing15, zhi)
        self.out_iframe()
        self.driver.close()