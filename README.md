# Remote-Shutdown

Remote-Shutdown allows you to turn off a Windows computer over a network connection. This works both on a LAN connection, and over the Internet (requires port forwarding). For security, this project uses [Fernet](https://cryptography.io/en/latest/fernet/) for message encryption.


## Usage

You will need to run the RSDLocalServer.py file on the Windows machine you would like to shutdown remotely. For instance, I placed an entry for this file on Windows Task Scheduler to run at startup. Because of the way programs are ran from the Task Scheduler, you also need to specify the "Start in" parameter to point to the directory that the RSDServerConfig.txt file is stored:

![enter image description here](https://i.imgur.com/ph0BBrf.png)

Once the server is running, you can simply use RSDRemoteClient.py to issue the shutdown command:
```python
import RSDRemoteClient

RSDRemoteClient.shutdown()
```

**Important:** Ensure that you setup both config files and place in the same directory with their corresponding .py files before running!

You have the option to run the provided FernetKeyGen.py script to generate and save a key to file, or you can use the [Fernet Documentation](https://cryptography.io/en/latest/fernet/) to implement your own solution.



## Disclaimer

This code is fully functional, however, it was developed for learning purposes and may not offer the full functionality or error handling as may be seen in other software.
