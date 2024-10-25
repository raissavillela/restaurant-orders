# Projeto Restaurant Orders

A partir de uma estrutura inicial foi finalizada uma ferramenta de construção de cadápios para um restaurante.
Ao longo deste projeto fui responsável por:

  * Construir testes para classes já implementadas;

  * Implementar uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades);

  * Implementar uma classe que gerará os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento;
  
  * Implementar uma classe que faz a gestão de estoque dos ingredientes.
    

##  Neste projeto, atestei que sou capaz de:
  
  * Praticar o conceito de Hashmaps através das estruturas de dados Dict e Set do Python;

  * Praticar os conhecimentos de testes de software;

  * Praticar os conhecimentos de orientação a objetos.

  Para garantir a qualidade do código, utilizei os linters `ESLint` e `StyleLint`.


## Orientações
  <details>
  <summary><strong>Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**
  
  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary>
    <b>Como rodar a aplicação?</b>
  </summary>

Para ver a aplicação rodando com as funcionalidades implementadas, use o comando a seguir:

```bash
python3 -m uvicorn app:app
```

Acesse a rota `/docs` para ver a [documentação](http://127.0.0.1:8000/docs) gerada pelo FastAPI!

</details> 


# Requisitos
  * Implemente testes para a classe Ingredient.
  
  * Implemente testes para a classe Dish.
  
  * Implemente a classe MenuData que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado.
  
  * Implemente o método get_main_menu dentro da classe MenuBuilder. 
  
  * Implemente os métodos check_recipe_availability e consume_recipe dentro da classe InventoryMapping.

  * Implemente do método get_main_menu considerando também a disponibilidade em estoque dos ingredientes dos pratos.

# O que já veio pronto da Trybe
   * A implementação de algumas das classes que foram usadas ao longo do seu desenvolvimento.

   * Arquivos csv de Gestão de Receitas e Estoque.
  
   * Testes feitos pela Trybe para avaliar se o meu teste passa conforme o objetivo proposto, e confirmar que meu teste falha em alguns casos em que deveria falhar.


Projeto desenvolvido durante a Formação em Desenvolvimento Web Full-Stack da [Trybe](https://www.betrybe.com/). 
Todos os arquivos de configuração, banco de dados e estrutura são de autoria da Trybe.
