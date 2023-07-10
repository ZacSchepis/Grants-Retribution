import subprocess
def check_installs(package_name):
    try: 
        __import__(package_name)
    except ImportError:
        base_script = 'pip install --upgrade {}'
        subprocess.run(base_script.format(package_name), shell=True, capture_output=False, text=False)

import notebook
import nbconvert
import jupyterlab
import jupyter_server
import jupyter_core
import jupyter_client
import ipywidgets
import ipykernel
import IPython
import traitlets
packs_module_ = ['traitlets','notebook','nbconvert','jupyterlab','jupyter_server','jupyter_core','jupyter_client','ipywidgets','ipykernel','IPython', 'papermill','jupyterlab_slurm']

for packs in packs_module_:
    check_installs(packs)



needed = {
    'IPython': [8,14,0],'ipykernel': [6,24,0],'ipywidgets': [8,0,7],'jupyter_client': [8,3,0],'jupyter_core': [5,3,1],'jupyter_server': [2,7,0],'jupyterlab': [4,0,2],'nbconvert': [7,6,0],'notebook': [6,5,4],'traitlets': [5,9,0]
}
packs_module = [traitlets,notebook,nbconvert,jupyterlab,jupyter_server,jupyter_core,jupyter_client,ipywidgets,ipykernel,IPython]

def makeversion_str(package_):
    try:
        if package_.__version__:
            nums = package_.__version__.split(".")
            return [int(num) for num in nums]
    except:
        print("Module not found")

def check_versions():
    base_script = 'pip install --upgrade {}'

    vals = [makeversion_str(name) for name in packs_module]
    cur = dict(zip(needed.keys(), vals)) 
    for mod in needed.keys():
        curval = cur.get(mod)
        neededval = cur.get(mod)
        if (curval[0] < neededval[0]):
            if (curval[1] < neededval[1]):
                print(f'About to run: `{base_script.format(mod)}` because {mod} is not the right version')
                res = subprocess.run(base_script.format(mod), shell=True, capture_output=False, text=0)
        else:
            print(f'Package `{mod}` should be at a satisifable version')

check_versions()
