//npm install @faker-js/faker --save-dev  >> dependencias gerar nomes aleatorios
describe('Teste completo Mercado1', () => {
  it('Testa login errado e certo, clientes, produtos, vendas e logout', () => {
    cy.visit('https://sistema-3-estoque.netlify.app');
    const objetos = [
      {nome:"lapiz", categoria:"papelaria", quantidade:"6", preco:"5"},
      {nome:"abacaxi", categoria:"fruta", quantidade:"3", preco:"75"},
      {nome:"mouse", categoria:"periferico", quantidade:"2", preco:"5"},
      {nome:"cama", categoria:"casa", quantidade:"10", preco:"105"},
      {nome:"teclado", categoria:"periferico", quantidade:"3", preco:"125"},
      {nome:"pc", categoria:"Pc", quantidade:"600", preco:"1005"},
      {nome:"tv", categoria:"casa", quantidade:"10", preco:"20005"},
      {nome:"coca-cola", categoria:"refri", quantidade:"620", preco:"105"},
      {nome:"mochila", categoria:"uniforme", quantidade:"12", preco:"395"},
      {nome:"casa", categoria:"casa", quantidade:"2", preco:"100000"},
    ]

    cy.wait(1000)
    for (let index = 0; index < 10; index++) {
      cy.get("#nome-produto").type(objetos[index].nome)
      cy.wait(1000)
      cy.get("#categoria-produto").type(objetos[index].categoria)
      cy.wait(1000)
      cy.get("#quantidade-produto").type(objetos[index].quantidade)
      cy.wait(1000)
      cy.get("#preco-produto").type(objetos[index].preco)
      cy.wait(1000)
      cy.get("#btn-cadastrar").click()
    }
        cy.wait(1000)
        cy.screenshot("print-atv3")
  });
});
