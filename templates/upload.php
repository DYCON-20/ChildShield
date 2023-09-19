<?php
// Vérifie si un fichier a été téléchargé
if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
    $tempFile = $_FILES['file']['tmp_name'];
    $uploadDir = 'uploads/';
    
    // Assurez-vous que le répertoire d'upload existe
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }
    
    // Générez un nom de fichier unique pour éviter les conflits
    $uploadFile = $uploadDir . uniqid() . '_' . $_FILES['file']['name'];

    // Déplacez le fichier téléchargé vers le répertoire d'upload
    if (move_uploaded_file($tempFile, $uploadFile)) {
        echo 'L\'image a été téléchargée avec succès !';
    } else {
        echo 'Une erreur est survenue lors du téléchargement de l\'image.';
    }
} else {
    echo 'Aucun fichier n\'a été téléchargé ou une erreur est survenue.';
}
?>
