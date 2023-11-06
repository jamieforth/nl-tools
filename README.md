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
   - If not: `mkdir .ssh`
   - `exit`
   - `scp ssh/authorized_keys eeg-a:.ssh/`
   - Run powershell as Administrator and run `notepad`.
   - In notepad open the file `C:\ProgramData\ssh\sshd_config` (select
     `All files`).
   - Comment out the two lines at the bottom starting `Match Group
     administators...`.
   - Restart `sshd`/the tablet.
   - Then `ssh eeg-a` should log you in without a password.
   - If you are using an ssh-agent/password manager, you might need to
     run the following first: `ssh-add ~/.ssh/id_rsa-neurolive` (the
     passphrase is the same as the tablet passwords).


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
pip install pipenv -i http://kassia.local/neuroive/simple --trusted-host kassia.local
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

1. script to start `LSL server` and `lsl-relay`.
   - place this on the desktop?
   - or will we start remotely via an ssh script?
2. script to pull software updates from Jamie F's laptop?
