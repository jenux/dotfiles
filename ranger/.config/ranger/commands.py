import os
from ranger.api.commands import Command
from ranger.core.loader import CommandLoader


class compress(Command):
    def execute(self):
        """ Compress marked files to current directory """
        cwd = self.fm.thisdir
        marked_files = cwd.get_selection()

        if not marked_files:
            return

        def refresh(_):
            cwd = self.fm.get_directory(original_path)
            cwd.load_content()

        original_path = cwd.path
        parts = self.line.split()
        au_flags = parts[1:]

        descr = "compressing files in: " + os.path.basename(parts[1])
        obj = CommandLoader(args=['apack'] + au_flags + \
                [os.path.relpath(f.path, cwd.path) for f in marked_files], descr=descr, read=True)

        obj.signal_bind('after', refresh)
        self.fm.loader.add(obj)

    def tab(self, tabnum):
        """ Complete with current folder name """

        extension = ['.zip', '.tar.gz', '.rar', '.7z']
        return ['compress ' + os.path.basename(self.fm.thisdir.path) + ext for ext in extension]

class extract(Command):
    def execute(self):
        """ extract selected files to current directory."""
        cwd = self.fm.thisdir
        marked_files = tuple(cwd.get_selection())

        def refresh(_):
            cwd = self.fm.get_directory(original_path)
            cwd.load_content()

        one_file = marked_files[0]
        cwd = self.fm.thisdir
        original_path = cwd.path
        au_flags = ['-x', cwd.path]
        au_flags += self.line.split()[1:]
        au_flags += ['-e']

        self.fm.copy_buffer.clear()
        self.fm.cut_buffer = False
        if len(marked_files) == 1:
            descr = "extracting: " + os.path.basename(one_file.path)
        else:
            descr = "extracting files from: " + os.path.basename(
                one_file.dirname)
        obj = CommandLoader(args=['aunpack'] + au_flags
                            + [f.path for f in marked_files], descr=descr,
                            read=True)

        obj.signal_bind('after', refresh)
        self.fm.loader.add(obj)



class fzf_select(Command):
   """
   :fzf_select
   Find a file using fzf.
   With a prefix argument to select only directories.

   See: https://github.com/junegunn/fzf
   """

   def execute(self):
       import subprocess
       import os
       from ranger.ext.get_executables import get_executables

       if 'fzf' not in get_executables():
           self.fm.notify('Could not find fzf in the PATH.', bad=True)
           return

       fd = None
       if 'fdfind' in get_executables():
           fd = 'fdfind'
       elif 'fd' in get_executables():
           fd = 'fd'

       if fd is not None:
           hidden = ('--hidden' if self.fm.settings.show_hidden else '')
           exclude = "--no-ignore-vcs --exclude={node_modules,.wine,.git,.idea,.vscode,.sass-cache,node_modules,build,.local,.steam,.m2,.rangerdir,.ssh,.ghidra,.mozilla} --exclude '*.py[co]' --exclude '__pycache__'"
           only_directories = ('--type directory' if self.quantifier else '')
           fzf_default_command = '{} --follow {} {} {} --color=always'.format(
               fd, hidden, exclude, only_directories
           )
       else:
           hidden = ('-false' if self.fm.settings.show_hidden else r"-path '*/\.*' -prune")
           exclude = r"\( -name '\.git' -o -iname '\.*py[co]' -o -fstype 'dev' -o -fstype 'proc' \) -prune"
           only_directories = ('-type d' if self.quantifier else '')
           fzf_default_command = 'find -L . -mindepth 1 {} -o {} -o {} -print | cut -b3-'.format(
               hidden, exclude, only_directories
           )

       env = os.environ.copy()
       env['FZF_DEFAULT_COMMAND'] = fzf_default_command
       env['FZF_DEFAULT_OPTS'] = '--height=100% --layout=reverse --ansi --preview="{}"'.format('''
           (
               ~/.fzf-scope.sh {} ||
               #batcat --color=always {} ||
               bat --color=always {} ||
               #cat {} ||
               tree -ahpCL 3 -I '.git' -I '*.py[co]' -I '__pycache__' {}
           ) 2>/dev/null | head -n 100
       ''')

       fzf = self.fm.execute_command('fzf --no-multi', env=env,
                                     universal_newlines=True, stdout=subprocess.PIPE)
       stdout, _ = fzf.communicate()
       if fzf.returncode == 0:
           selected = os.path.abspath(stdout.strip())
           if os.path.isdir(selected):
               self.fm.cd(selected)
           else:
               self.fm.select_file(selected)
