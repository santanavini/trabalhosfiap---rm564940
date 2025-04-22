

#RyanCarlos_RM561677_fase2_cap7
#ThyagoPaiva_RM562049_fase2_cap7
#ViniciusSantana_RM564940_fase2_cap7
#VitorGuisso_RM562317_fase2_cap7


# Pacores necessários
if (!require(ggplot2)) install.packages("ggplot2", dependencies = TRUE)
if (!require(scales)) install.packages("scales", dependencies = TRUE)

# Carregar os pacotes
library(ggplot2)
library(scales)


# Para essa atividade, vamos utilizar a variável: Valor da produção

# Vetor com os valores da produção
valor_producao <- c(
  605000, 4800000, 13445000, 12694000, 142000, 869000, 1035000, 6119000, 4360000,
  339000, 7297000, 511000, 361000, 19154000, 7131000, 2552000, 483000, 2239000, 
  40000, 29397000, 17160000, 8640000, 7184000, 256000, 20700000, 1047000, 316000, 
  356000, 3343000, 126768000, 15515000, 90011000, 17152000, 8545000, 2394000, 
  1400000, 70890000, 1526000, 74644000, 1469000, 292000, 74499000, 679000, 
  29221000, 283000, 159000, 3574000, 2719000, 1204000
)

# Medidas de Tendência Central
media <- mean(valor_producao)
mediana <- median(valor_producao)
moda <- as.numeric(names(sort(table(valor_producao), decreasing = TRUE)[1]))

# Medidas de Dispersão
amplitude <- max(valor_producao) - min(valor_producao)
desvio_medio <- mean(abs(valor_producao - mean(valor_producao)))
desvio_padrão <- sd(valor_producao)
variancia <- var(valor_producao)

# Medidas Separatrizes
quartis <- quantile(valor_producao)
decis <- quantile(valor_producao, probs = seq(0.1, 0.9, by = 0.1))
percentis <- quantile(valor_producao, probs = seq(0.01, 0.99, by = 0.01))

# Função para formatar valores em R$
f_real <- function(x) format(x, big.mark = ".", decimal.mark = ",", nsmall = 2)

# Resultados
cat("MEDIDAS DE TENDÊNCIA CENTRAL\n")
cat("Média: R$", f_real(media), "\n")
cat("Mediana: R$", f_real(mediana), "\n")
cat("Moda: R$", f_real(moda), "\n\n")

cat("MEDIDAS DE DISPERSÃO\n")
cat("Amplitude: R$", f_real(amplitude), "\n")
cat("Desvio Médio: R$", f_real(desvio_medio), "\n")
cat("Desvio Padrão: R$", f_real(desvio_padrão), "\n")
cat("Variância: R$", f_real(variancia), "\n\n")

cat("MEDIDAS SEPARATRIZES\n")
cat("Quartis:\n"); print(f_real(quartis))
cat("Decis:\n"); print(f_real(decis))
cat("Percentis:\n"); print(f_real(percentis))


# Análise gráfica quantitativa


faixa_valor <- cut(
  valor_producao,
  breaks = c(0, 250000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 100000000, 150000000),
  labels = c(
    "Até 250 mil",
    "250 mil a 500 mil",
    "500 mil a 1 mi",
    "1 mi a 2 mi",
    "2 mi a 5 mi",
    "5 mi a 10 mi",
    "10 mi a 20 mi",
    "20 mi a 50 mi",
    "50 mi a 100 mi",
    "Acima de 100 mi"
  ),
  include.lowest = TRUE
)

# Gerar o gráfico de barras
ggplot(data.frame(faixa_valor), aes(x = faixa_valor)) +
  geom_bar(fill = "purple") +
  labs(
    title = "Distribuição por Faixas de Valor da Produção",
    x = "Faixa de Valor da Produção",
    y = "Frequência"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))



# Análise gráfica qualitativa

# Vetor com a classificação do valor produzido

classificacao <- c(
  "Pequeno", "Pequeno", "Médio", "Médio", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Pequeno",
  "Pequeno", "Pequeno", "Pequeno", "Médio", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Médio",
  "Médio", "Pequeno", "Pequeno", "Pequeno", "Médio", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Grande",
  "Médio", "Grande", "Médio", "Pequeno", "Pequeno", "Pequeno", "Grande", "Pequeno", "Grande", "Pequeno",
  "Pequeno", "Grande", "Pequeno", "Médio", "Pequeno", "Pequeno", "Pequeno", "Pequeno", "Pequeno"
)

# Criando um dataframe
df_classificacao <- data.frame(Classificacao = classificacao)

# Gráfico de barras da variável qualitativa
ggplot(df_classificacao, aes(x = Classificacao)) +
  geom_bar(fill = "steelblue") +
  labs(
    title = "Distribuição da Classificação do Valor Produzido",
    x = "Classificação",
    y = "Frequência"
  ) +
  theme_minimal()


