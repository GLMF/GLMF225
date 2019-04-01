# Sécurisez vos noms de domaine avec DNSSEC
par Christophe BORELLY [Professeur de l'ENSAM – IUT de Béziers]

---

Le service DNS (Domain Name System) est depuis les années 1980 un des composants essentiel du fonctionnement d’internet car il permet notamment la conversion d’un nom de domaine en adresse IP (et l’inverse également). Il a été la cible de plusieurs attaques comme l’usurpation d’identité DNS (DNS ID Spoofing [1]) et la pollution de cache (DNS cache poisoning [1][2]). Avec la mise en place d’une zone racine « signée » en janvier 2010 [3], il est désormais possible de vérifier les données reçues par le système DNS en activant DNSSEC (Domain Name System Security Extensions) [4]. Je vous propose donc de voir comment mettre en œuvre tout cela. 
