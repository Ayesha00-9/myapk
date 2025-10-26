[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3==3.10.8, kivy==2.3.0, cython==0.29.36, pyjnius==1.5.0
orientation = portrait
osx.python_version = 3
fullscreen = 0

# Important: use android.archs, not android.arch
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0

[app]
# Optional: to include main.py
main = main.py
