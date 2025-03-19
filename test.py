from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# 1️⃣ Authentification
gauth = GoogleAuth()

# Charger le fichier credentials.json
gauth.LoadClientConfigFile("credentials.json")

# Authentification via le navigateur
gauth.LocalWebserverAuth()  # Cela ouvre un navigateur pour se connecter à ton compte Google

# Sauvegarder les credentials pour les prochaines exécutions
gauth.SaveCredentialsFile("mycreds.txt")

# 2️⃣ Initialiser Google Drive
drive = GoogleDrive(gauth)

# Vérifier la connexion : lister les fichiers dans le Drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    print(f"Nom : {file['title']} | ID : {file['id']}")
