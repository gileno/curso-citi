# Curso CITI
Repositório para o curso ministrado na 26º Jornada de Cursos do CITI


## Links Python

- [Curso Gratuito de Python](http://pycursos.com/python-para-zumbis/)
- [Artigos sobre Python](http://www.gilenofilho.com.br/tags/python/)
- [Exercícios/Problems](http://dojopuzzles.com/)
- [métodos mágicos](http://www.rafekettler.com/magicmethods.html)

## Links Django

- [Como funciona o ORM do Django](http://www.gilenofilho.com.br/como-funciona-o-orm-do-django/)
- [Curso Gratuito de Django](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/)
- [Usar o Gmail para Enviar E-mail](https://gist.github.com/gileno/2821493)

## Projeto a ser desenvolvido

Criar um projeto para cadastro de cursos estilo MOOC. Cada curso terá as seguintes informações:

Curso
- Nome
- Slug
- Descrição
- Categoria (modelo abaixo)
- Data de início (campo opcional)
- Destaque (indica se o curso é destaque, opcional)
- Preço

Categoria
- Nome
- Slug

O projeto precisará implementar as seguintes páginas:

- Página inicial listando cursos em destaque (veja modelo acima)
- Página para exibir todos os cursos
- Página para exibir cursos de uma determinada categoria
- Página para envio de mensagem de contato
- Página para um determinado curso exibindo todas as informações dele (nome, descrição, preço…)
- Possibilidade de cadastro do Usuário (usando modelagem do próprio django ou a sua - custom user)
- Possibilidade do usuário fazer login
- Possibilidade do usuário se inscrever no curso via botão presente dentro da página do curso
- Página para exibir os cursos os quais o usuário está inscrito

Para criar as interfaces (html/css) pode utilizar qualquer framework, recomendo o bootstrap utilizado durante o curso.
