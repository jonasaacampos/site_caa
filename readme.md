### Iniciando django

```bash
django-admin startproject app .

#iniciar servidor
python manage.py runserver

# criar apps
python manage.py startapp nome_app

# usar app após criação
# alterar arquivo settings.py

# gera o script do banco de dados
python manage.py makemigrations

# executa as queries para o banco de dados.
python manage.py migrate

# criar superuser
python manage.py createsuperuser


```

Sequencia de criação

1. Models
   1. Criar classe
2. Admin
   1. Criar classe
   2. registrar admin


### Chaves ssh git hub

- [Gerando uma nova chave SSH e adicionando-a ao agente SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- Copiar a chave (git bash > `cat git.pub` ou `clip < git.pub`)
- [Settings > SSH Keys](https://github.com/settings/keys)

### Documentation

- `:notebook: doc: documentação`
- `:star: feat: describe feat...`
- `:recycle: refatc: ...`

parei #A027
