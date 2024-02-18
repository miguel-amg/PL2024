""" Name: Miguel Guimarães
    University: Universidade do Minho
    Processamento de Linguagens 2024 / Language processing 2024 """ 

########################### Setup ###########################
# Imports 
import re # Regular expression 

# Setup variables
MDpath = "files/text.md" # Path to markdown file
HTMLpath = "files/final.html" # Save path for hmtl file

########################### Code ###########################
f = open(MDpath, "r") # Open file
content = f.read() # Read file

# Substitute "### text" -> <h1>text</h1>
new_content = re.sub(r'^(#+) (.+)', "<h1>\\2</h1>" , content , flags=re.MULTILINE) # \\1 Calls the value of the first subgroup (It's # ola)

# Substitute **text** -> <b>text</b>
new_content = re.sub(r'\*\*([^*\n ]+)\*\*', r'<b>\1</b>', new_content)

# Substitute *text* -> <b>texto</b>
new_content = re.sub(r'\*([^*\n ]+)\*', r'<i>\1</i>', new_content) 

# Subsistute (1. elem1 2. elem2) -> (<ol> <li>elem1</li> <li>elem2</li> </ol>)
new_content = re.sub(r'\d+\. (.*)', r'<li>\1</li>', new_content) # Insert <li>
new_content = re.sub(r'(<li>.+</li>\s*)+', r'<ol>\n\g<0></ol>\n', new_content) # Insert the <ol> - Miguel´s note: \g<0> is the full string it represents the group 0.

# Subsistute (![imagem dum coelho](http://www.coellho.com)) -> (<img src="http://www.coellho.com" alt="imagem dum coelho"/>)
new_content = re.sub(r'!\[([^\[]+)\]\((http://www\.[^\[]+\.[^\[]+?)\)', r'<img src="\2" alt="\1"/>', new_content) # Insert <img>

# Subsistute ([página da UC](http://www.uc.pt)) -> (<a href="http://www.uc.pt">página da UC</a>)
new_content = re.sub(r'\[([^\[]+)\]\((http://www\.[^\[]+\.[^\[]+?)\)', r'<a href="\2">\1</a>', new_content) # Insert <a>

########################### Write new content ###########################
f = open(HTMLpath, "w") # Write file with content
f.write(new_content)

