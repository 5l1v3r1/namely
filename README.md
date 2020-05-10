# namely
Namely creates a list of emails based on user inputted names and domains. 

```
usage: namely.py [-h] [-n name name] [-nf namefile] [-d domain]                                                                                            
                 [-df domainfile] [-t template] [-tf templatefile]                                                                                         
                 [-o outfile]                                                                                                                              
                                                                                                                                                           
 __  _  __  __ __ ___ _ __   __                                                                                                                            
|  \| |/  \|  V  | __| |\ `v' /                                                                                                                            
| | ' | /\ | \_/ | _|| |_`. .' 
|_|\__|_||_|_| |_|___|___|!_!  

by Oriel & Tyler Kranig

github.com/OrielOrielOriel
github.com/tylerkranig

optional arguments:
  -h, --help            show this help message and exit
  -n name name, --name name name
                        A single name
  -nf namefile, --namefile namefile
                        A list of names
  -d domain, --domain domain
                        A single domain
  -df domainfile, --domainfile domainfile
                        A list of domains
  -t template, --template template
                        A single template
  -tf templatefile, --templatefile templatefile
                        A list of templates
  -o outfile, --outfile outfile
                        The file to output to
```

## Example Usage

```
./namely.py -n hannah montana -d bad-dragon.com

hannah_montana@bad-dragon.com
montana_hannah@bad-dragon.com
h_montana@bad-dragon.com
hannah_m@bad-dragon.com
han_montana@bad-dragon.com
m_hannah@bad-dragon.com
mon_hannah@bad-dragon.com
hannah.montana@bad-dragon.com
montana.hannah@bad-dragon.com
h.montana@bad-dragon.com
hannah.m@bad-dragon.com
han.montana@bad-dragon.com
m.hannah@bad-dragon.com
mon.hannah@bad-dragon.com
hannahmontana@bad-dragon.com
montanahannah@bad-dragon.com
hmontana@bad-dragon.com
hannahm@bad-dragon.com
hanmontana@bad-dragon.com
mhannah@bad-dragon.com
monhannah@bad-dragon.com
hannah-montana@bad-dragon.com
montana-hannah@bad-dragon.com
h-montana@bad-dragon.com
hannah-m@bad-dragon.com
han-montana@bad-dragon.com
m-hannah@bad-dragon.com
mon-hannah@bad-dragon.com
```


