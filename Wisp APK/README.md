# Wisp (APK)

APK de base inchangé (VPN, interface, code) — seul `assets/hosts.txt` est remplacé par `app/hosts.txt`
(233 → 910 domaines bloqués), puis l'APK est aligné et signé par GitHub Actions.

- `app/hosts.txt` : liste complète des domaines bloqués (format `0.0.0.0 domaine`)
- `app/hosts-added.txt` : les 677 domaines ajoutés par rapport à l'APK d'origine
- `base/Wisp-base.apk` : APK d'origine (non modifié)
- `.github/workflows/main.yml` : build + signature

## Utilisation
1. Modifier `app/hosts.txt`, commit, push → le workflow construit l'APK.
2. Récupérer `Wisp.apk` dans l'onglet *Actions* (artifact) ou *Releases* (tag `latest`).

## Signature
Par défaut une clé de test (`keystore/wisp.keystore`) est utilisée. Pour une clé privée, ajoutez les secrets
`KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`. Changer de clé oblige à désinstaller l'ancienne version avant d'installer.

## Exclus volontairement du blocage DNS
`s.youtube.com`, `redirector.googlevideo.com`, `youtubei.googleapis.com`, `graph.facebook.com`, `graph.instagram.com`, `i.instagram.com`, `d.reddit.com`
(ils casseraient YouTube, Instagram, Facebook et Reddit sur tout le téléphone).
