# HAI927I - Christal

## Présentation du projet 💻

* [Pourquoi nous ?](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Pr%C3%A9sentations/HAI927I%20-%20Choix%20sujet%20-%20D%C3%A9bruitage.pdf)

## Comptes rendus 📝
* [Compte rendu n°1](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR1.pdf)
* [Compte rendu n°2](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR2.pdf)
* [Compte rendu n°3](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR3.pdf)
* [Compte rendu n°4](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR4.pdf)
* [Compte rendu n°5](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR5.pdf)
* [Compte rendu n°6](https://github.com/Christinamrn/HAI927I-Christal/blob/main/Comptes%20Rendus/%5BHAI927I%5D%20Christal%20-%20CR6.pdf)

## Fonctionnement du git ⚙️
Voici comment est organisé le projet avec ses différents dossiers :

* 📁 **imgtest**  regroupe une sélection d'images que l'on souhaite tester pour lesquelles aucun traitement n'a été effectué.

* 📁 **gen_noise** regroupe différents générateurs de bruit artificiel. 

* 📁 **imgoutnoised**  regroupe les images résultantes des générateurs du dossier gen_noise.

* 📁 **filters** regroupe différents filtres à tester.

* 📁 **imgoutdenoised** regroupe les images résultantes du débruitage.

* 📁 **metrics** regroupe les fonctions calculant les métriques.

## Application Qt 💻
* 📁 **QtChristalApp** est le dossier contenant l'application en cours de développement. Celle-ci reprend les concepts vu précédemment ainsi que les prochains ajouts sur une interface graphique. Celle-ci est destinée à un utilisateur lambda qui souhaiterait débruiter son image simplement par le biais de notre application. Nous utilisons QtCreator en version Python (QtPy).

## Efficient Poisson Denoising for Photography
Nous avons implémenté le papier [(lien)](https://ieeexplore.ieee.org/document/5414042) dans notre code.


## MPRNet 🌐
Multi-Stage Progressive Image Restoration (CVPR 2021) *Syed Waqas Zamir, Aditya Arora, Salman Khan,Munawar Hayat, Fahad Shahbaz Khan, Ming-Hsuan Yang and Ling Shao* [Paper](https://arxiv.org/pdf/2102.02808.pdf)  | [Code](https://github.com/swz30/MPRNet)

Nous utilisons MPRNet dans notre code avec les modèles pré-entraînés disponibles sur le github mentionné.
