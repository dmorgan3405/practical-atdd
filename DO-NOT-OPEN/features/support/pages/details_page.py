from page_object import PageObject


class DetailsPage(PageObject):

    def define_elements(self):
        self.button(name="adopt_me", identifier={'css': '[value="Adopt Me!"]'})
