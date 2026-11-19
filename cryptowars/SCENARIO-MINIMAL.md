# Scénario jouable minimal (stub)

## Objectif
Permettre de démarrer une bataille simple avec les champions TON et BTC une fois le mod chargé dans VCMI.

## Unités
- TON Champion (id: tonChampion) : attaque 12, défense 10, PV 60, dégâts 10-15, vitesse 8
- BTC Champion (id: btcChampion) : attaque 13, défense 14, PV 80, dégâts 12-17, vitesse 5

## Scénario proposé
Bataille 1v1 ou équipes :
- Équipe 1 : 5x TON Champion
- Équipe 2 : 4x BTC Champion
- Victoire : éliminer l'adversaire

## Comment tester (une fois l'environnement disponible)
1. Compiler VCMI avec le mod CryptoWars activé (Mods/cryptowars/mod.json, keepDisabled=false).
2. Lancer le client, activer le mod dans le launcher si nécessaire.
3. Démarrer une bataille personnalisée ou utiliser un map editor pour placer les unités.
4. Vérifier que les icônes portraits s'affichent et que les stats sont correctes.

## Tests restants (SDK Android / build complet manquant)
- Compilation Android (prioritaire) : nécessite Android SDK, NDK, CMake, Conan.
- Extraction des frames d'animation depuis les GIF/WebP (voir tools/extract_frames.py).
- Génération des .def ou JSON animations pour les groupes de combat.
- Validation in-engine : chargement du mod, rendu des portraits, bataille jouable jusqu'au bout sans crash.
- Tests sur device Android réel ou émulateur.

Branche : mission/001-cryptowars-minimal (dérivée de mission/001-cryptowars @ a6436993022b320544f6f371af8d3b4d9ce94d9f)
