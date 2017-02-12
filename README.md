# Persistent command line memoizer

## Improvememnts
- Python 3
- Process tree and IO visualization (currently in YAML)

## TODO
- [ ] Port to [D](http://dlang.org/) for better performance.
- [ ] Test on Linux for Windows 10 (does it support strace and inotify?)
- [ ] Add optional support for more robust tracing
  with [ltrace](https://en.wikipedia.org/wiki/Ltrace)
- Store git repo URL for sets of files in a tree-like format in rw_list file in cache
- [ ] Implement a memoization server using [inotify](https://en.wikipedia.org/wiki/Inotify)
