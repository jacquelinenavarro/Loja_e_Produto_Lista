produtos = []
funcionarios = []

def cadastrar_funcionario():
    cpf = input('CPF do funcionário: ')
    for f in funcionarios:
        if f[0] == cpf:
            print('CPF já cadastrado.')
            return
    nome = input('Nome do funcionário: ')
    sobrenome = input('Sobrenome do funcionário: ')
    data_nascimento = input('Data de nascimento do funcionário (dd/mm/aaaa): ')
    funcionarios.append((cpf, nome, sobrenome, data_nascimento))

def listar_funcionarios():
    for f in funcionarios:
        cpf, nome, sobrenome, data_nascimento = f
        print(f'CPF: {cpf}, Nome: {nome} {sobrenome}, Data de Nascimento: {data_nascimento}')

def deletar_funcionario():
    cpf_a_deletar = input('CPF do funcionário a ser deletado: ')
    for f in funcionarios:
        if f[0] == cpf_a_deletar:
            funcionarios.remove(f)
            print('Funcionário removido com sucesso.')
            return
    print('Funcionário não encontrado.')

def alterar_funcionario():
    cpf_a_alterar = input('CPF do funcionário a ser alterado: ')
    for i, f in enumerate(funcionarios):
        if f[0] == cpf_a_alterar:
            print('Digite os novos dados do funcionário')
            cpf = input('CPF do funcionário: ')
            nome = input('Nome do funcionário: ')
            sobrenome = input('Sobrenome do funcionário: ')
            data_nascimento = input('Data de nascimento do funcionário (dd/mm/aaaa): ')
            funcionarios[i] = (cpf, nome, sobrenome, data_nascimento)
            print('Funcionário alterado com sucesso.')
            return
    print('Funcionário não encontrado.')

def cadastrar_produto():
    codigo = input('Código do produto: ')
    for p in produtos:
        if p[0] == codigo:
            print('Código do produto já cadastrado.')
            return
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade em estoque: '))
    produtos.append((codigo, nome, preco, quantidade))

def listar_produtos():
    for p in produtos:
        codigo, nome, preco, quantidade = p
        print(f'Código: {codigo}, Nome: {nome}, Preço: R${preco:.2f}, Quantidade: {quantidade}')

def deletar_produto():
    codigo_a_deletar = input('Código do produto a ser deletado: ')
    for p in produtos:
        if p[0] == codigo_a_deletar:
            produtos.remove(p)
            print('Produto removido com sucesso.')
            return
    print('Produto não encontrado.')

def alterar_produto():
    codigo_a_alterar = input('Código do produto a ser alterado: ')
    for i, p in enumerate(produtos):
        if p[0] == codigo_a_alterar:
            print('Digite os novos dados do produto')
            codigo = input('Código do produto: ')
            nome = input('Nome do produto: ')
            preco = float(input('Preço do produto: '))
            quantidade = int(input('Quantidade em estoque: '))
            produtos[i] = (codigo, nome, preco, quantidade)
            print('Produto alterado com sucesso.')
            return
    print('Produto não encontrado.')

while True:
    op = input("Digite o módulo: (f)funcionário, (p)produto, (s)sair: ")

    if op == 's':
        print("Você saiu do sistema! ")
        break

    elif op == 'f':
        op_funcionario = input('c - Cadastrar funcionário; l - Listar funcionários; d - Deletar funcionário; a - Alterar funcionário: ')

        if op_funcionario == 'c':
            cadastrar_funcionario()
        elif op_funcionario == 'l':
            listar_funcionarios()
        elif op_funcionario == 'd':
            deletar_funcionario()
        elif op_funcionario == 'a':
            alterar_funcionario()

    elif op == 'p':
        op_produto = input('c - Cadastrar produto; l - Listar produtos; d - Deletar produto; a - Alterar produto: ')

        if op_produto == 'c':
            cadastrar_produto()
        elif op_produto == 'l':
            listar_produtos()
        elif op_produto == 'd':
            deletar_produto()
        elif op_produto == 'a':
            alterar_produto()
