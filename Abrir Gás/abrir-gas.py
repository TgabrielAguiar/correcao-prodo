import shutil
import os

shutil.move('C:\ERP\Dados\gas\DADOS.FDB', 'C:\ERP\Dados')
os.system('C:\ERP\Retaguarda.exe')
os.system("taskkill /im Retaguarda.exe")
os.system("taskkill /im backup.exe")
shutil.move('C:\ERP\Dados\DADOS.FDB', 'C:\ERP\Dados\gas')
quit()
