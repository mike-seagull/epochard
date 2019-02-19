[![Build Status](https://travis-ci.com/mike-seagull/epochard.svg?branch=master)](https://travis-ci.com/mike-seagull/epochard)  
Sweeps daily backups of [OPNsense](https://opnsense.org/) config files
<h3>epochard</h3>
<h4>prints epoch backup filenames to date strings</h4>
<code>python src/epochard.py [FILE|DIRECTORY|EPOCH]</code>
<h4>To compile it into a binary</h4>
<code>pyinstaller --distpath bin --onefile src/epochard.py</code>
