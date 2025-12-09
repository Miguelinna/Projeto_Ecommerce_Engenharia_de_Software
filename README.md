# Projeto_Ecommerce_Engenharia_de_Software

---

# 📘 Descrição do Projeto de Engenharia de Software  
**Título:** Construindo um Sistema de E-commerce com Design Top-Down e Funções  

## 🎯 Objetivo  
O projeto tem como finalidade desenvolver um sistema de e-commerce simplificado, aplicando conceitos de **Design Top-Down** e **programação estruturada em funções/classes**. A ideia é simular o fluxo completo de uma compra online, desde o cadastro do cliente até a finalização do pedido, garantindo clareza nos requisitos e testes automatizados.  

  
# 👥 Histórias de Usuário 
## 🧪 Cenários de Utilização e Testes com Gherkin
Agora, vamos detalhar cada História de Usuário com cenários específicos usando a linguagem Gherkin (Dado, Quando, Então). Isso nos ajuda a esclarecer os requisitos e serve como base para os testes de um Analista de Qualidade (QA).
Funcionalidade: Realizar uma compra sem um sistema on-line

HU-1:  Escolher a loja e realizar cadastro
    Cenário: Escolher a loja e fazer cadastro para realizar uma compra

  	Dado que o usuário escolheu e acessou a loja virtual.
Quando ele clica em "Criar conta" E preenche os campos obrigatórios com dados válidos E clica em "Cadastrar".
Então o sistema deve exibir a mensagem "Cadastro realizado com       sucesso" e o cliente deve ser redirecionado para a página inicial logado.
HU-2:  Escolher um produto
    Cenário: buscar produto desejado

Dado que o cliente está logado na loja virtual e está na página inicial.
Quando ele digita "Tênis Esportivo" no campo de busca e clica em um dos resultados exibidos.
Então o sistema deve redirecioná-lo para a página do produto.
HU-3: páginas dos produtos  
    Cenário: Página do produto

	Dado que o cliente está na página do produto
	Quando ele já escolheu o item desejado
Então o sistema exibe a descrição do produto, nome, preço e a imagem do item selecionado.

HU-4: carrinho
   Cenário: Visualizar carrinho e revisar itens

  	Dado que o cliente adicionou um ou mais produtos ao carrinho
  	Quando ele acessa a página do carrinho
  	Então o sistema deve exibir todos os produtos adicionados com:
	|  Nome   |   Quantidade   |   Preço Unitário   |  Subtotal  |
  	E o total da compra deve ser calculado corretamente.
  


HU-5: Forma de pagamentos
   Cenário: Selecionar forma de pagamento e finalizar compra

Dado que o cliente está na página do carrinho E clicou no botão "Finalizar compra".
Quando ele escolhe a forma de pagamento "Cartão de Crédito" e preenche os dados do cartão corretamente e confirma o pedido
Então o sistema deve exibir a mensagem "Compra realizada sucesso" e o pedido deve ser registrado com status "em processamento".
  

## 💻 Implementação em Python  
O sistema foi implementado em Python, utilizando **classes e funções** para organizar o código:  
- Classe `Roupa`: representa os produtos, com atributos como nome, tamanho, preço e estoque.  
- Classe `LojaRoupas`: gerencia o estoque, carrinho e fluxo de compra.  
- Funções principais: listar estoque, adicionar ao carrinho, visualizar carrinho e finalizar compra.  
- Interface simples via **menu interativo no terminal**, permitindo ao usuário navegar pelas opções.  

## 📊 Diagrama (Visão Geral)  
O diagrama do sistema pode ser representado como:  

```
Cliente → LojaRoupas → Estoque → Carrinho → Pagamento
```

- **Cliente**: interage com o sistema via menu.  
- **LojaRoupas**: núcleo da aplicação, controla estoque e carrinho.  
- **Estoque**: lista de produtos disponíveis.  
- **Carrinho**: itens escolhidos pelo cliente.  
- **Pagamento**: etapa final, onde o pedido é confirmado.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/e8116051-fd57-4dea-bd6d-b433ba8908b4" />



---
