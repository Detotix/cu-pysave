This is a library for the game **"Casualties: Unknown"**.  
Currently it only provides basic reading and writing of savefiles  
more features are planned.

## Example: Loading, printing and writing a savefile
```python
import cu_pysave as cu
loadedsave=cu.LoadSave("save.sv")#loading a save file

print(loadedsave.dict())
loadedsave.write_save("test1.sv")#writing a save file

#loading as a dict and writing after that
loadeddict=cu.CU_GameSave(loadedsave.dict())#loading a dict
loadeddict.write_save("test2.sv")#writing a save file
```
## pip installation
'''bash
pip install git+https://github.com/detotix/cu-pysave.git
'''