import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data

# no modificar
def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common import WebDriverException

    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance')
                    if log.get("message") and 'api/v1/number?number' in log["message"]]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code
        except WebDriverException:
            time.sleep(1)
    raise Exception("No se encontró el código de confirmación del teléfono.")

class UrbanRoutesPage:
    # Selectores

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    round_button = (By.CSS_SELECTOR, ".button.round")
    comfort_option = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_modal_button = (By.CSS_SELECTOR, 'div.np-button')
    phone_input = (By.ID, 'phone')
    submit_phone_button = (By.CSS_SELECTOR, '.button.full')
    code_input = (By.XPATH, "//input[@type='text' and @placeholder='xxxx']")
    confirm_code_button = (By.XPATH, "//button[contains(text(), 'Confirmar')]")
    confirm_button_number = (By.XPATH, "//button[text()='Confirmar']")
    payment_method = (By.XPATH, "//div[contains(@class, 'pp-button') and contains(., 'Método de pago')]")
    add_card = (By.XPATH, "//div[contains(@class, 'pp-row') and .//div[text()='Agregar tarjeta']]")
    card_number_input = (By.ID, 'number')
    code_card_input = (By.XPATH, "//div[contains(@class, 'card-code-input')]//input[@id='code']")
    add_card_text = (By.XPATH, "//div[contains(@class, 'section') and contains(@class, 'active') and .//div[text()='Agregar tarjeta']]")
    add_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_button_payment_method = (By.XPATH, "//div[contains(@class, 'section') and contains(., 'Método de pago')]//button[contains(@class, 'close-button')]")
    field_message_for_driver = (By.CSS_SELECTOR, "input#comment")
    circle_in_pannel = (By.XPATH, "//div[@class='dst-picker-row']//input[@id='from']")
    display_order_requirements = (By.CSS_SELECTOR, ".reqs-arrow > img[alt='Arrow']")
    blanket_and_scarves = (By.XPATH, "//div[text()='Manta y pañuelos']/ancestor::div[contains(@class, 'r-sw-container')]//div[contains(@class, 'switch')]")
    plus_counter = (By.CSS_SELECTOR, ".r-counter-container .counter .counter-plus")
    button_order_a_taxi = (By.CSS_SELECTOR, ".smart-button-wrapper button.smart-button > span.smart-button-main")
    search_car = (By.XPATH, "//div[@class='order-header-content']/div[normalize-space(text())='Buscar automóvil']")
    countdown_locator = (By.CSS_SELECTOR, ".order-header .order-header-content > .order-header-time")
    driver_text = (By.CSS_SELECTOR, ".order-header-content > .order-header-title")


    #methods

    def __init__(self, driver):
        self.driver = driver

    def set_addresses(self, address_from, address_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.from_field)).send_keys(address_from)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.to_field)).send_keys(address_to)

    def verify_addresses(self, from_address, to_address):
        assert self.driver.find_element(*self.from_field).get_property('value') == from_address
        assert self.driver.find_element(*self.to_field).get_property('value') == to_address

    def select_round_trip(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.round_button)
        ).click()

    def select_comfort_option(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.comfort_option)
        ).click()

    def open_phone_modal(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.phone_modal_button)
        ).click()

    def enter_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def submit_phone_number(self):
        self.driver.find_element(*self.submit_phone_button).click()

    def enter_confirmation_code(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.code_input))
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_input).send_keys(code)
        self.driver.find_element(*self.confirm_code_button).click()

    def click_confirmation_code(self):
        self.driver.find_element(*self.confirm_button_number).click()

    def clik_enter_payment_method(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.payment_method))
        self.driver.find_element(*self.payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()

    def enter_card_number(self):
        self.driver.find_element(*self.card_number_input).send_keys(data.card_number)

    def enter_code_card_input(self):
        self.driver.find_element(*self.code_card_input).send_keys(data.card_code)

    def click_add_card_text(self):
        self.driver.find_element(*self.add_card_text).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()

    def click_close_button_payment_method(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.close_button_payment_method))
        self.driver.find_element(*self.close_button_payment_method).click()

    def input_message_for_driver(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.field_message_for_driver))
        self.driver.find_element(*self.field_message_for_driver).send_keys(data.message_for_driver)
        self.driver.find_element(*self.circle_in_pannel).click()

    def click_display_order_requirements(self):
        self.driver.find_element(*self.display_order_requirements).click()

    def click_blanket_and_scarves(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.blanket_and_scarves))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.blanket_and_scarves)).click()

    def click_add_ice_cream(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.plus_counter))
        self.driver.find_element(*self.plus_counter).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.plus_counter)).click()

    def verify_button_order_a_taxi_is_on(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.button_order_a_taxi))
        assert self.driver.find_element(*self.button_order_a_taxi).is_displayed()
        print("el boton para solicitar un taxi si se muestra")

    def driver_information_appears(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.button_order_a_taxi)).click()
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.search_car))
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.countdown_locator))
        WebDriverWait(self.driver,40).until(expected_conditions.invisibility_of_element_located(self.countdown_locator))
        WebDriverWait(self.driver,30).until(expected_conditions.presence_of_element_located(self.driver_text)).is_displayed()
        #driver_text_assert = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(self.driver_text))

        #assert self.driver.find_element(*self.driver_img).is_displayed()
        #assert "El conductor llegará" in driver_img_assert
        #assert driver_text_assert.is_displayed(), "El texto del conductor no está visible"


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_addresses(address_from, address_to)
        routes_page.verify_addresses(address_from, address_to)

    def test_set_comfort_button(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_addresses(data.address_from, data.address_to)
        routes_page.select_round_trip()
        routes_page.select_comfort_option()

    def test_set_number_phone_field(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.submit_phone_number()
        page.enter_confirmation_code()

    def test_add_card(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.clik_enter_payment_method()
        page.click_add_card()
        page.enter_card_number()
        page.enter_code_card_input()
        page.click_add_card_text()
        page.click_add_card_button()
        page.click_close_button_payment_method()

    def test_enter_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.input_message_for_driver()

    def test_select_blanket_and_scarves(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.click_display_order_requirements()
        page.click_blanket_and_scarves()

    def test_add_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.click_display_order_requirements()
        page.click_add_ice_cream()

    def test_button_order_a_taxi_is_on(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.clik_enter_payment_method()
        page.click_add_card()
        page.enter_card_number()
        page.enter_code_card_input()
        page.click_add_card_text()
        page.click_add_card_button()
        page.click_close_button_payment_method()
        page.verify_button_order_a_taxi_is_on()

    def test_driver_information_appears(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.clik_enter_payment_method()
        page.click_add_card()
        page.enter_card_number()
        page.enter_code_card_input()
        page.click_add_card_text()
        page.click_add_card_button()
        page.click_close_button_payment_method()
        page.verify_button_order_a_taxi_is_on()
        page.driver_information_appears()

        time.sleep(1)

    @classmethod
    def teardown_class(cls):
     cls.driver.quit()