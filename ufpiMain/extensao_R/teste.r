x <- 5

vetor_numeros <- c(1,2,3,4,5)
primeiro_vetor <- vetor_numeros[1]
media <- mean(vetor_numeros)

if (media > 5){
    mensagem <- "maior que 5"
}else{
    mensagem <- "menor que 5"
}

print(mensagem)