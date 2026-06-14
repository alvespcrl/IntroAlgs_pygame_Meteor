from src.dados import carregar_recorde, salvar_recorde
from src.config import CAMINHO_RECORDE

recorde = carregar_recorde(CAMINHO_RECORDE)
print("Recorde atual:", recorde)

salvar_recorde(CAMINHO_RECORDE, recorde + 10)

print("Novo recorde:", carregar_recorde(CAMINHO_RECORDE))