import yfinance as yf
import pandas as pd

# Pobierz dane PKO i CDR
pko = yf.Ticker("PKO.WA").history(period="1mo")["Close"]
cdr = yf.Ticker("CDR.WA").history(period="1mo")["Close"]

df = pd.DataFrame({
    "PKO BP": pko,
    "CD Projekt": cdr
})

df.index = df.index.tz_convert(None)
df.index = df.index.date

print(df.tail(10))