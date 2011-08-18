VIM-Netbeans
=============

We want use VIM as great as Netbeans for editing PHP, Phyton, JS, HTML, XML and many else filetype.

This VIM bundled with many plugins, syntax and custom .vimrc configuration. 

This VIM is inspired by many great developers that share their custom VIM configuration.

All TLDR; documentation located in .vimrc. You can read and follow link there to see related projects used.

Installing
-----------
Go to your Command / Terminal : 

cd ~/

git clone git://github.com/yodiaditya/vim-netbeans.git

cd vim-netbeans/bundle/

ln -s ~/vim-netbeans/.vim ~/.vim

ln -s ~/vim-netbeans/.vimrc ~/.vimrc

cd ~/vim-netbeans/bundle/


Then download dependencies package.


Dependencies
------------

After do installing, you should clone all these package into ~/vim-netbeans/bundle/   

1. Check syntax after editing files : https://github.com/tomtom/checksyntax_vim.git

2. Pathogen https://github.com/tpope/vim-pathogen

3. Snipmate-vim from garbas https://github.com/garbas/vim-snipmate

4. Get Snipmate-vim dependency : 
    
    git clone https://github.com/tomtom/tlib_vim.git

    git clone https://github.com/MarcWeber/vim-addon-mw-utils.git

5. Snipmate-snippets : https://github.com/honza/snipmate-snippets 

6. Fugitive for Github easy connection : http://github.com/tpope/vim-fugitive.git

7. Supertab from https://github.com/ervandew/supertab.git

8. NERDTree for file explorer from https://github.com/scrooloose/nerdtree


All of this plugin should clone on ~/.vim/bundle because i using Pathogen here

Also, i install Python Debugger like pyflakes, pylint and pep8. 

For installing Python debugger using PIP :

sudo pip install pylint
sudo pip install pyflakes
sudo pip install pep8
sudo pip install ropevim

Read .vimrc for magic keys and guide.

For using Ubuntu
sudo apt-get install exuberant-ctags


Usage
------
For using this custom VIM, here are some clue : 

1. Use Backspace as PageUp & Space as PageDown 

2. Use tab in insert mode for autocomplete. 

3. Move tab using CTRL+Arrow


Author
-------
I'm using VIM and Netbeans for building many application on PHP and Python

Check out my blog for another articles : 

1. http://yoodey.com for Drupal 7, EC2 and Ubuntu Tutorial

2. http://cisight.com for Codeigniter and Optimization Tutorial 

3. http://wpscale.com for Wordpress Tutorial
