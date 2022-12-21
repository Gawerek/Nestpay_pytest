# -*- coding: utf-8 -*-

"""Zbiór bazowych klas reprezentujących różne elementy strony."""
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from constants import WAITING_TIME


class BasePageElement:
    """Klasa bazowa dla pojedyńczego elementu strony."""

    def __init__(self, locator_type, locator_value):
        self.locator_value = locator_value
        self.locator_type = locator_type
        self.locator = (locator_type, locator_value)

    def _find_element(self, driver):
        """Znajdź element na stronie."""
        elements = WebDriverWait(driver, WAITING_TIME).until(
            lambda driver: driver.find_elements(*self.locator),
            "The '{}' element was not found within {} seconds".format(self.locator_value, WAITING_TIME))

        if len(elements) > 1:  # considering > 5 terminals, this will yield an error 🥴
            raise ValueError("Unexpectedly more than one element with given locator - {} - was found.".
                             format(self.locator_value))
        return elements[0]

    def _find_elements(self, driver, locator=None):
        """Znajdź element na stronie."""
        elements = WebDriverWait(driver, WAITING_TIME).until(
            lambda driver: driver.find_elements(*(locator if locator else self.locator)),
            "At least one '{}' element was not found within {} seconds".format(self.locator_value, WAITING_TIME))
        return elements


class TextElement(BasePageElement):
    """Element reprezentujący pole tekstowe."""

    def __set__(self, obj, value):
        """Ustawienie wartości dla pola tekstowego.
        """
        element = self._find_element(obj.driver)
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.TAB)

    def __get__(self, instance, owner):
        return self._find_element(instance.driver)


class CheckboxElement(BasePageElement):
    """Element reprezentujący pole wyboru tak/nie."""

    def __set__(self, obj, value):
        """Ustawienie wartości."""
        if not isinstance(value, bool):
            raise ValueError("You are trying to assign '{}' value to CheckboxElement."
                             " Only True/False values are permitted".format(value))
        element = self._find_element(obj.driver)
        if value ^ element.is_selected():
            element.click()

    def __get__(self, obj, owner):
        """Pobranie wartości."""
        element = self._find_element(obj.driver)
        return element.is_selected()


class ClickableElement(BasePageElement):
    """Element reprezentujący obiekt klikalny np. przycisk, odnośnik."""

    def _find_element(self, driver, locator=None):
        """Znajdź klikalny element."""
        WebDriverWait(driver, WAITING_TIME).until(EC.element_to_be_clickable(self.locator),
                                              "The {} element was not clickable within {} seconds".
                                           format(self.locator_value, WAITING_TIME))

        return super()._find_element(driver)

    def __get__(self, obj, owner):
        """Pobieranie danego elementu"""
        return self._find_element(obj.driver)


class HoverableElement(BasePageElement):
    """Element którego akcja wywoływana jest przez najechanie myszką"""
    def __get__(self, obj, owner):
        """Pobieranie danego elementu"""
        setattr(self, "driver", obj.driver) # element requires driver to be hovered over
        return self

    def hover(self):
        performer = ActionChains(self.driver)
        WebDriverWait(self.driver, WAITING_TIME).until(EC.visibility_of_element_located(self.locator)),\
            f"Element located by {self.locator_type}: {self.locator_value} not visible within {WAITING_TIME}"
        performer.move_to_element(self._find_element(self.driver)).perform()


class ListElement(BasePageElement):
    """Element reprezentujący listę
    UWAGA, dla systemu ARC elementy listy są gdzie indziej niż guzik je rozwijający, jak i pole zwartością ;-;"""

    def __init__(self, locator_type, locator_value, use_text_instead_of_value=False):
        self.children_locator = (locator_type, f"{locator_value}/option")
        self.use_text_instead_of_value = use_text_instead_of_value
        super().__init__(locator_type, locator_value)

    def __set__(self, obj, value):
        """Ustawienie wartości."""
        element = self._find_element(obj.driver)
        element.click()
        children = self._find_elements(obj.driver, self.children_locator)
        for elem in children:
            if elem.get_attribute('textContent' if self.use_text_instead_of_value else 'value') == value:
                break
        else:
            raise LookupError(f"No child element of value {value} found")
        elem.click()

    def __get__(self, obj, owner):
        """Pobranie wartości."""
        element = self._find_element(obj.driver)
        return element.is_selected()


class RadioButtonsElement(BasePageElement):
    """Klasa reprezentujące zestaw zależnych przyxisków typu radio"""

    def __init__(self, buttons: dict):
        """Inicjalizacja klasy
        :param buttons
            dict: {nazwa: [locator, locator_value], ...}"""
        super().__init__(locator_type=None, locator_value=None)
        self.buttons = buttons

    def __set__(self, obj, value):
        """Ustawienie wartości."""
        assert value in self.buttons.keys(), f"Value {value} not present in radio names keys. Available values:" \
                                             f"{','.join(list(self.buttons.keys()))}"
        self.locator = self.buttons[value]
        element = self._find_element(obj.driver)
        element.click()

    def __get__(self, obj, owner):
        """Pobranie wartości."""
        for name, locator in self.buttons.items():
            self.locator = locator
            if self._find_element(obj.driver).is_selected():
                return name
        return None


class LabelElement(BasePageElement):
    def __set__(self, instance, value):
        raise NotImplementedError(f"Label element is read only, attempted to set value {value}")

    def __get__(self, obj, owner):
        return "\n".join(element.get_attribute('textContent') for element in self._find_elements(obj.driver))
