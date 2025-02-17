'''Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.'''

# Definizione di un numero in virgola mobile, dichiarianmo il valore di x
x= float(input(f"Benvenuto, inserisci il valore di x: "))

# Calcolianmo il reciproco valore di y tramite la asegunete formula:
y= 1/x

# Visualizzazione dei valori
print(f"Il valore di x è il seguente: {x} ")
print(f"il valore di y ovvero (1/x) è il seguente: {y}")

# Calcolo del prodotto tra x e y
prodotto = x * y
print(f"Prodotto tra x : {prodotto}")

# Sottrazione di x dal prodotto e visualizzazione del risultato
sottrazione = prodotto - 1.0
print(f"Sottrazione (prodotto - 1.0): {sottrazione}")
