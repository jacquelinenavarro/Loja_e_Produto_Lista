# Projeto: Loja & Produtos 

## Curso Back-End com Python / Turma: 03

#### Aluna:  

- [x] Jacqueline Navarro  

#### Professor:  

- [x] André Ribeiro

#### Data prevista para entrega:  

- [x] 31/07/2024 

---

# Projeto nº 10: Loja e Produtos

## Projeto de Lógica de Programação com Python - Programação Estruturada
(Utilizando Listas)
---

### Requisitos solicitados:

- [x] Para cada objeto criar no mínimo dois dados.

Exemplo: Médico(nome, crm), Pacientes(nome, cpf)

- [x] O sistema deverá realizar operações de CRUD com programação estruturada.

---
### Detalhamento do Projeto

#### Descrição:

- [x] Uma loja vende vários produtos.
- [x] Cada produto é vendido por uma única loja.
- [x] Relação: Uma loja -> Muitos produtos

### Resumo descritivo do Projeto:

O código define duas listas, produtos e funcionarios, e algumas funções para gerenciar os funcionários e os produtos. 
Essas funções do sistema permitem a gestão básica de funcionários e produtos, incluindo cadastro, listagem, remoção e atualização de dados. São elas:

* cadastrar_funcionario(): Adiciona um novo funcionário à lista funcionarios, verificando se o CPF já está cadastrado.
* listar_funcionario(): Exibe todos os funcionários cadastrados com seus detalhes.
* deletar_funcionario(): Remove um funcionário da lista com base no CPF fornecido.
* alterar_funcionario(): Atualiza os dados de um funcionário existente, identificando-o pelo CPF.
* cadastrar_produto(): Adiciona um novo produto à lista produtos, verificando se o código do produto já está cadastrado.
* listar_produto(): Exibe todos os produtos cadastrados com seus detalhes.
* deletar_produto(): Remove um produto da lista com base no código do produto fornecido.
* alterar_produto(): Atualiza os dados de um produto existente, identificando-o pelo código do produto.