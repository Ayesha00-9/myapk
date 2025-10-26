# small launcher that runs the original script without modifying it.
# Buildozer expects a main.py entry point; this keeps your original file intact.
import runpy
runpy.run_path('password_bruteforce.py', run_name='__main__')
