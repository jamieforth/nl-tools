# Neurolive tablet setup

Clone this repository to your laptop.

```
cd <some place you want to download this repository>

git clone https://github.com/jamieforth/nl-tools.git

cd nl-tools
```

## ssh

1. On your laptop copy `ssh/config` into `~/.ssh/config` (or copy and
   paste the contents if you have an existing config file).
2. On your laptop copy both of the following files into `~/.ssh`
   - `id_rsa-neurolive`
   - `id_rsa-neurolive.pub`
   - (ask Jamie F or Laura for these keys!)
3. test you can log into a tablet, e.g. `eeg-a`

```
ssh eeg-a
```

4. This will ask for the password if `authorized_keys` has not yet
   been configured on the tablet.
   - To check this, ssh into the tablet and check if
     `C:\Users\neuro\.ssh\authorized_keys` exists.
   - If not on the tablet: `mkdir .ssh`
   - `exit` to return to your laptop
   - On your laptop: `scp ssh/authorized_keys eeg-a:.ssh/`
   - On the tablet (use the screen) enable `Show hidden items`: Open
     File Explorer and select `Show hidden items` (it's an option in
     the top bar).
   - On the tablet open powershell as Administrator and run `notepad`.
   - In notepad open the file `C:\ProgramData\ssh\sshd_config` (select
     `All files`).
   - Comment out the two lines at the bottom starting `Match Group
     administators...`.
   - Restart `sshd`/the tablet.
   - Then `ssh eeg-a` should log you in without a password.
   - If you are using an ssh-agent/password manager, you might need to
     run the following first: `ssh-add ~/.ssh/id_rsa-neurolive` (the
     passphrase is the same as the tablet passwords).

     On a Windows machine, there are two extra steps:
      2. Go to Services-> OpenSSH Authentication Agent and change startup type to 'Automatic', Apply, and Start the service.
      2. From PowerShell, run : `ssh-add "C:\Users\<USERNAME>\.ssh\id_rsa-neurolive"` (changing USERNAME to your windows username)


## pylsl-tools

Install the [pylsl-tools](https://github.com/jamieforth/pylsl-tools)
package.


1. ssh into a tablet.
2. Check python and git are installed.

```
git --version
python --version
```

3. Install pipenv from `kassia.local`.

```
pip install pipenv -i http://kassia.local/neurolive/simple --trusted-host kassia.local
```

```
git clone http://kassia.local/neurolive/nl-tools
```

```
cd nl-tools
pipenv install
```

4. Test install: `pipenv run lsl-simulate --help`


## Test simulated data.

```
# Windows firewall will block python scripts accessing the network!
# First run this command from a GUI terminal (not over ssh) so that
# the firewall pop-up can be accepted.
pipenv run lsl-simulate -n 1 -s 2 --max-time 10 --debug
```

```
# You can use any control-name, it just needs to match the name of 
# the controller.
pipenv run lsl-simulate -n 1 -s 2 --debug --control-name ctrl1
```

On another computer start the controller.

```
pipenv run lsl-control --name ctrl1
```

Then the tablet stream (and any other stream on the network) can be
remote controlled from this terminal window.


## Windows batch scripts

Before doing any of the below options, some batch scripts need to be copied to the tablets. You can do this by calling the python script ```copy_files_to_devices.py``` from your main machine.

1. You can start both the AntNeuro EEG remote software plus the lsl_relay from a single script on the Desktop of each tablet. You can run this by:
   - on the tablet, click on the 'lsl_run.bat' file
   - ...working on how to do this remotely
2. A single script is also used to update Jamie F's software. You can find this in the C:/Users/neuro home directory. Call either by
   - on the tablet, go to File Explorer, navigate to C:/Users/neuro and click on the 'nl_tools_update.bat' file
   - [easier] ssh into the tablet, and run ```nl_tools_update```
   - [most convenient] from your main machine, run the python script ```update_all_devices.py```
   - 
   
