from atf.ui import *


class MainPageSbisRu(Region):

    contacts = Element(By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]', 'Контакты')

    def go_to_contacts_section(self):
        self.contacts.click()
