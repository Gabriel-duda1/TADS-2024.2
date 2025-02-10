import pandas as pd

#Assim se cria uma tabela
tabela = pd.DataFrame({
    'Nome': ['Renata' , 'Anderson' , 'Paulo' ],
    'Nota': [10, 5, 5],
    'Nota2': [7, 3, 6],
})
#Selecionar as colunas ou mudar 
tabela[['Nome', 'Nota', 'Nota2',]]

tabela.query('Nota > 7')

tabela.query('Nome == "Renata"')
tabela.query('Nome in ("Renata", "paulo")')

tabela \
  .query('Nota > 7')


  #criando colunas
tabela \
  .assign (
    media = lambda x: (x['Nota2'])/2
  )