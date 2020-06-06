import requests as req

PngData = req.get("https://www.impacta.edu.br/themes/wc_agenciar3/images/logo.png").content

Arquivo = open("C:\\Temp\\ws_py\\aula10\\LogoImpacta.png","wb")
Arquivo.write(PngData)
Arquivo.close()