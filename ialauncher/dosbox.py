import sys, os, glob, subprocess


class DOSBoxNotFound(Exception):
    pass


def try_command(command):
    print("try_command1")


#subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

#subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, #timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, #**other_popen_kwargs)

#    subprocess.run(command + ['--version'], capture_output=True).check_returncode()
    subprocess.check_call(command + ['--version'], stdout=subprocess.PIPE)
    print("try_command2")
    return command


def get_dosbox_path():
    try:
        return try_command(['dosbox'])
    except:
        pass
    try:
        # Proper way to do it on macOS
        return try_command(['open', '-a', 'DOSBox', '--args'])
    except:
        pass
    try:
        # Fallback to hardcoded path on macOS
        return try_command(['/Applications/dosbox.app/Contents/MacOS/DOSBox'])
    except:
        pass
#    try:
        # Special case for Windows
#    pf = os.environ['ProgramFiles(x86)']
    pf = "c:\Program Files (x86)"
#        path = glob.glob(f'{pf}\dosbox*\dosbox.exe')[0]
    path = glob.glob('%s\dosbox*\dosbox.exe' % pf)[0]
    print("path:")
    print(path)
    return try_command([path])

#    except Exception as err:
#        print("Unexpected error: ", sys.exc_info()[0])
#        pass

#    raise DOSBoxNotFound("The program DOSBox could not be found on your system.")


