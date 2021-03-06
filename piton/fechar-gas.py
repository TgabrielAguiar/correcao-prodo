import shutil
import os

os.system("taskkill /im Retaguarda.exe")
os.system("taskkill /im backup.exe")
shutil.move('C:\ERP\Dados\DADOS.FDB', 'C:\ERP\Dados\gas')
quit()
