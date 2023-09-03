from src.phonebook import Phonebook


class TestPhonebook1:
    def test_add_success(self):
        phone = Phonebook()
        expected_result = "Número adicionado"

        result = phone.add("SAMU", "180")

        assert result == expected_result

    def test_add_invalid_name_hashtag(self):
        phone = Phonebook()
        expected_result = "Nome inválido"

        result = phone.add("#", "100")

        assert result == expected_result

    def test_add_invalid_name_at(self):
        phone = Phonebook()
        expected_result = "Nome inválido"

        result = phone.add("@", "100")

        assert result == expected_result

    def test_add_invalid_name_exclamation(self):
        phone = Phonebook()
        expected_result = "Nome inválido"

        result = phone.add("!", "100")

        assert result == expected_result

    def test_add_invalid_name_dollar_sign(self):
        phone = Phonebook()
        expected_result = "Nome inválido"

        result = phone.add("$", "100")

        assert result == expected_result

    def test_add_invalid_name_percent(self):
        phone = Phonebook()
        expected_result = "Nome inválido"

        result = phone.add("%", "100")

        assert result == expected_result

    def test_add_existent(self):
        phone = Phonebook()
        expected_result = "Número adicionado"

        result = phone.add("PM", "190")

        assert result == expected_result

    def test_add_invalid_number(self):
        phone = Phonebook()
        expected_result = "Número inválido"

        result = phone.add("Joao", "")

        assert result == expected_result

    def test_lookup_success(self):
        phone = Phonebook()
        phone.add("SAMU", "180")
        expected_result = "180"

        result = phone.lookup("SAMU")

        assert result == expected_result

    def test_get_names(self):
        phone = Phonebook()
        expected_list = ['POLICIA', 'PM', 'BOMBEIROS']
        phone.add('PM', '190')
        phone.add('BOMBEIROS', '170')
        names = phone.get_names()

        assert sorted(names) == sorted(expected_list)

    def test_get_name_by_number(self):
        phone = Phonebook()
        phone.add('SAMU', '180')
        expected_result = "SAMU"

        result = phone.get_name_by_number("180")

        assert result == expected_result

    def test_get_name_by_number_doesnt_exist(self):
        phonebook = Phonebook()
        expected_result = "Número não encontrado"

        result = phonebook.get_name_by_number("100")

        assert result == expected_result

    def test_change_number(self):
        phone = Phonebook()
        phone.add('SAMU', '190')
        expected_result = "Número foi modificado"

        result = phone.change_number("SAMU", "192")

        assert result == expected_result

    def test_change_number_error(self):
        phonebook = Phonebook()
        expected_result = "Número não foi modificado"

        result = phonebook.change_number("Joao", "10")

        assert result == expected_result

    def test_clear(self):
        phonebook = Phonebook()
        expected_result = "phonebook limpado"

        result = phonebook.clear()

        assert result == expected_result

    def test_lookup_invalid_name_hashtag(self):
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        result = phonebook.lookup("Joao #")

        assert result == expected_result

    def test_lookup_invalid_name_at(self):
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        result = phonebook.lookup("Joao @")

        assert result == expected_result

    def test_lookup_invalid_name_exclamation(self):
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        result = phonebook.lookup("Joao !")

        assert result == expected_result

    def test_lookup_invalid_name_dollar_sign(self):
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        result = phonebook.lookup("Joao $")

        assert result == expected_result

    def test_lookup_invalid_name_percent(self):
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        result = phonebook.lookup("Joao %")

        assert result == expected_result

    def test_delete_number(self):
        phonebook = Phonebook()
        expected_result = "Número foi deletado"
        phonebook.add("João", "1818")

        result = phonebook.delete("João")

        assert result == expected_result
