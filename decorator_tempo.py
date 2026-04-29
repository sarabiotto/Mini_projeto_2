import time
import logging
import functools

logging.basicConfig(
    filename='execucao.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def medir_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        duracao = fim - inicio
        mensagem = f'{func.__name__} executou em {duracao:.4f} segundos'
        logging.info(mensagem)
        print(mensagem)
        return resultado
    return wrapper