from operator import contains

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
from selenium.webdriver.support import expected_conditions as EC



import data

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
    blanket_and_scarves = (By.XPATH, "//div[@class='r-sw-container'][div[@class='r-sw-label' and normalize-space(.)='Manta y pañuelos']]//span[contains(@class,'slider')]")
    plus_counter = (By.XPATH, "//div[contains(@class,'r-counter-container')][ .//div[@class='r-counter-label' and normalize-space(.)='Helado'] ]//div[@class='counter-plus']")
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

    def comfort_option_assert(self):
        switch = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[data-for='tariff-card-4'].i-button.tcard-i"))
        )
        switch.click()

        active_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-for='tariff-card-4'].i-button.tcard-i.active"))
        )

        assert "active" in active_button.get_attribute("class")

    def open_phone_modal(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.phone_modal_button)
        ).click()

    def enter_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def phone_number_assert(self):
        phone_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                self.phone_input)
        )
        value = phone_field.get_attribute("value")
        assert data.phone_number in value, f"Expected '{data.phone_number}' in field, but got '{value}'"

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

    def credit_card_asset(self):
        # Espera a que el campo esté visible
        payment_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.payment_method)
        )
        # Extrae el texto visible del contenedor
        field_text = payment_field.text
        # Validación defensiva
        assert field_text, "No se encontró texto visible en el campo de método de pago"
        assert "Tarjeta" in field_text, f"Expected 'Tarjeta' in field, but got '{field_text}'"

    def input_message_for_driver(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.field_message_for_driver))
        self.driver.find_element(*self.field_message_for_driver).send_keys(data.message_for_driver)
        self.driver.find_element(*self.circle_in_pannel).click()

    def message_for_driver_assert(self):
        # Espera a que el campo esté visible
        message_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.field_message_for_driver)
        )
        # Extrae el texto visible del contenedor
        field_text = message_field.text or message_field.get_attribute("value")
        # Validación defensiva
        assert field_text, "No se encontró texto visible en el campo de mensaje para el conductor"
        assert data.message_for_driver in field_text, f"Expected '{data.message_for_driver}' in field, but got '{field_text}'"

    def click_display_order_requirements(self):
        self.driver.find_element(*self.display_order_requirements).click()

    def click_blanket_and_scarves(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.blanket_and_scarves))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.blanket_and_scarves)).click()

        # Localiza el input asociado al label "Manta y pañuelos"
        xpath_input = (
            "//div[@class='r-sw-container'][div[@class='r-sw-label' and normalize-space(.)='Manta y pañuelos']]"
            "//input[@class='switch-input']")

        checkbox = self.driver.find_element(By.XPATH, xpath_input)

        # Assert: el switch debe estar activado
        assert checkbox.is_selected(), "El switch 'Manta y pañuelos' no quedó activado después del clic"

    def click_add_ice_cream(self):
        # Espera a que el botón sea clickeable
        plus_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.plus_counter)
        )

        # Primer clic
        plus_button.click()

        # Espera a que el contador se actualice (opcional pero recomendable)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                (By.CLASS_NAME, "counter-value"), "1"
            )
        )

        # Segundo clic
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.plus_counter)
        ).click()

    def assert_two_ice_creams(self):
        xpath_value = ("//div[@class='r-counter-container']"
                       "[div[@class='r-counter-label' and normalize-space(.)='Helado']]"
                       "//div[@class='counter-value']")

        # Espera a que el contador se actualice
        counter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_value))
        )

        value = counter.text.strip()
        assert value == "2", f"Esperaba 2 helados, pero obtuve {value}"

    def verify_button_order_a_taxi_is_on(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.button_order_a_taxi))
        assert self.driver.find_element(*self.button_order_a_taxi).is_displayed()
        print("el boton para solicitar un taxi si se muestra")

    def request_a_taxi_is_visible_assert(self):
        # Espera a que el campo esté visible
        button_message_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.button_order_a_taxi)
        )
        # Extrae el texto visible del contenedor
        field_text = button_message_field.text or button_message_field.get_attribute("value")
        # Validación defensiva
        assert field_text, "No se encontró texto visible en el boton para pedir el taxi"
        assert "Pedir un taxi" in field_text, f"Expected 'Pedir un taxi' in field, but got '{field_text}'"

    def driver_information_appears(self):
        # Click en el botón para pedir taxi
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.button_order_a_taxi)
        ).click()

        # Espera a que aparezca el buscador de coche
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(self.search_car)
        )

        # Espera a que aparezca el contador
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.countdown_locator)
        )

        # Espera a que desaparezca el contador
        WebDriverWait(self.driver, 40).until(
            expected_conditions.invisibility_of_element_located(self.countdown_locator)
        )

        # Espera a que el texto del conductor sea visible
        driver_info_element = WebDriverWait(self.driver, 45).until(
            expected_conditions.visibility_of_element_located(self.driver_text)
        )

        # Espera a que el texto contenga la frase general
        WebDriverWait(self.driver, 45).until(
            expected_conditions.text_to_be_present_in_element(self.driver_text, "El conductor llegará en")
        )

        # Validación final
        driver_text = driver_info_element.text or driver_info_element.get_attribute("value")
        assert "El conductor llegará en" in driver_text, \
            f"Expected driver info to contain 'El conductor llegará en', but got '{driver_text}'"

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
        routes_page.comfort_option_assert()
        #assert routes_page.comfort_option_assert() is True

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
        page.phone_number_assert()

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
        page.credit_card_asset()

    def test_enter_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.input_message_for_driver()
        page.message_for_driver_assert()

    def test_select_blanket_and_scarves(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        #page.click_display_order_requirements()
        page.click_blanket_and_scarves()

    def test_add_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        #page.click_display_order_requirements()
        page.click_add_ice_cream()

    def test_button_order_a_taxi_is_on(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.submit_phone_number()
        page.enter_confirmation_code()
        page.clik_enter_payment_method()
        page.click_add_card()
        page.enter_card_number()
        page.enter_code_card_input()
        page.click_add_card_text()
        page.click_add_card_button()
        page.click_close_button_payment_method()
        page.verify_button_order_a_taxi_is_on()
        page.request_a_taxi_is_visible_assert()

    def test_driver_information_appears(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_addresses(data.address_from, data.address_to)
        page.select_round_trip()
        page.select_comfort_option()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.submit_phone_number()
        page.enter_confirmation_code()
        page.clik_enter_payment_method()
        page.click_add_card()
        page.enter_card_number()
        page.enter_code_card_input()
        page.click_add_card_text()
        page.click_add_card_button()
        page.click_close_button_payment_method()
        page.input_message_for_driver()
        page.message_for_driver_assert()
        page.verify_button_order_a_taxi_is_on()
        page.driver_information_appears()

    @classmethod
    def teardown_class(cls):
     cls.driver.quit()