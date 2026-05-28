//npm install @faker-js/faker --save-dev  >> dependencias gerar nomes aleatorios
describe('Teste completo Mercado1', () => {
  it('Testa login errado e certo, clientes, produtos, vendas e logout', () => {
    cy.visit('https://sistema-4-urna.netlify.app/');
    cy.wait(1000)
    cy.get('[onclick="clicar(6)"]').click()
    cy.wait(1000)
    cy.get('[onclick="clicar(7)"]').click()
    cy.wait(1000)
    cy.get('.btn-confirma').click()
    cy.wait(1000)
    cy.screenshot('print-tela_atv4')
    cy.wait(5000)
  });
});
