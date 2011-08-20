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

git clone git://github.com/yodiaditya/vim-netbeans.git vim-netbeans

ln -s ~/vim-netbeans/.vim ~/.vim

ln -s ~/vim-netbeans/.vimrc ~/.vimrc


Dependencies
------------

After do installing, you should go to VIM and do :BundleInstall. I use Vundle here which i use pathogen in the past development.

I use nodejs-snipmate and snipmate snippets from honza. So delete /snipmate.vim/snippets for enabling this two snippets update. 


Also, i install Python Debugger like pyflakes, pylint and pep8. 

For installing Python debugger using PIP :

sudo pip install pylint
sudo pip install pyflakes
sudo pip install pep8

Read .vimrc for magic keys and guide.

Also you need Ctags. If you using Ubuntu, then can do this command :
sudo apt-get install exuberant-ctags

Usage
------
For using this custom VIM, here are some clue : 

1. Use Backspace as PageUp & Space as PageDown 

2. Use tab in insert mode for autocomplete for Python ( using PyDiction )

3. Text Autocomplete every you type. Also you can use CTRL + Space for Omni Completion

4. Move tab using CTRL+Arrow

5. Using NERDTree by :NERDTree or editing .vimrc to enable NERDTree automatically.


Author
-------
I'm using VIM and Netbeans for building many application on PHP, JS and Python

I have a lot of blog which contains many information. You can check here : 

1. http://yoodey.com for Drupal 7, EC2 and Ubuntu Tutorial

2. http://cisight.com for Codeigniter, CakePHP and Optimization Tutorial 

3. http://wpscale.com for Wordpress Tutorial

4. http://yodi.me for my Programming Insight

5. http://re.web.id for Indonesian Python Programming Guide
