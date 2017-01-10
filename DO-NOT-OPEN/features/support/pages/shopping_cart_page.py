from page_object import PageObject


class ShoppingCartPage(PageObject):

    def define_elements(self):
        self.button(name='complete_adoption', identifier={'css': '[value="Complete the Adoption"]'})
        self.button(name='continue_shopping', identifier={'css': '[value="Adopt Another Puppy"]'})
