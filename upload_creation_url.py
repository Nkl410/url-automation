import openpyxl
from openpyxl.drawing.image import Image
import os
from PIL import Image as PILImage
import io

def extract_images_from_excel(file_path, output_folder):
    """
    Extrait les images d'un fichier Excel et les enregistre dans un dossier spécifique.
    :param file_path: Chemin du fichier Excel
    :param output_folder: Dossier où enregistrer les images
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    wb = openpyxl.load_workbook(file_path, data_only=True)
    image_found = False
    
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        image_count = 1
        
        if not hasattr(sheet, '_images') or not sheet._images:
            print(f"Aucune image trouvée dans la feuille : {sheet_name}")
            continue
        
        for image in sheet._images:
            img_path = os.path.join(output_folder, f"{sheet_name}_image_{image_count}.png")
            
            if hasattr(image, 'ref') and image.ref is not None:
                img_bytes = io.BytesIO(image._image)
                img = PILImage.open(img_bytes)
                img.save(img_path)
                print(f"Image enregistrée : {img_path}")
                image_found = True
            else:
                print(f"Problème avec l'image dans la feuille {sheet_name}")
            
            image_count += 1
    
    if not image_found:
        print("Aucune image n'a été extraite. Vérifiez que votre fichier Excel contient bien des images insérées en tant qu'objets.")
    else:
        print(f"Extraction terminée. Images enregistrées dans {output_folder}")

# Exemple d'utilisation
if __name__ == "__main__":
    fichier_excel = "/Users/nikolavucic/Documents/URL/Template_Listing_url.xlsx"  # Remplacez par le chemin du fichier Excel
    dossier_sortie = "images_extraitees"  # Nom du dossier de sortie
    extract_images_from_excel(fichier_excel, dossier_sortie)
