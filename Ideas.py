try:
    b = ''
    a = '10'*b
except ZeroDivisionError as eror:
    print(f'Tentou dividir por zero <{eror.__class__.__name__}>')
except Exception:
    raise

