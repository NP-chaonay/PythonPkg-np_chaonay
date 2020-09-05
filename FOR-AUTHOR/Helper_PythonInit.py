## Initialization
import sys,os
import subprocess as sp
import np_chaonay.main as npc_m

### Shell Utilities and Application Commands Wrapper
def nano(file):
	sp.run(['nano',file])
def gedit(file):
	sp.Popen(['gedit',file])
def ls(path='.'):
	sp.Popen(['ls',path])

### Create and upload Git tag
def new_uploading_tag(tag_name,tag_desc=None,commit=None):
	args=['git', 'tag', '-a', tag_name]
	if tag_desc: args+=['-m', tag_desc]
	if commit: args+=[commit]
	sp.run(args)

## For specific works
### Create and upload Git tag
def SW_new_uploading_tag(version,development=False,commit=None):
	if development:
		tag_name=version+'_dev'
		version=version+'.dev'
	else:
		tag_name=version+'_stable'
	tag_desc='Latest commit of version \''+version+'\''
	new_uploading_tag(tag_name,tag_desc,commit)

def SW_diff(path,a='origin/master',b='origin/development'):
	sp.run(['git', 'diff', a, b, '--', path])

def SW_git_push(msg):
	if not msg: npc_m.print_categorical_bracket('git_push:ERROR','GIT push function requires committing message.')
	npc_m.print_categorical_bracket('git_push','GIT Add')
	sp_log=sp.run(['git', 'add', '.'])
	if sp_log.returncode!=0:
		npc_m.print_categorical_bracket('git_push:ERROR','GIT Add Error')
	npc_m.print_categorical_bracket('git_push','GIT Commit')
	sp_log=sp.run(['git', 'commit', '-m', msg])
	if sp_log.returncode!=0:
		npc_m.print_categorical_bracket('git_push:ERROR','GIT Commit Error, undoing changes staging.')
		sp.run(['git', 'reset'])
	npc_m.print_categorical_bracket('git_push','GIT Push')
	sp.run(['python3', npc_m.slash_suffix_for_dir(npc_m.get_homedir())+".password/ ", 'github'])	
	sp_log=sp.run(['git', 'push'])
	if sp_log.returncode!=0:
		npc_m.print_categorical_bracket('git_push:ERROR','GIT Push Error, cancelling commit.')
		sp.run(['git', 'reset', '--soft', 'HEAD^'])
		sp.run(['git', 'reset'])
