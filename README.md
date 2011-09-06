VIM-Netbeans
=============

use VIM as great as Netbeans for editing PHP, Python, JS, HTML, XML and many else filetype.

This have several great feature :

- Supported with NodeJS, Stylus, Less and many CSS/Javascript engine, template, parser 
- Integrated with JavascriptLint for auto-checking syntax 
- Have great Python checking and fast shortcut like `Shift - e` for execute current files
- Use Vundle for managing plugins
- `F8` for Browser files and Tags
- Check .vimrc to see many feature and goodies bag


This VIM is inspired by many great developers that share their custom VIM configuration.


Installing
-----------

Go to your Command / Terminal : 

    cd ~/
    git clone https://github.com/yodiaditya/vim-netbeans.git 
    ln -s ~/vim-netbeans/.vimrc ~/.vimrc
    ln -s ~/vim-netbeans/.vim ~/.vim
    git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
    vim ~/.vimrc 

When opening .vimrc, do ":BundleInstall" to install all package and exit by :wq.

    rm -rf ~/.vim/bundle/snipmate.vim/snippets

Change your TAB behaviour between PyDiction and Snipmate by follow this link :

http://stackoverflow.com/questions/1687252/with-vim-use-both-snipmate-and-pydiction-together-share-the-tab-key

But i prefer using CTRL+Space as Snipmate Completion. Here a how to make it :

`vim ~/.vim/bundle/snipmate.vim/after/plugin/snipMate.vim`

Edit start from line 15 :

    "ino <silent> <tab> <c-r>=TriggerSnippet()<cr>
    "snor <silent> <tab> <esc>i<right><c-r>=TriggerSnippet()<cr>
    ino <silent> <C-Space> <c-r>=TriggerSnippet()<cr>
    snor <silent> <C-Space> <esc>i<right><c-r>=TriggerSnippet()<CR>


Dependencies
------------

After do installing, you should go to VIM and do :BundleInstall. I use Vundle here which i use pathogen in the past development.

I use nodejs-snipmate and snipmate-snippets. To preventing crash between default snippets in Snipmate and others,

delete ~/.vim/bundle/snipmate.vim/snippets. 


### A. Python Debugger like pyflakes, pylint and pep8

For installing Python debugger using PIP :

    sudo apt-get install python-pip
    sudo pip install git+git://github.com/kevinw/pyflakes.git
    sudo pip install pylint
    sudo pip install pep8

Read .vimrc for magic keys and guide.


### B. Ctags

If you using Ubuntu, then can do this command :

`sudo apt-get install exuberant-ctags`


### C. JavascriptLint

This is powerfull Javascript syntax checker with quickfix.

Folow this link for installation guide : http://cisight.com/auto-checking-errors-for-javascript-in-vim/

Also add this into .vim/bundle/javaScriptLint.vim/plugin/javaScriptLint.vim :


    " set up commands
    command! JavaScriptLintExec call JavascriptLint()
    command! JavaScriptLintClear call s:ClearCursorLineColor()

### D. Colorscheme

This VIM using Mustang as Colorscheme. If you use Yakuake for running VIM, then you should change your Yakuke for running 256-colors.

Here are to set it : http://yoodey.com/using-terminal-console-yakuake-running-256-colors

Usage
------
For using this custom VIM, here are some clue : 

1. Use Backspace as PageUp & Space as PageDown in normal mode
2. Use tab (insert mode) for autocomplete Python using PyDiction
3. Autocomplete every you type. Also you can use CTRL + Space for Snipmate Autocompletion
4. Move to another tab / buffer using CTRL+Arrow
5. Using NERDTree by :NERDTree or editing .vimrc to enable NERDTree automatically.
6. Using F7 for FuzzFinder in Full Path or <leader>t (,t) for open based on current Buffer 
7. Press F8 for enabling NERDTRee and Tagbar (Love it!) 
8. Use <leader> space for MRU
9. Use Shift+e for execute Python code 
10. Use Shift+n for execute NodeJS code 
11. Use Shift+j for checking javascript syntax in current file 
12. Also check many goodies bag in .vimrc


Author
-------
I'm using VIM and Netbeans for building many application on PHP, Javascript, NodeJS, Ruby and Python

I have a lot of blog which contains many information. You can check here : 

- http://yoodey.com for Drupal 7, EC2 and Ubuntu Tutorial
- http://cisight.com for Codeigniter, CakePHP and Optimization Tutorial 
- http://wpscale.com for Wordpress Tutorial
- http://yodi.me for Python, Jekyll, Ruby and many research developments
- http://re.web.id for Indonesian Python Programming Guide
