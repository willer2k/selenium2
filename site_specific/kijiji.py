from ..config import *

# external
from typing import Any, Callable, List, NamedTuple, NoReturn, Union as U, Tuple

# internal
from ..browser import Browser
from ..logger import Logger

class Kijiji:

	# good format to fetch all locations
	locations_access = 'https://web.archive.org/web/20170914180512/https://www.kijiji.ca/'

	category_page = 'https://www.kijiji.ca/p-post-ad.html?categoryId={}'
	my_ads = 'https://www.kijiji.ca/m-my-ads/active/1'
	my_favourites = 'https://www.kijiji.ca/m-watch-list.html'
	my_messages = 'https://www.kijiji.ca/m-msg-my-messages/'
	my_orders = 'https://www.kijiji.ca/t-my-orders.html'
	my_profile = 'https://www.kijiji.ca/o-profile/1017207992/1'
	my_settings = 'https://www.kijiji.ca/t-settings.html'
	sign_in_page = 'https://www.kijiji.ca/t-login.html'

	def __init__(self, driver: U[Browser,str], desired_capabilities: dict = None,
	             profile: object = None, options: object = None):
		self.log = Logger().log
		if type(driver) is Browser:
			self.driver = driver
		elif type(driver) is str:
			self.driver = Browser(driver, desired_capabilities, profile, options)
		else:
			raise ValueError('Expected for driver to be of type "string" or '
			                 '"Browser", but received a type of "%s" instead'
			                 % (type(driver),))

	def active_posts(self)->int:
		pass

	def get_new_messages(self)->List[str]:
		pass

	def is_signed_in(self)->bool:
		"""
		Will look for notifications icon (the bell) which is available only if
		the user is logged in
		To assert that user is signed out, use "is_signed_out()" method as it
		is faster.
		:return: bool - True for logged in
		"""
		try:
			self.driver.wait_for_element("//div[contains(@class,'container__loggedIn')]")
			self.log.info('Asserted user is logged in.')
			return True
		except:
			self.log.info('Failed to assert that the user is logged in.')
			return False

	def is_signed_out(self)->bool:
		"""
		Will look for 'Sign in' link in the nav bar which is available only if
		the user is logged out
		To assert that user is signed in, use "is_signed_in()" method as it
		is faster.
		:return: bool - True for logged out
		"""
		try:
			self.driver.wait_for_element("@Sign In")
			self.log.info('Asserted user is logged out.')
			return True
		except:
			self.log.info('Failed to assert that the user is logged out.')
			return False

	def log_alert_message(self)->NoReturn:
		"""Get the alert displayed by kijiji, such as invalid login"""

		# get error message
		alert_banner = self.driver.find_element(
			'//div[@id="MessageContainer"]//div[@class="message"]',
			required=False
		)
		if alert_banner is not None:
			error = self.driver.find_element(
				'//div[@id="MessageContainer"]/div[contains(@class,"error")]',
				required=False,
			)
			if error is not None:
				self.log.info('Kijiji [ERROR] msg: %s' % (alert_banner.text,))
			else:
				self.log.info('Kijiji msg: %s' % (alert_banner.text,))

		# get success message
		alert_banner = self.driver.find_element(
			'//div[contains(@class,"container__success")]/*[starts-with(@class,"messageTitle")]',
			required=False
		)
		if alert_banner is not None:
			self.log.info('Kijiji [SUCCESS] msg: %s' % (alert_banner.text,))

	def new_messages(self)->int:
		pass

	def post_ad(self, data: dict):
		pass

	def reply_to_new_messages(self)->NoReturn:
		pass

	def sign_in(self, username:str, password:str)->NoReturn:
		"""
		Sign in to kijiji using the provided username and password.
		If the user is already signed in and it can be confirmed, the process
		will not be halted, however, in the event that a sign in cannot be
		confirmed, the process will be halted and will throw a RuntimeError
		exception.

		:param username: str
		:param password: str
		:return: NoReturn
		"""
		self.driver.goto(self.sign_in_page)
		if self.is_signed_out():
			self.log.info("Signing in to kijiji.")
			self.driver.send_keys('#LoginEmailOrNickname', username)
			self.driver.send_keys('#login-password', password)
			self.driver.click_button('#SignInButton')
			if not self.is_signed_in(): #failed confirm sign in
				self.log_alert_message()
				raise RuntimeError('Failed to sign in using id: "%s", pw: "%s".'
				                   % (username, password))
		else: #failed to confirm user is signed out
			if self.is_signed_in():
				self.log.info("Attempted to sign in, but the user is already "
				              "signed in.")
			else: #failed to confirm user is also signed in
				self.log.critical('Failed to assert that user is either '
				                  'signed in or signed out while trying to '
				                  'sign in. Site might have changed. User '
				                  'used: %s, password: %s'
				                  % (username, password))
				raise RuntimeError('Failed assert that the user is either '
				                   'signed in or signed out.')

	def sign_out(self)->NoReturn:
		"""
		Sign out from kijiji.
		If the user is already signed out and it can be confirmed, the process
		will not be halted, however, in the event that a sign out cannot be
		confirmed, the process will be halted and will throw a RuntimeError
		exception.

		:return: NoReturn
		"""
		url = self.driver.get_url()
		self.log.info("Signing out of kijiji.")
		if 'www.kijiji.ca' not in url:
			self.driver.goto(self.my_settings)
		if self.is_signed_in():
			dropdown = self.driver.wait_for_element("//button[contains(@class,'control')]")
			dropdown.click()
			logout = self.driver.wait_for_element("//button[contains(@class,'signOut')]")
			logout.click()
			if not self.is_signed_out():
				raise RuntimeError('Failed to sign out.')
			self.log_alert_message()
		else:
			if self.is_signed_out():
				self.log.info("Attempted to sign out, but the user is already "
				              "signed out.")
			else:
				self.log.critical('Failed to assert that user is either '
				                  'signed in or signed out while trying to '
				                  'sign out. Site might have changed.')
				raise RuntimeError('Failed assert that the user is either '
				                   'signed in or signed out.')


