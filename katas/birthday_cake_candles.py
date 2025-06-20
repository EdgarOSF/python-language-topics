candles = [3, 2, 1, 3]

def birthdayCakeCandles(candles):
    max_candle = max(candles)
    candles_count = 0
    
    for i in candles:
        if max_candle == i:
            candles_count += 1

    print(candles_count)

birthdayCakeCandles(candles)