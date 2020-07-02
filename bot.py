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
			follow_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')

			follow_button.click()

		def follow_user(self, user):
			self.nav_user(user)
	
if __name__ == '__main__':
	with open('userpass.txt', 'r') as f:
		username = f.readline()
		password = f.readline()
	print("\nLogging in with username: " + username)
	print("and password: " + password[0] + "*****" + password[-2] + '\n')
	ig_bot = InstagramBot(username, password)

	time.sleep(5)
	ig_bot.nav_user('javal_group')

	
