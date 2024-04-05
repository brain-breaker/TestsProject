from atf import log, info
from atf.ui import *
from Region.main_page_sbis_ru import MainPageSbisRu
from Region.contacts_page_sbis_ru import ContactsPageSbisRu


class TestRegionPartners(TestCaseUI):

    def test(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)
        log('Перейти на https://sbis.ru/ в раздел "Контакты"')
        main_page_sbis = MainPageSbisRu(self.driver)
        main_page_sbis.go_to_contacts_section()

        log('Проверить, что определился ваш регион и есть список партнеров')
        our_region = 'Ярославская обл.'
        our_partner_city = 'Ярославль'
        our_partner_name = 'СБИС - Ярославль'
        contacts_page_sbis = ContactsPageSbisRu(self.driver)
        contacts_page_sbis.should_be_partner_list()
        contacts_page_sbis.should_be_correct_our_region(our_region)
        contacts_page_sbis.should_be_correct_our_partner_city(our_partner_city)
        contacts_page_sbis.should_be_correct_our_partner_name(our_partner_name)

        info('Изменить регион')
        contacts_page_sbis.go_to_region()
        contacts_page_sbis.go_to_selected_region()

        log('Проверить, что подставился выбранный регион, список партнеров изменился, '
            'url и title содержат информацию выбранного региона')
        required_region = 'Камчатский край'
        required_region_description = '41-kamchatskij-kraj'
        required_partner_city = 'Петропавловск-Камчатский'
        required_partner_name = 'СБИС - Камчатка'
        contacts_page_sbis.should_be_correct_selected_region(required_region)
        contacts_page_sbis.should_be_correct_selected_partner_city(required_partner_city)
        contacts_page_sbis.should_be_correct_selected_partner_name(required_partner_name)
        contacts_page_sbis.should_be_correct_selected_region_url_and_title(required_region_description, required_region)
