from page_object import PageObject


class DashboardPage(PageObject):

    def define_elements(self):
        self.page_url('{base_url}')
        self.buttons('view_detail', {'css': '[value="View Details"]'})

    def view_details_for(self, puppy_index):
        self.view_detail_elements()[puppy_index - 1].click()
