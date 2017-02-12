# Persistent command line memoizer

## Improvememnts

- Python 3

## TODO

- [ ] Process tree and IO visualization (currently in YAML)
- [ ] Port to [D](http://dlang.org/) for better performance.
- [ ] Test on Linux for Windows 10 (does it support strace and inotify?)
- [ ] Add optional support for more robust tracing
  with [ltrace](https://en.wikipedia.org/wiki/Ltrace)
- Store git repo URL for sets of files in a tree-like format in rw_list file in cache
- [ ] Implement a memoization server using [inotify](https://en.wikipedia.org/wiki/Inotify)

- [ ] Fix crash when building ~/Work/dmd

- [ ] Cache stdout and stderr

- [ ] current time before call to strace and the modtime for each input after
- [ ] use to more safely remove written files in opened (potential input)
- [ ] Reuse watchman here to faster discard directories that have are
- [ ] but whose content haven't changed.

- [ ] Reuse `watchman`:
- [ ] https://facebook.github.io/watchman/
- [ ] https://github.com/facebook/watchman

- [ ] Lookup command and list of inputs from output artifact

- [ ] Activate checking of `access` inputs

- [ ] Warn about certain output paths?
- [ ] Warn when inputs and outputs

- [ ] Save and load
- [ ] Zero exist codes in calls to sys.exit()

- [ ] How to handle stat mtime on input dirs where output files are written?

- [ ] Update modification times in cache if they are same as written file

- [ ] Add `env` argument to `memoized_run` and use it instead of `os.environ._data` if set

- [ ] Detect file system race conditions in child processes

- [ ] Ask on StackExchange if there's a flag to strace to not show failing calls

- [ ] Ask Claes Wallin how to fingerprint the Linux kernel version or distribution
- [ ] /proc/version
- [ ] /proc/mounts

- [ ] use gcc -pipe

- [ ] add git origin (repo:commit) to input files and sort them on git repo origin
- [ ]_REPO:GIT_COMMIT
- [ ] rel_path_file_a
- [ ] rel_path_file_b
- [ ] ...

- [ ] parse 'st_mtime using Python's datetime.strptime(some_string, '')

- [ ] directory chash is chash of list of file names in directory

- [ ] use ltrace and reduce env deps by catching all getenv

- [ ] add server that does inotify watches for all dirs containing input and
- [ ] files

- [ ] Add automatic distribution of execution via chroot. System libs and
  programs can be hard-linked out read-only from cache
