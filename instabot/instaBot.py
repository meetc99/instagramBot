import sys
import time
from selenium import webdriver
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.gui()

    def gui(self):

        self.hashtagLabel = QtWidgets.QLabel(self)
        self.hashtagLabel.setText("Hashtag")
        self.hashtagLabel.setFixedSize(50, 20)
        self.hashtagLabel.move(5, 10)

        self.hashtag1 = QtWidgets.QLineEdit(self)
        self.hashtag1.setFixedSize(150, 20)
        self.hashtag1.move(50, 10)

        self.likeButton = QtWidgets.QPushButton(self)
        self.likeButton.setText('like')
        self.likeButton.setFixedSize(150, 20)
        self.likeButton.move(50, 50)

        self.likeButton.clicked.connect(self.like)
        self.show()

    def like(self):

        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--ingnore-certificate-errors')
        options.add_argument('--incognito')

        chromeExe = 'C:/selenium/chromedriver.exe'

        driver = webdriver.Chrome(executable_path=chromeExe, options=options)
        username = 'username'
        password = 'password'

        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        textBox1 = driver.find_element_by_xpath('//input[@name="username"]')
        textBox1.clear()
        textBox1.send_keys(username)

        textBox2 = driver.find_element_by_xpath('//input[@name="password"]')
        textBox2.clear()
        textBox2.send_keys(password)

        loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        loginButton.click()
        time.sleep(5)

        messageButton = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]')
        messageButton.click()
        time.sleep(5)

        hashtag1Giris = self.hashtag1.text()
        textBox3 = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        textBox3.send_keys(hashtag1Giris)
        time.sleep(10)

        tagButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[1]/span')
        tagButton.click()
        time.sleep(10)


        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)
        hrefs = driver.find_elements_by_tag_name('a')
        photo_hrefs = [elem.get_attribute('href') for elem in hrefs]
        photo_hrefs = [href for href in photo_hrefs]
        #print('photos:' + str(len(photo_hrefs)))

        for photo_href in photo_hrefs:
            driver.get(photo_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                likeButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button')
                likeButton.click()
                time.sleep(5)
            except Exception as e:
                time.sleep(2)
        driver.close()
        driver.quit()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.setFixedSize(300, 300)
    sys.exit(app.exec_())
