from .config import *

# external
from typing import Any, Callable, List, NamedTuple, NoReturn, Union as U, Tuple
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

# internal

class Browser:

	driver: WebDriver = ...
	implicit_wait: int = ...
	log: Any = ...
	speed: int = ...
	screenshot_directory: str = ...
	cookies_directory: str = ...
	timeout: bool = ...

	def assert_proxy_is(self, ip:str)->NoReturn: ...
	def set_implicit_wait(self, time_to_wait: int) -> NoReturn: ...
	def unset_implicit_wait(self) -> NoReturn: ...

	""" from browser.pu """
	def __init__(self, browser: str = 'ff' , desired_capabilities: dict = None,
	             profile: object = None, options: object = None) -> NoReturn: ...
	# site-specific methods (must 'set_site_behaviour' first)
	def set_site_behaviour(self, site: str) -> NoReturn: ...
	def create_account(self, details: dict, cookies: str = None) -> bool: ...
	def create_content(self, details: dict) -> str: ...
	def delete_content(self, details: dict) -> bool: ...
	def edit_content(self, details: dict) -> bool: ...
	def is_signed_in(self) -> bool: ...
	def is_signed_out(self) -> bool: ...
	def sign_in(self, details: dict, cookies: str = None) -> NoReturn: ...
	def sign_out(self) -> NoReturn: ...
	def site_custom(self, method_name, *args) -> Any: ...

	""" from base.py """
	def find_element(self, locator: U[WebElement, str], tag: str=None,
	    required: bool=True, parent: U[WebDriver, WebElement]=None) -> WebElement : ...
	def find_elements(self, locator: U[List[WebElement], str], tag: str=None,
	    required: bool=False, parent: U[WebDriver, WebElement]=None) -> List[WebElement] : ...
	def is_text_present(self, text: str) -> bool: ...
	def is_enabled(self, locator: U[WebElement, str], tag: str=None) -> bool: ...
	def is_visible(self, locator: U[WebElement, str], tag: str=None) -> bool: ...

	""" from alert.py """
	def get_alert(self, timeout: int=DEFAULT_TIMEOUT, message: str ='') -> Alert: ...
	def get_alert_text(self, timeout: int=DEFAULT_TIMEOUT) -> str: ...
	def handle_alert(self, action: str='accept', timeout: int=DEFAULT_TIMEOUT) -> str: ...
	def input_text_into_alert(self, text: str, action: str='accept',
	                          timeout: int=None) -> str: ...

	""" from browsermanagement.py """
	def back(self) -> NoReturn: ...
	def forward(self) -> NoReturn: ...
	def get_session_id(self) -> str: ...
	def get_source(self) -> str: ...
	def get_title(self) -> str: ...
	def get_url(self) -> str: ...
	def goto(self, url: str) -> NoReturn: ...
	def refresh(self) -> NoReturn: ...
	def quit(self) -> NoReturn: ...

	""" from cookies.py """
	def add_cookie(self, cookie_dict: dict) -> NoReturn: ...
	def delete_all_cookies(self) -> NoReturn: ...
	def delete_cookie(self, name: str) -> NoReturn: ...
	def get_cookie(self, name:str) -> U[str, None]: ...
	def get_cookies(self) -> List[dict]: ...
	def load_cookies(self, filename: str, path: str='default') -> NoReturn: ...
	def save_cookies(self, filename: str) -> str: ...
	def set_cookies_directory(self, path: str=None, append: bool=True) -> str: ...
	def set_cookies_expiry(self, date: int=3735325880) -> NoReturn: ...

	""" from element.py """
	def clear_element_text(self, locator: U[WebElement, str]) -> NoReturn: ...
	def click_button(self, locator: U[WebElement, str]) -> NoReturn: ...
	def click_element(self, locator: U[WebElement, str]) -> NoReturn: ...
	def click_element_at_coordinates(self, locator: U[WebElement, str],
	                                 xoffset: int, yoffset: int) -> NoReturn: ...
	def click_image(self, locator: U[WebElement, str]) -> NoReturn: ...
	def double_click_element(self, locator: U[WebElement, str]) -> NoReturn: ...
	def drag_and_drop(self, locator: U[WebElement, str],
	                  target: U[WebElement, str]) -> NoReturn: ...
	def element_text_contains(self, locator: U[WebElement, str], expected: str,
	                          ignore_case: bool=True) -> bool: ...
	def element_text_is(self, locator: U[WebElement, str], expected: str,
	                    ignore_case: bool=False) -> bool: ...
	def get_element_attribute(self, locator: U[WebElement, str], attribute: str) -> str: ...
	def get_element_property(self, locator: U[WebElement, str], prop: str) -> str: ...
	def get_element_size(self, locator: U[WebElement, str]) -> (int, int): ...
	def get_text(self, locator: U[WebElement, str]) -> str: ...
	def page_contains_text(self, text:str) -> bool: ...
	def right_click_element_at_coordinates(self, locator: U[WebElement, str],
	                                       xoffset: int, yoffset: int) -> NoReturn: ...
	def send_keys(self, locator: U[WebElement, str]=None,
	               *keys: U[List[str], str]) -> NoReturn: ...
	def highlight_elements(self, locator: U[List[WebElement], WebElement, str],
	                       tag: str=None) -> NoReturn: ...
	def set_focus_to_element(self, locator: U[WebElement, str]) -> NoReturn: ...
	def mouse_down(self, locator: U[WebElement, str]) -> NoReturn: ...
	def mouse_out(self, locator: U[WebElement, str]) -> NoReturn: ...
	def mouse_over(self, locator: U[WebElement, str]) -> NoReturn: ...
	def mouse_up(self, locator: U[WebElement, str]) -> NoReturn: ...
	def scroll_element_into_view(self, locator: U[WebElement, str]) -> NoReturn: ...
	def simulate_event(self, locator: U[WebElement, str], event: str) -> NoReturn: ...

	""" from frames.py """
	def send_method_to_element_in_frame(self, frame_locator: U[WebElement, str, int],
	        element_locator: U[WebElement, str], method: Callable) -> Any: ...
	def switch_to_frame(self, locator: U[WebElement, str, int]) -> NoReturn: ...
	def unselect_frame(self) -> NoReturn: ...

	""" from javascript.py """
	def execute_javascript(self, *code: List[str]) -> Any: ...
	def execute_async_javascript(self, *code: List[str]) -> Any: ...
	def inject_jQuery(self) -> NoReturn: ...

	""" from screenshot.py """
	def capture_element_screenshot(self, locator: U[WebElement, str],
	                filename: str='element-screenshot-{index:03}.png') -> str: ...
	def capture_page_screenshot(self, filename: str='screenshot-{index:03}.png') -> str: ...
	def set_screenshot_directory(self, path: str=None, append: bool=True) -> str: ...

	""" from selects.py """
	def get_select_items(self, locator: U[WebElement, str],
	                     attribute:str='') -> List[U[str, Tuple[str, str]]]: ...
	def get_selected_item(self, locator: U[WebElement, str], values: bool=False) -> str: ...
	def select_all_from_multilist(self, locator: U[WebElement, str]) -> NoReturn: ...
	def select_from_list_by_index(self, locator: U[WebElement, str],
	                              *indexes: str) -> NoReturn: ...
	def select_from_list_by_value(self, locator: U[WebElement, str],
	                              *values: str) -> NoReturn: ...
	def select_from_list_by_label(self, locator: U[WebElement, str],
	                              *labels: str) -> NoReturn: ...
	def unselect_all_from_list(self, locator: U[WebElement, str]) -> NoReturn: ...
	def unselect_from_list_by_index(self, locator: U[WebElement, str],
	                                *indexes: str) -> NoReturn: ...
	def unselect_from_list_by_value(self, locator: U[WebElement, str],
	                                *values: str) -> NoReturn: ...
	def unselect_from_list_by_label(self, locator: U[WebElement, str],
	                                *labels: str) -> NoReturn: ...

	""" from tables.py """
	def get_table_cell_by_index(self, locator: U[WebElement, str],
	                    row: U[str, int], column: U[str, int]) -> WebElement: ...
	def get_table_cell_text(self, locator: U[WebElement, str],
	                    row: U[str, int], column: U[str, int]) -> U[str, None]: ...
	def get_table_cell_by_text(self, locator: U[WebElement, str],
	                           text: str) -> str: ...
	def get_table_row_by_index(self, locator: U[WebElement, str],
	                           row: U[str, int]) -> List[WebElement]: ...
	def get_table_row_by_text(self, locator: U[WebElement, str],
	                          text: str) -> List[WebElement]: ...

	""" from waiting.py """
	def wait_for_element(self, locator: U[WebElement, str], negate:bool =False,
	                     timeout: int=DEFAULT_TIMEOUT,
	                     parent: U[WebDriver, WebElement]=None) -> WebElement: ...
	def wait_for_element_to_be_enabled(self, locator: U[WebElement, str],
		        negate: bool=False, timeout: int=DEFAULT_TIMEOUT) -> WebElement : ...
	def wait_for_element_to_be_visible(self, locator, negate=False,
	                                   timeout=DEFAULT_TIMEOUT) -> WebElement: ...
	def wait_for_element_to_contain(self, locator: U[WebElement, str],
	                                text: str, negate: bool=False,
	                                timeout: int=DEFAULT_TIMEOUT) -> WebElement: ...
	def wait_for_script(self, condition: str, negate: bool=False,
	            timeout: int=DEFAULT_TIMEOUT, message: str='msg') -> Any: ...
	def wait_for_page_to_contain(self, text: str, negate:bool =False,
	                             timeout: int=DEFAULT_TIMEOUT)->bool: ...

	""" from windowmanager.py """
	def select_window(self, locator: U[List[str], str], timeout:int=None) -> str: ...
	def close_window(self) -> NoReturn: ...
	def get_all_windows_handles(self) -> List[str]: ...
	def get_all_windows_ids(self) -> List[str]: ...
	def get_all_windows_names(self) -> List[str]: ...
	def get_all_windows_titles(self) -> List[str]: ...
	def get_all_windows_urls(self) -> List[str]: ...
	def get_window_handle(self) -> str: ...
	def get_window_info(self) -> NamedTuple: ...
	def get_window_position(self) -> Tuple[int,int]: ...
	def get_window_size(self) -> Tuple[int,int]: ...
	def maximize_browser_window(self) -> NoReturn: ...
	def set_window_id(self, id: U[str, int]) -> NoReturn: ...
	def set_window_name(self, name: U[str, int]) -> NoReturn: ...
	def set_window_position(self, x: U[str, int], y: U[str, int]) -> NoReturn: ...
	def set_window_size(self, width: U[str, int],
	                    height: U[str, int]) -> NoReturn: ...


