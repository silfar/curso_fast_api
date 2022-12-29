from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha:str) -> bool:    
    """
    Fun��o para verificar a senha est� correta, comparando a senha 
    em texto puro, informada pelo usu�rio, e o hash da senha que 
    estar� salvo no banco de dados durante a cria��o da conta 
    
    """
    
    return CRIPTO.verify(senha,hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
        Fun��o que gera e retorna o hash da senha 
    """
    return CRIPTO.hash(senha)
