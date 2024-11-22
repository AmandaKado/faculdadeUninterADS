"""

QUESTÃO 4 de 4 - Conteúdo até aula 06

Enunciado: Você e sua equipe de programadores foram contratados por uma pequena empresa para desenvolver um software de gerenciamento de Contatos
Comerciais. Este software deve ter o seguinte menu e opções:

    1) Cadastrar Contato
    2) Consultar Contato
    1. Consultar Todos
    2. Consultar por Id
    3. Consultar por Atividade
    4. Retornar ao menu
    3) Remover Contato
    4) Encerrar Programa

Elabore um programa em Python que:

    A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
    
        Por exemplo: print(“Bem vindos a lista de contatos do Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 8];
    
    B. Deve-se implementar uma lista com o nome de lista_contatos e a variável id_global com valor inicial igual ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8];
    
    C. Deve-se implementar uma função chamada cadastrar_contato(id) que recebe apenas id como parâmetro e que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
    
        a. Pergunta nome, atividade, telefone do contato;
        
        b. Armazena o id (este é fornecido via parâmetro da função), nome, atividade, telefone dentro de um dicionário;
        
        c. Copiar o dicionário para dentro da lista_contatos (utilizar o copy);
        
        D. Deve-se implementar uma função chamada consultar_contatos() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
    
            a. Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
    
                i. Se Consultar Todos, apresentar todos os contatos com todos os seus dados cadastrados;
                
                ii. Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o contato específico (apenas 1) com todos os seus dados cadastrados;
                
                iii. Se Consultar por Atividade, solicitar ao usuário que informe a atividade, e apresentar o(s) contato(s) que exercem aquela atividade com todos os seus dados cadastrados;
            
                iv. Se Retornar ao menu, deve-se retornar ao menu principal (return);
                
                v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
                
                vi. Enquanto o usuário não escolher a opção 4, o menu consultar contatos deve se repetir.
        
    E. Deve-se implementar uma função chamada remover_contato() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
    
        a. Deve-se pergunta pelo id do contato a ser removido;
        
        b. Remover o contato da lista_contatos;
        
        c. Se o id fornecido não for de um contato da lista, printar “Id inválido” e repetir a pergunta E.a.
        
    F. Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
    
        a. Deve-se pergunta qual opção deseja (1. Cadastrar Contato / 2. Consultar Contato / 3. Remover Contato / 4. Encerrar Programa):
            
            i. Se Cadastrar Contato, incrementar em um id_ global e em seguida, chamar a função cadastrar_contato (id_ global);
            
            ii. Se Consultar Contato, chamar função consultar_contato ();
            
            iii. Se Remover Contato, chamar função remover_ contato ();
            
            iv. Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
            
            v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a. vi. Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
    
    G. Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
    
    H. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
    
    I. Deve-se apresentar na saída de console um cadastro do seu contato da seguinte forma: para nome informe seu nome completo (não usar apelidos ou abreviações), para atividade informar como estudante, e para telefone informe sua RU. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
    
    J. Deve-se apresentar na saída de console um cadastro de mais 2 contatos com mesmo tipo de atividade (por exemplo: marceneiro, padeiro, pintor, pedreiro) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
    
    K. Deve-se apresentar na saída de console uma consulta de todos os contatos [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
    
    L. Deve-se apresentar na saída de console uma consulta por código (id) de um dos contados [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
    
    M. Deve-se apresentar na saída de console uma consulta por atividade em que 2 contatos exerçam a mesma atividade [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
    
    N. Deve-se apresentar na saída de console uma remoção de um dos contatos e em seguida de uma consulta de todos os contatos, provando que o contato foi removido [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];

"""

print("Bem vindos a lista de contatos da Amanda Mayumi Kado") #Print simples para mostrar quem desenvolveu o sistema
