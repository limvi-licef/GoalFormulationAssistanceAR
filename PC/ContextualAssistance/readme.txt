1. Installation

	installation automatique a partir du script install_env.bat.
	Se placer avec la console Anaconda Prompt dans le dossier V1 puis lancer le script:
	>> (env_par_defaut) install.bat

	Pour faire la meme chose manuellement (si install.bat n'as pas marche ou que
	lors de l'execution il manque des packages:
	>> (env_par_defaut) conda create -n tf_env_proj tensorflow=2.0
	>> (env_par_defaut) conda activate tf_env_proj
	>> (tf_env_proj) pip install opencv-python OwlReady2

2. Lancement

	Toujours avec Anaconda Prompt. Sauf si la console precedente s'est fermee, l'environnement
	est correct et il suffit de taper:
	>> python main.py

	Si fermeture de la console, il faut reactiver l'environnement:
	>> (env_par_defaut) conda activate tf_env_proj