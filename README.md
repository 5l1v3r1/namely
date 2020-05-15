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
./namely.py -n hannah montana -d linked.in  

hannah_montana@linked.in
montana_hannah@linked.in
h_montana@linked.in
hannah_m@linked.in
han_montana@linked.in
m_hannah@linked.in
mon_hannah@linked.in
hannah.montana@linked.in
montana.hannah@linked.in
h.montana@linked.in
hannah.m@linked.in
han.montana@linked.in
m.hannah@linked.in
mon.hannah@linked.in
hannahmontana@linked.in
montanahannah@linked.in
hmontana@linked.in
hannahm@linked.in
hanmontana@linked.in
mhannah@linked.in
monhannah@linked.in
hannah-montana@linked.in
montana-hannah@linked.in
h-montana@linked.in
hannah-m@linked.in
han-montana@linked.in
m-hannah@linked.in
mon-hannah@linked.in
hannah@linked.in
montana@linked.in
```


### Custom template provided as a CLI argument: 

```
cat names.txt

fergus smith                                                                   
shaun coins                                                                    
bowie taylor                                                                   
sophie driver                                                                  
hugo bear                                                                      
steven kerb

./namely.py --namefile names.txt -d potato.land -t potato_master.\${first1}-\${last}1998@\${domain} 

potato_master.f-smith1998@potato.land                                          
potato_master.s-coins1998@potato.land                                          
potato_master.b-taylor1998@potato.land                                         
potato_master.s-driver1998@potato.land                                         
potato_master.h-bear1998@potato.land                                           
potato_master.s-kerb1998@potato.land
```


### Arbitrary key values and associated wordlists: 

```
echo Hamster >> animals.txt
echo Cobra >> animals.txt
echo Blue >> colors.txt
echo Orange >> colors.txt
echo Green >> colors.txt

cat animals.txt

Hamster
Cobra

cat colors.txt 

Blue
Orange
Green

./namely.py -n Lily Raichu -d online.tv -k animal animals.txt -k color colors.txt -t \${first}-\${last}\'s\${color}-\${animal}@\${domain}

Lily-Raichu'sBlue-Hamster@online.tv
Lily-Raichu'sOrange-Hamster@online.tv
Lily-Raichu'sGreen-Hamster@online.tv
Lily-Raichu'sBlue-Cobra@online.tv
Lily-Raichu'sOrange-Cobra@online.tv
Lily-Raichu'sGreen-Cobra@online.tv
```