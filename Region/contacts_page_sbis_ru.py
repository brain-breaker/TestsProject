from atf.ui import *


class ContactsPageSbisRu(Region):

    region = Element(By.CSS_SELECTOR, 'div.sbisru-Contacts .sbis_ru-Region-Chooser__text', 'Регион')
    partner_list = Element(By.CSS_SELECTOR, 'div.sbisru-Contacts-List__col', 'Список партнеров')
    partner_city = Element(By.CSS_SELECTOR, '#city-id-2', 'Город партнеров')
    partner_name = CustomList(By.CSS_SELECTOR, 'div.sbisru-Contacts-List__name', 'Партнер')
    selected_region = Element(By.XPATH, '//*[contains(text(), "Камчатский край")]', 'Выбранный регион')

    def go_to_region(self):
        self.region.click()

    def go_to_selected_region(self):
        self.selected_region.scroll_into_view()
        self.selected_region.click()

    def should_be_correct_our_partner_city(self, correct_our_partner_city):
        self.partner_city.should_be(ExactText(correct_our_partner_city))

    def should_be_correct_our_partner_name(self, correct_our_partner_name):
        self.partner_name.item(1).should_be(ExactText(correct_our_partner_name))

    def should_be_correct_our_region(self, correct_our_region):
        self.region.should_be(ExactText(correct_our_region))

    def should_be_correct_selected_partner_city(self, correct_selected_partner_city):
        self.partner_city.should_be(ExactText(correct_selected_partner_city))

    def should_be_correct_selected_partner_name(self, correct_selected_partner_name):
        self.partner_name.item(1).should_be(ExactText(correct_selected_partner_name))

    def should_be_correct_selected_region(self, correct_selected_region):
        self.region.should_be(ExactText(correct_selected_region))

    def should_be_correct_selected_region_url_and_title(self, correct_selected_region_url, correct_selected_region):
        self.browser.should_be(UrlContains(correct_selected_region_url), TitleContains(correct_selected_region))

    def should_be_partner_list(self):
        self.partner_list.should_be(Displayed)
