# M5 - BandKamp Generic View

## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```


## Execução dos testes:

Como este projeto se trata de uma refatoração, não terá divisão de testes por tarefa, pois o objetivo é que todos os testes continuem passando após a refatoração.
Deste modo, para rodar a bateria de todos os testes, utilize:
```shell
pytest --testdox -vvs
```
---

Caso você tenha interesse em rodar apenas um diretório de testes específico, utilize os comandos abaixo:

Users:
```python
pytest --testdox -vvs tests/users/
```

Albums:
```python
pytest --testdox -vvs tests/albums/
```

Songs:
```python
pytest --testdox -vvs tests/songs/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/users/test_login_view.py::UserLoginViewTest::test_user_login_without_required_fields
```