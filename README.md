# EnglishThesaurus

Este dicionário em inglês foi feito utilizando somente python, com um database vindo de um curso sobre python. [Course Link](https://www.udemy.com/course/the-python-mega-course/)

O código JSON funciona da seguinte maneira: O usuário digita a palavra desejada (em inglês) e o programa irá retornar a definição (caso exista no database JSON). Caso o usuário digite uma palavra errada, foi utilizado a biblioteca DIFFLIB, mais especificamente a função get_close_matches, para realizar uma "correção" da palavra digitada pelo usuário.

O código MySQL é um pouco mais simples, porém tem a melhoria de não necessitar de um arquivo JSON acompanhando-o, nesse caso utilizasse o database em um servido MySLQ, sendo que quando o usuário digita uma palavra na busca, é necessário realizar uma query no banco e assim trazer ela para o mesmo.