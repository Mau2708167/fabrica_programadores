programa {
  funcao inicio() {
    //declarando as variaveis
  real peso,altura,imc
  cadeia nome
  escreva ("digite seu nome:")
  leia(nome) 
  escreva ("digite seu peso:")
  leia(peso)
  escreva("digite sua altura:")
  leia(altura)
  // não esquecer de colocar a multiplicaçao
  // entre parênteses  (altura * altura)
  imc = peso/ (altura*altura)
  escreva("---bem vindo---",nome) 
  escreva("no resultado de sua imc é:", imc)
  
  

  
  }
}
