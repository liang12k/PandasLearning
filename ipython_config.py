#
# this default config to be placed in:
# ~/.ipython/profile_default
# http://2sn.org/python/ipython_config.py
#

# Configuration file for ipython.



c = get_config()

#------------------------------------------------------------------------------
# TerminalIPythonApp configuration
#------------------------------------------------------------------------------

# TerminalIPythonApp will inherit config from: BaseIPythonApplication,
# Application, InteractiveShellApp

# Execute the given command string.
# c.TerminalIPythonApp.code_to_run = ''

# The IPython profile to use.
# c.TerminalIPythonApp.profile = u'default'

# Set the log level by value or name.
# c.TerminalIPythonApp.log_level = 30

# lines of code to run at IPython startup.
# c.TerminalIPythonApp.exec_lines = []

# Enable GUI event loop integration ('qt', 'wx', 'gtk').
# c.TerminalIPythonApp.gui = None

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.TerminalIPythonApp.pylab = None

# Suppress warning messages about legacy config files
# c.TerminalIPythonApp.ignore_old_config = False

# If a command or file is given via the command-line, e.g. 'ipython foo.py
# c.TerminalIPythonApp.force_interact = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHON_DIR.
# c.TerminalIPythonApp.ipython_dir = u'/home/alex/.config/ipython'

# Whether to display a banner upon starting IPython.
# c.TerminalIPythonApp.display_banner = True

# Start IPython quickly by skipping the loading of config files.
# c.TerminalIPythonApp.quick = False

# A list of dotted module names of IPython extensions to load.
# c.TerminalIPythonApp.extensions = []

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.TerminalIPythonApp.copy_config_files = False

# dotted module name of an IPython extension to load.
# c.TerminalIPythonApp.extra_extension = ''

# List of files to run at IPython startup.
# c.TerminalIPythonApp.exec_files = []

import os

filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    c.TerminalIPythonApp.exec_files = [filename]

# Whether to overwrite existing config files when copying
# c.TerminalIPythonApp.overwrite = False

# A file to be run
# c.TerminalIPythonApp.file_to_run = ''

#------------------------------------------------------------------------------
# TerminalIPythonApp configuration
#------------------------------------------------------------------------------

# TerminalIPythonApp will inherit config from: BaseIPythonApplication,
# Application, InteractiveShellApp

# Execute the given command string.
# c.TerminalIPythonApp.code_to_run = ''

# The IPython profile to use.
# c.TerminalIPythonApp.profile = u'default'

# Set the log level by value or name.
# c.TerminalIPythonApp.log_level = 30

# lines of code to run at IPython startup.
# c.TerminalIPythonApp.exec_lines = []

# Enable GUI event loop integration ('qt', 'wx', 'gtk').
# c.TerminalIPythonApp.gui = None

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.TerminalIPythonApp.pylab = None

# Suppress warning messages about legacy config files
# c.TerminalIPythonApp.ignore_old_config = False

# If a command or file is given via the command-line, e.g. 'ipython foo.py
# c.TerminalIPythonApp.force_interact = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHON_DIR.
# c.TerminalIPythonApp.ipython_dir = u'/home/alex/.config/ipython'

# Whether to display a banner upon starting IPython.
# c.TerminalIPythonApp.display_banner = True

# Start IPython quickly by skipping the loading of config files.
# c.TerminalIPythonApp.quick = False

# A list of dotted module names of IPython extensions to load.
# c.TerminalIPythonApp.extensions = []

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.TerminalIPythonApp.copy_config_files = False

# dotted module name of an IPython extension to load.
# c.TerminalIPythonApp.extra_extension = ''

# List of files to run at IPython startup.
# c.TerminalIPythonApp.exec_files = []

# Whether to overwrite existing config files when copying
# c.TerminalIPythonApp.overwrite = False

# A file to be run
# c.TerminalIPythonApp.file_to_run = ''

#------------------------------------------------------------------------------
# InteractiveShellApp configuration
#------------------------------------------------------------------------------

# A Mixin for applications that start InteractiveShell instances.
#
# Provides configurables for loading extensions and executing files as part of
# configuring a Shell environment.
#
# Provides init_extensions() and init_code() methods, to be called after
# init_shell(), which must be implemented by subclasses.

# Execute the given command string.
# c.InteractiveShellApp.code_to_run = ''

# lines of code to run at IPython startup.
# c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('from __future__ import division')
c.InteractiveShellApp.exec_lines.append('from __future__ import print_function')
c.InteractiveShellApp.exec_lines.append('from __future__ import with_statement')
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')

# A list of dotted module names of IPython extensions to load.
# c.InteractiveShellApp.extensions = []

# dotted module name of an IPython extension to load.
# c.InteractiveShellApp.extra_extension = ''

# List of files to run at IPython startup.
# c.InteractiveShellApp.exec_files = []

# A file to be run
# c.InteractiveShellApp.file_to_run = ''

#------------------------------------------------------------------------------
# TerminalInteractiveShell configuration
#------------------------------------------------------------------------------

# TerminalInteractiveShell will inherit config from: InteractiveShell

# auto editing of files with syntax errors.
# c.TerminalInteractiveShell.autoedit_syntax = False

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.TerminalInteractiveShell.color_info = True

#
# c.TerminalInteractiveShell.history_length = 10000

#
# c.TerminalInteractiveShell.separate_in = '\n'

# Set the color scheme (NoColor, Linux, or LightBG).
c.TerminalInteractiveShell.colors = 'LightBG'

# Autoindent IPython code entered interactively.
# c.TerminalInteractiveShell.autoindent = True

#
# c.TerminalInteractiveShell.readline_omit__names = 2

#
# c.TerminalInteractiveShell.prompt_in2 = '   .\\D.: '

#
# c.TerminalInteractiveShell.separate_out = ''

#
# c.TerminalInteractiveShell.prompt_in1 = 'In [\\#]: '

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does nject even if you didn't type
# explicit parenthesesif
reen_length = 0

# Set the editor used by IPython (default to $EDITOR/vi/notepad).
# c.TerminalInteractiveShell.editor = 'vi'

#
# c.TerminalInteractiveShell.prompts_pad_left = True

# The part of the banner to be printed before the profile
# c.TerminalInteractiveShell.banner1 = 'Python 2.7.2 (default, Oct 27 2011, 01:40:22) \nType "copyright", "credits" or "license" for more information.\n\nIPython 0.11 -- An enhanced Interactive Python.\n?         -> Introduction and overview of IPython\'s features.\n%quickref -> Quick reference.\nhelp      -> Python\'s own help system.\nobject?   -> Details about \'object\', use \'object??\' for extra details., '"\\C-k": kill-line', '"\\C-u": unix-line-discard']

# The part of the banner to be printed after the profile
# c.TerminalInteractiveShell.banner2 = ''

#
# c.TerminalInteractiveShell.separate_out2 = ''

#
# c.TerminalInteractiveShell.wildcards_case_sensitive = True

#
# c.TerminalInteractiveShell.readline_merge_completions = True

# Set to confirm when you try to exit IPython with an EOF (Control-D in Unix,
# Control-Z/Enter in Windows). By typing 'exit' or 'quit', you can lled without the leading %.
# c.TerminalInteractiveShell.automagic = True

#
# c.TerminalInteractiveShell.readline_use = True

# Start logging to the given file in append mode.
# c.TerminalInteractiveShell.logappend = ''

#
# c.TerminalInteractiveShell.xmode = 'Context'

#
# c.TerminalInteractiveShell.quiet = False

# Enable auto setting the terminal title.
# c.TerminalInteractiveShell.term_title = False

#
# c.Terry exception.
# c.TerminalInteractiveShell.pdb = False

#------------------------------------------------------------------------------
# ProfileDir configuration
#-------------------------------tty printed, :func:`repr` is used. See the
# documentation of :mod:`IPython.external.pretty` for details on how to write
# pretty printers.  Here is a simple example::
#
#     def dtype_pprinter(obj, p, cycle):
#         if cycle:
#             return p.text('dtype(...)')
#         if hasattr(obj, 'fields'):
#             if obj.fields is None:
#                 p.text(repr(obj))
#             else:
#                 p.begin_group(7, 'dtype([')
#                 for i, field in enumerate(obj.descr):
#                     if i > 0:
#                         p.text(',')
#                         p.breakable.PlainTextFormatter.max_width = 79

#
# c.PlainTextFormatter.singleton_printers = {}

