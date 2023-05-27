import random


class Utils:
    """Utilities functions class"""

    def create_xpath(self, xpath, xpath_replace_string, mapper):
        xpath = xpath.replace(xpath_replace_string, mapper)
        print(xpath)
        return xpath

    def get_random_collection_filter(self, d):
        lst = []
        for k in d:
            if k != "AllCollections":
                lst.append(k)
        return lst[random.randint(0, len(lst)-1)]

    def get_random_warrior_id(self):
        return random.randint(0, 5999)

    def standarize_text(self, text):
        text = ''.join(text.splitlines())
        text = text.replace(". ",".")
        return text
