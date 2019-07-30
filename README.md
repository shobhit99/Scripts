# Logger
## Records data after every n seconds and is saved in csv
### requires iotop and bmon
```sh
sudo apt-get install iotop
sudo apt-get install bmon
python logger.py
```
## Output
```
csv file with following data
Timestamp,Memory Usage,Cpu Usage,Network Down,Network Up,Disk Read,Disk Write
```
