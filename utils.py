import random


class Utils:
    """Utilities functions class"""
    @staticmethod
    def create_xpath(xpath, xpath_replace_string, mapper):
        return xpath.replace(xpath_replace_string, mapper)

    @staticmethod
    def create_xpath_warrior(xpath, warriorid, mapper):
        replaced_collection = xpath.replace("/1/", mapper)
        replaced_id = replaced_collection.replace("3183", warriorid)
        return replaced_id

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
