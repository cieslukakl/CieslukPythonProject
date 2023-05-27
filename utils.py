import random


class Utils:
    """Utilities functions class"""
    @staticmethod
    def create_xpath(xpath, xpath_replace_string, mapper):
        xpath = xpath.replace(xpath_replace_string, mapper)
        print(xpath)
        return xpath

    @staticmethod
    def get_random_collection_filter(d):
        lst = []
        for k in d:
            if k != "AllCollections":
                lst.append(k)
        return lst[random.randint(0, len(lst)-1)]

    @staticmethod
    def get_random_warrior_id():
        return random.randint(0, 5999)

    @staticmethod
    def standarize_text(text):
        text = ''.join(text.splitlines())
        text = text.replace(". ", ".")
        return text
