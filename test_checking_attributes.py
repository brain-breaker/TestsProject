from atf import log, info
from atf.ui import *


class MainPageSbisRu(Region):
    contacts = Element(By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]', 'Контакты')


class ContactsPageSbisRu(Region):
    tensor_banner = Element(By.CSS_SELECTOR, '[class = "sbisru-Contacts__logo-tensor mb-12"]', 'Баннер Тензор')


class MainPageTensorRu(Region):
    required_block = Element(By.XPATH, '//*[text()="Сила в людях"]', 'Блок "Сила в людях"')
    more_detailes = Element(By.CSS_SELECTOR, 'a.tensor_ru-link[href="/about"]', 'Подробнее')


class AboutPageTensorRu(Region):
    required_section = Element(By.XPATH, '//*[text()="Работаем"]', 'Раздел "Работаем"')
    block_with_foto = CustomList(By.CSS_SELECTOR, 'div.tensor_ru-About__block3-image-wrapper img', 'Фотографии')


class TestAttributesFoto(TestCaseUI):

    def test(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)
        log('Перейти на https://sbis.ru/ в раздел "Контакты"')
        main_page_sbis = MainPageSbisRu(self.driver)
        main_page_sbis.contacts.click()

        log('Найти баннер Тензор, кликнуть по нему')
        contacts_page_sbis = ContactsPageSbisRu(self.driver)
        contacts_page_sbis.tensor_banner.should_be(Displayed)

        log('Перейти на https://tensor.ru/')
        self.browser.switch_to_new_window(action=contacts_page_sbis.tensor_banner.click)

        log('Проверить, что есть блок "Сила в людях"')
        main_page_tensor = MainPageTensorRu(self.driver)
        main_page_tensor.required_block.should_be(Displayed)

        log('Перейти в блоке "Сила в людях" в "Подробнее" и '
            'проверить, что открывается https://tensor.ru/about')
        main_page_tensor.more_detailes.should_be(Displayed)
        main_page_tensor.more_detailes.scroll_into_view()
        main_page_tensor.more_detailes.click()

        log('Найти раздел "Работаем" и '
            'проверить, что у всех фотографий хронологии одинаковые высота (height) и ширина (width)')
        about_page_tensor = AboutPageTensorRu(self.driver)
        about_page_tensor.required_section.should_be(Displayed)
        height = about_page_tensor.block_with_foto.item(1).get_attribute('height')
        width = about_page_tensor.block_with_foto.item(1).get_attribute('width')
        for i in range(2, 5):
            (about_page_tensor.block_with_foto.item(i).
             should_be(Attribute(height=height, width=width),
                       msg=f'The attributes {about_page_tensor.block_with_foto.item(i)} are different!'))
