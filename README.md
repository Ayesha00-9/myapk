# PasswordEstimator APK Build Repo (template)

This repository contains your original Python script (`password_bruteforce.py`) and a minimal `main.py` launcher,
plus a `buildozer.spec` and a GitHub Actions workflow (`.github/workflows/build.yml`) that attempts to build an APK
using Buildozer on GitHub Actions.

How to use (minimal steps):
1. Unzip this repository and push it to a **new GitHub repository** (create one on github.com).
2. Make sure Actions are enabled for the repo (they are enabled by default for new repos).
3. Push to `main` (or `master`) branch to trigger the workflow, or go to the Actions tab and `Run workflow` manually.
4. If the build succeeds, download the APK from the workflow artifacts (Actions -> specific run -> Artifacts -> apk-artifacts).

Important notes and caveats:
- I cannot build the APK here — you must push this repo to GitHub to run the cloud build.
- Building Android APKs in CI can be fragile: Buildozer may attempt to download Android SDK components and can time out.
- The workflow provided is a minimal template and may need extra packages or adjustments for a successful build.
- Your original `password_bruteforce.py` is NOT modified in this repo.
