# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'
#pre_build = vcs_update


def post_build():
    git_add_files('PKGBUILD')
    git_commit()


#if __name__ == '__main__':
#    single_main()
