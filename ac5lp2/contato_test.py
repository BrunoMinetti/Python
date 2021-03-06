from agenda import Contato, CreateContactError, Telefone

from agenda import (Contato, CreateContactError, DeleteError,
                    Email, Telefone)


class TelefoneAtualizado(Telefone):
    """
    Eu esqueci de incluir este método na classe de Telefone, então
    estou criando esta classe para poder adicionar o método à classe Telefone
    sem que vocês precisem editar o código de vocês. Basta usar a nova classe
    que criei durantes os testes, como fiz.

    Portanto NÃO INCLUAM este método na classe Telefone de vocês.
    """

    def __eq__(self, other):
        if not isinstance(other, Telefone):
            raise TypeError('Não é possível comparar um Telefone com '
                            'objetos de outro tipo')
        n_self = self.telefone.replace('-', '')
        n_other = other.telefone.replace('-', '')
        return n_self == n_other


def test_cria_contato():
    try:
        c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    except TypeError:
        assert False, "Erro ao criar o contato"
    else:
        assert c.nome == "Aluno", 'O nome foi criado incorretamente'
        assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
        assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")
        assert isinstance(c.get_telefones()['principal'], Telefone)
        assert isinstance(c.get_emails()['principal'], Email)


def test_nao_cria_contato():
    contatos = [
        (123, "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br"),
        ('', "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br"),
        ("Aluno", 11999999999, "aluno@aluno.faculdadeimpacta.com.br"),
        ("Aluno", "1199999-9999", "aluno.faculdadeimpacta.com.br")
    ]
    for contato in contatos:
        try:
            Contato(contato[0], contato[1], contato[2])
        except TypeError:
            assert True, "Erro ao criar o contato"
        except ValueError:
            assert True, "Passado valor errado"
        except CreateContactError:
            assert True, "Não levantou o erro CreateContactError"
        except Exception:
            raise AssertionError('Levantou um erro do tipo incorreto')
        else:
            raise AssertionError('Não deveria criar um contato com nome vazio')


def test_adiciona_telefone():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
    assert c.get_telefones()['fixo'] == TelefoneAtualizado("113322-4567")
    assert c.get_telefones()['celular'] == TelefoneAtualizado("1198888-8888")


def test_adiciona_outro_telefone_como_principal():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    try:
        c.adiciona_telefone("1198888-8888")
    except ValueError:
        pass
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1198888-8888")


def test_adiciona_telefone_invalido_1():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    telefones = [
        ("11332211-456789", "fixo"),
        ("1198888", "celular"),
        ('', "fixo"),
        ("1199-999", "principal"),
        ("1198888")
    ]
    for telefone in telefones:
        try:
            c.adiciona_telefone(telefone[0], telefone[1])
        except ValueError:
            pass
        # except AssertionError:
        #     assert True, 'Telefone pode conter hífens e ter de 8 a 11 dígitos'
        else:
            raise AssertionError('Telefone pode conter hífens e ter de 8 a 11 dígitos')
        assert not any(['fixo' in c.get_telefones()])
        assert not any(['celular' in c.get_telefones()])


def test_adiciona_telefone_invalido_2():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    try:
        c.adiciona_telefone(1198888, "celular")
        c.adiciona_telefone(11.98888 - 8888, "celular")
    except TypeError:
        pass
    else:
        raise AssertionError('Telefone deve ser do tipo string')
    assert not any(['celular' in c.get_telefones()])


def test_adiciona_email():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("aluno@outrodominio.com.br", "extra")
    assert c.get_emails()['principal'] == Email('aluno@aluno.faculdadeimpacta.com.br')
    assert c.get_emails()['particular'] == Email('aluno@gmail.com')
    assert c.get_emails()['extra'] == Email('aluno@outrodominio.com.br')


def test_adiciona_outro_email_como_principal():
    c = Contato("Funcionario", "1199999-9999", "funcionario@secretaria.faculdadeimpacta.com.br")
    assert c.get_emails()['principal'] == Email("funcionario@secretaria.faculdadeimpacta.com.br")
    try:
        c.adiciona_email("funcionario@tutoria.faculdadeimpacta.com.br")
    except ValueError:
        pass
    assert c.get_emails()['principal'] == Email("funcionario@tutoria.faculdadeimpacta.com.br")


def test_adiciona_email_invalido_1():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    emails = [
        '',
        # "aluno 1@impacta.com.br",
        "amauri@@impacta.com.br",
        # "amauri..impacta.com.br",
        "amauriimpacta.com.br",
        "amauri_giovani@impacta.com.br",
        # "am.au-ri@gm-ai.l",
        # "a@g",
        # "a@g.com.b",
        # "aluno@gmail.com.brasil",
        # "a@g.com",
        # "ama@uri@facul.edu",
        # "ama-uri@aluno.facul.",
        # "ama-uri.giova-ni333@aluno.facul",
        #"ama-uri.giova-ni333@.br",
        # "@amauriimpacta.com.br",
        # "amauriimpacta@.com.br",
        # "amauri@impacta@faculdade.com.br"
    ]
    for email in emails:
        try:
            c.adiciona_email(email)
        except ValueError:
            pass
        else:
            raise AssertionError('O email deve conter @ e domínio corretamente')
        assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")


def test_adiciona_email_invalido_2():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    for email in [123, 12.30]:
        try:
            c.adiciona_email(email)
        except TypeError:
            pass
        else:
            raise AssertionError('Email deve ser do tipo string')
        assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")


def test_apaga_telefone():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    c.apaga_telefone('fixo')
    c.apaga_telefone('celular')
    assert not any(['fixo' in c.get_telefones()])
    assert not any(['celular' in c.get_telefones()])
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")


def test_apaga_telefone_tipo_nao_existe():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    tipos = ['particular', '1198888-8888', 11988888888]
    for tipo in tipos:
        try:
            c.apaga_telefone(tipo)
        except KeyError:
            pass
        else:
            raise AssertionError("Não levantou erro para chave inexistente")
    assert c.get_telefones()['principal'] == TelefoneAtualizado("1199999-9999")
    assert c.get_telefones()['fixo'] == TelefoneAtualizado("113322-4567")
    assert c.get_telefones()['celular'] == TelefoneAtualizado("1198888-8888")


def test_apaga_email():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("nome@trabalho.com.br", "trabalho")
    c.apaga_email('particular')
    c.apaga_email('trabalho')
    assert not any(['particular' in c.get_emails()])
    assert not any(['trabalho' in c.get_emails()])
    assert c.get_emails() == {'principal': Email("aluno@aluno.faculdadeimpacta.com.br")}
    assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")


def test_apaga_email_tipo_nao_existe():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("nome@trabalho.com.br", "trabalho")
    tipos = ['faculdade', 'empresa', 11988888888, 'aluno@aluno.faculdadeimpacta.com.br']
    for tipo in tipos:
        try:
            c.apaga_email(tipo)
        except KeyError:
            pass
        else:
            raise AssertionError("Não levantou erro para chave inexistente")
    assert c.get_emails()['principal'] == Email("aluno@aluno.faculdadeimpacta.com.br")
    assert c.get_emails()['particular'] == Email("aluno@gmail.com")
    assert c.get_emails()['trabalho'] == Email("nome@trabalho.com.br")
    assert c.get_emails() == {'principal': Email("aluno@aluno.faculdadeimpacta.com.br"),
                              'particular': Email("aluno@gmail.com"),
                              'trabalho': Email("nome@trabalho.com.br")}


def test_get_telefones():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    assert c.get_telefones() == {'principal': TelefoneAtualizado('1199999-9999'),
                                 'fixo': TelefoneAtualizado('113322-4567'),
                                 'celular': TelefoneAtualizado('1198888-8888')}


def test_get_emails():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("aluno@outrodominio.com.br", "extra")
    assert c.get_emails() == {'principal': Email("aluno@aluno.faculdadeimpacta.com.br"),
                              'particular': Email("aluno@gmail.com"),
                              'extra': Email("aluno@outrodominio.com.br")}


def test_lista_telefones():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_telefone("113322-4567", "fixo")
    c.adiciona_telefone("1198888-8888", "celular")
    assert c.lista_telefones() == [('principal', TelefoneAtualizado('1199999-9999')),
                                 ('fixo', TelefoneAtualizado('113322-4567')),
                                 ('celular', TelefoneAtualizado('1198888-8888'))]


def test_lista_emails():
    c = Contato("Aluno", "1199999-9999", "aluno@aluno.faculdadeimpacta.com.br")
    c.adiciona_email("aluno@gmail.com", "particular")
    c.adiciona_email("aluno@outrodominio.com.br", "extra")
    assert c.lista_emails() == [('principal', Email("aluno@aluno.faculdadeimpacta.com.br")),
                               ('particular', Email("aluno@gmail.com")),
                                ('extra', Email("aluno@outrodominio.com.br"))]


def test_buscar():
    c1 = Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    c1.adiciona_telefone("111111-1111", "fixo")
    c1.adiciona_telefone("1191111-1111", "celular")
    c1.adiciona_email("aluno11@aluno.faculdadeimpacta.com.br", "email2")
    c1.adiciona_email("aluno111@aluno.faculdadeimpacta.com.br", "email3")
    assert c1.buscar("Alun") is True
    assert c1.buscar("1111") is True
    assert c1.buscar("@aluno") is True
    assert c1.buscar("234315435") is False


def test_create_dump():
    c1 = Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    c1.adiciona_telefone("111111-1111", "fixo")
    c1.adiciona_telefone("1191111-1111", "celular")
    c1.adiciona_email("aluno11@aluno.faculdadeimpacta.com.br", "email2")
    c1.adiciona_email("aluno111@aluno.faculdadeimpacta.com.br", "email3")
    c2 = Contato("Aluno2", "115222-2222", "aluno2@aluno.faculdadeimpacta.com.br")
    c2.adiciona_telefone("112222-2222", "fixo")
    c2.adiciona_telefone("1192222-2222", "celular")
    c2.adiciona_email("aluno22@aluno.faculdadeimpacta.com.br", "email2")
    c2.adiciona_email("aluno222@aluno.faculdadeimpacta.com.br", "email3")
    c3 = Contato("Aluno3", "115333-3333", "aluno3@aluno.faculdadeimpacta.com.br")
    c3.adiciona_telefone("113333-3333", "fixo")
    c3.adiciona_telefone("1193333-3333", "celular")
    c3.adiciona_email("aluno33@aluno.faculdadeimpacta.com.br", "email2")
    c3.adiciona_email("aluno333@aluno.faculdadeimpacta.com.br", "email3")
    for c in [c1, c2, c3]:
        assert c.create_dump() == {
            'nome': c.nome,
            'telefones': c.get_telefones(),
            'emails': c.get_emails()
        }

def test__repr__():
    c = Contato("Aluno1", "115111-1111", "aluno1@aluno.faculdadeimpacta.com.br")
    assert c.__repr__() == '<Contato: Aluno1>'
