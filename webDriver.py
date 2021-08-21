
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebDriver:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\dell-pc\Downloads\chromedriver_win32\chromedriver.exe")
        self.vars = {}

    def setup(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.page = self.driver.page_source

    def quit(self):
        self.driver.quit()

    def getNumArray(self):
        retList = []
        for i in range(9):
            oneList = []
            for j in range(9):
                oneList.append(0)
            retList.append(oneList)
        return retList

    def putNum(self, x, y, num):
        pass

    def finish(self):
        pass

class WebDriverSudokuCn(WebDriver):
    def __init__(self, url):
        super().__init__(url)


    def setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.page = self.driver.page_source

    def quit(self):
        self.driver.quit()

    def getNumArray(self):
        retList = []
        for i in range(9):
            oneList = []
            for j in range(9):
                oneList.append(0)
            retList.append(oneList)
        for i in range(9):
            for j in range(9):
                eleNum = self.driver.find_element(By.ID, "vc_%d_%d" %(j, i))
                text = eleNum.text
                if len(text) > 0:
                    num = int(text)
                    retList[i][j] = num
        return retList

    def putNum(self, x, y, num):
        self.driver.find_element(By.ID, "vc_%d_%d" % (y, x)).click()
        key = "%d"%(num,)
        self.driver.find_element(By.ID, "vc_%d_%d" % (y, x)).send_keys(key)

    def finish(self):
        pass


class WebDriver_puzzle_sudoku(WebDriver):
    def __init__(self, url):
        super().__init__(url)

    def putNum(self, x, y, num):
        elem = self.numArry[x][y]
        elem.click()
        self.driver.find_element(By.CSS_SELECTOR, "#buttonsRight > .button%d" %(num,)).click()


    def getNumArray(self):
        retList = super().getNumArray()
        self.numArry = super().getNumArray()

        elem = self.driver.find_element_by_class_name("sudoku-cell-back")
        numDiv = elem.find_elements_by_class_name("number")

        index = 0
        for i in range(9):
            for j in range(9):
                one = numDiv[index]
                index += 1
                if len(one.text) > 0:
                    retList[i][j] = int(one.text)

        # "//*[@id="game"]/div[1]/div[2]"
        index = 2
        for i in range(9):
            for j in range(9):
                self.numArry[i][j] = self.driver.find_element(By.XPATH, '//*[@id="game"]/div[1]/div[%d]' %(index) )
                index += 1
        return retList

    def finish(self):
        self.driver.find_element(By.ID, "btnReady").click()


def testWebDriverSudokuCn():
    wd = WebDriverSudokuCn("https://www.sudoku-cn.com/")
    wd.setup()
    retList = wd.getNumArray()
    for line in retList:
        print(line,",")
    wd.putNum(0, 0, 9)
    time.sleep(1)
    wd.finish()

def testWebDriver_puzzle_sudoku():
    wd = WebDriver_puzzle_sudoku("https://cn.puzzle-sudoku.com/")
    wd.setup()
    retList = wd.getNumArray()
    for line in retList:
        print(line,",")
    for i in range(9):
        for j in range(9):
            if retList[i][j] == 0:
                wd.putNum(i,j, 9)
    # wd.putNum(0, 0, 9)
    # wd.putNum(1, 1, 9)
    wd.finish()
    time.sleep(100)

if __name__ == '__main__':
    if True:
        testWebDriver_puzzle_sudoku()
    else:
        testWebDriverSudokuCn()