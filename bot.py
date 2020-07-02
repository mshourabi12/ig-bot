from selenium import webdriver

import os
import time


class InstagramBot:

		def __init__(self, username, password):
			'''
				ARGS:
					username:str: for Instagram username
					password:str: for Instagarm password

				Attributes:
					driver:Selenium:webdriver.Firefox: The Firefox driver to luanch in and to automate browser actions

			'''
			self.username = username
			self.password = password

			self.message = "I am Javvad's robot. He asked me to inform you how much he loves you..."

			self.driver = webdriver.Firefox()

			self.base_url = 'https://www.instagram.com'

			self.login()


		def login(self):
			self.driver.get('{}'.format(self.base_url))

			self.driver.find_element_by_name('username').send_keys(self.username)
			self.driver.find_element_by_name('password').send_keys(self.password)		
			self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()

		def nav_user(self, user):
			self.driver.get('{}/{}/'.format(self.base_url, user))
		

		def follow_user(self, user):
			self.nav_user(user)
			follow_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
			follow_button.click()

		def goto_javal_group_direct(self, user):
			self.nav_user(user)
			time.sleep(3)
			direct_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
			direct_button.click()

			time.sleep(3)
			not_now_button = self.driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()

			time.sleep(3)
			javvad_start_messaging_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[1]/div/div/div/div').click()
			# javal_start_messaging_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[3]/a/div/div[2]/div[1]/div/div/div/div').click()
			i = 1
			while 1:
				time.sleep(1)
				text_entering_area = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(self.message)
				send_message_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
				text_entering_area = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("for " + str(i) + " times...")
				send_message_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
				i = i + 1




#f3e7bf07625546 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)  javval css selector

#f26e865fa6def56 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)   javvad css selector





if __name__ == '__main__':
	with open('userpass.txt', 'r') as f:
		username = f.readline()
		password = f.readline()
	print("\nLogging in with username: " + username)
	print("and password: " + password[0] + "*****" + password[-2] + '\n')

	ig_bot = InstagramBot(username, password)

	time.sleep(5)
	# ig_bot.nav_user('javal_group')
	ig_bot.goto_javal_group_direct('javal_group')

	
