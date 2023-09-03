class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '@' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '!' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '$' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '%' in name:
            return 'Nome inválido'  # corrigido erro ortográfico

        if len(number) == 0:  # corrigido bug. Troquei < por ==
            return 'Número inválido'  # corrigido erro ortográfico

        if name not in self.entries:
            self.entries[name] = number

        return 'Número adicionado'  # correção de identação

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '@' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '!' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '$' in name:
            return 'Nome inválido'  # corrigido erro ortográfico
        if '%' in name:
            return 'Nome inválido'  # corrigido erro ortográfico

        return self.entries[name]

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries.clear()  # corrigido bug
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def get_name_by_number(self, number):
        for entry_name, entry_number in self.entries.items():
            if entry_number == number:
                return entry_name
        return "Número não encontrado"

    def change_number(self, name, new_number):
        for entry_name, entry_number in self.entries.items():
            if entry_name == name:
                self.entries[name] = new_number
                return "Número foi modificado"
        return "Número não foi modificado"

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return "Número foi deletado"  # corrigido erro ortográfico
