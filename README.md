# GenForm

Ce projet est conçu pour générer des formulaires synthétiques destinés à l'entraînement et au test de modèles d'apprentissage automatique. Les formulaires synthétiques imitent les formulaires réels avec des en-têtes, des champs de texte et des données aléatoires. Ce README fournit des instructions sur la configuration et l'utilisation du générateur de formulaires synthétiques.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.6 ou supérieur


## Installation

1. **Cloner le dépôt :**
   git clone <url-du-dépôt>
   

2. **Installer les packages requis :**

   - PyTorch ```bash python3 pip install torch```

   - Scikit-Image ```bash python3 pip install scikit-image```

   - Transformers ```bash python3 pip install transformers```

   - Datasets ```bash python3 pip install datasets```

   - Matplotlib ```bash python3 install matplotlib```

   - Wget ```bash python3 install wget```


3. **Récupérer des polices d'écriture**

   Peut être fait :
   - Soit manuellement : Récupérer des polices d'écritures, les déplacer dans data/fonts, utiliser ```bash ls data/fonts > data/fonts/fonts.list``` puis clean_fonts.py ;

   - Soit en utilisant le script scrape.sh qui récupère des les polices libres pour une utilisation commerciale du site 1001fonts.com :
   ```bash
   bash synthetic_text_gen/scrape.sh
   ```
   Il peut être nécessaire de trier certaines polices trop illisibles si ce script est utilisé ;

   - Soit, pour automatiser le nettoyage des polices illisibles (nécessite Tesseract) :
   ```bash
   pip install pytesseract
   pip install editdistance
   bash synthetic_text_gen/scrape_clean.sh
   ```

4. **Générer `gpt2_form_generation.json` en utilisant GPT-2 :**

   - Utilisez le script `gpt_form.py` pour générer le fichier `gpt2_form_generation.json`.

   - Placez le fichier généré dans le répertoire `data` :
     ```bash
     mv gpt2_form_generation.json ./data/gpt2_form_generation.json
     ```


Structure du Répertoire

Assurez-vous que votre répertoire de projet est structuré comme suit :

```
<répertoire-du-dépôt>/
├── data/
│   ├── fonts/
│   │   └── clean-fonts.csv
│   └── gpt2_form_generation.json
├── synth_form_dataset.py
├── genForm.py
├── other files...
├── gpt_form.py
└── README.md
```


## Exécution du Générateur :

Exécutez le script de génération de formulaires synthétiques pour générer les formulaires et les enregistrer dans le répertoire spécifié :
```bash
python genForm.py [Nombre d'échantillons à générer : 100] [Ecrire les images sur le disque : True] [Ecrire les images dont un json ne peut pas être généré : False] [dossier de données : ./data] [Utiliser des masques : True]

```

Note: Assurez-vous que les chemins dans la configuration sont correctement définis selon la structure de votre répertoire de projet


## Paramètres de configuration

Grâce au paramètre "config" que prend le constructeur de la class SynthFormDataset (dans genForm.py) il est possible de modifier les formulaires générés.

'image_size'											default none		// Taille de l'image
'min_text_height'						 			default 8  			// Taille minimale du texte
'max_text_height'						 			default 32 			// Taille maximale du texte
'tables' 													default 0.2 		// Probabilité d'ajout d'un tableau dans le formulaire
'augmentation' 										default none		// Aucun effet
'augment_shade' 									default 1 			// Ajouter des distorsions de contraste/luminosité
'additional_aug_params'						default {}			// Autres paramètres de distorsion
'batch_size'		  						    						    // Inutile (neutralisé)
'questions'												default 1				// Nombre de paires question/réponse. Forcé à 1 si do_masks
'do_masks'												default 1				// Utiliser des masques ou non.
'max_qa_len_in' 									default = none 	// Longueur maximum des questions
'max_qa_len_out' 									default = none 	// Longueur maximum des réponses
'max_qa_len'											    						// Remplace les max_qa_len_in et max_qa_len_out s'ils ne sont pas définis
'cased'														default True		// Autoriser la capitalisation pour les questions/réponses
'color'														default False		// Autoriser la couleur dans les images générées (pas implémenté)
'rotation'																				// Inutilisé
'crop_params'											default none		// Paramètres des transformations de l'image générée
'rescale_range'																		// Intervalle de redimensionnement si la valeur n'est pas donnée explicitement
'rescale_to_crop_size_first'			default False		// Explicite
'rescale_to_crop_width_first'			default False		// Explicite
'rescale_to_crop_height_first'		default False		// Explicite
'cache_resized_images'						default False		// Mettre les images redimensionnées en cache
'crop_to_q'												default False		// Inutilisé avec ce dataset
'words'														default True		// ?
'use_json'												default False		// Niveau d'utilisation du json GPT-2. False, 'test', 'only', 'fine-tune', 'streamlined', 'readtoo', 'readmore' or 'readevenmore'
'shorten_text_in_json'						default False		// Explicite
'max_q_tokens'										default 20			// Longueur max des tokens pour les questions
'max_a_tokens'										default 800			// Longueur max des tokens pour les réponses

Autre paramètres inutilisés.

## Crédits

Nous remercions MM. Brian Davis, Bryan Morse, Bryan Price, Chris Tensmeyer, Curtis Wigington et Vlad Morariu pour Dessurt (https://github.com/herobd/dessurt) et SyntheticTextGen (https://github.com/herobd/synthetic_text_gen/tree/master) dont cet outil est une adaptation directe.
