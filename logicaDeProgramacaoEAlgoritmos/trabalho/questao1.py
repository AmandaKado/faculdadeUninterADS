"""
QUESTÃO 1 de 4 - Conteúdo até Aula 03

Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app para uma empresa X que vende Planos de Saúde. Uma das
estratégias dessa empresa X é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo:

 Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100);
 Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100);
 Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100);
 Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100);
 Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100);
 Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100);

O valor mensal do plano é calculado da seguinte maneira:

𝐯𝐚𝐥𝐨𝐫𝐌𝐞𝐧𝐬𝐚𝐥 = 𝐯𝐚𝐥𝐨𝐫𝐁𝐚𝐬𝐞 ∗ 𝐩𝐨𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞𝐦
Exemplo: Se o valorBase informado for 100.00 e a idade for 45 anos (240% segundo a tabela acima)
𝐯𝐚𝐥𝐨𝐫𝐌𝐞𝐧𝐬𝐚𝐥 = 𝟏𝟎𝟎. 𝟎𝟎 ∗ (
𝟐𝟒𝟎
𝟏𝟎𝟎) = 𝑹$ 𝟐𝟒𝟎. 𝟎𝟎
Elabore um programa em Python que:

A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
Por exemplo: print(“Sistema desenvolvido por Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
B. Deve-se implementar o input do valorBase do plano e da idade do cliente [EXIGÊNCIA DE CÓDIGO 2 de 6];
C. Deve-se implementar as regras de valores conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO
3 de 6];
D. Deve-se implementar o valorMensal [EXIGÊNCIA DE CÓDIGO 4 de 6];
E. Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
F. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
G. Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
H. Deve-se apresentar na saída de console a utilização do sistema informando uma idade maior ou igual a 29 anos, apresentando na saída de console o

valorMensal do plano [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];

EXEMPLO DE SAÍDA DE CONSOLE:

Figura 1.1: Exemplo de saída de console que o aluno deve fazer. Em que se perguntar o valorBase do plano (pode ser qualquer valor) e a idade (maior ou igual a 29 anos

[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2]), e é apresentado o valorMensal.

"""