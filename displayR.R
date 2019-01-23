

### Notes 2018-03-14
### Desc: Titles (mytble[,-1]$Title)
resultTitles = function(mytble0) {
  yesCT = noCT = 0
  srch = toupper(mytble0[,-1]$Srch[1])
  seng = toupper(mytble0[,-1]$Eng[1])
  PTR_CT = length((mytble0[,-1]$Title))
  for (i in seq_len(length((mytble0[,-1]$Title)))) {
    meh <- toupper(mytble0[,-1]$Title[i])
    if (length(grep(srch, meh))  > 0) {
      yesCT = yesCT + 1
    } else {
      noCT = noCT + 1
    }
  }
  pie(x=c(yesCT, noCT), labels=c("In", "Not In"), radius=1,
      col=c("honeydew", "darkslategray3"),
      main=paste(seng, "'", srch, "' Results\n",
                 "Keyword In Titles\n", "(n =", PTR_CT, ")",
                 title(sub="blah")))
}


### Notes 2018-03-14
### Desc: Pie Chart Labels
pchartmain = function(mytble, strtype) {
  msg = toupper(strtype)
  if (strtype == "protocol") {
    LVL_CT = length((mytble[,-1]$Protocol))
  } else if (strtype == "tlds") {
    LVL_CT = length((mytble[,-1]$TLDs))
  } else if (strtype == "fqdn") {
    LVL_CT = length((mytble[,-1]$FQDN))
  } else {
    LVL_CT = length((mytble[,-1]$Protocol))
  }
  mn = paste(toupper(mytble[,-1]$Engine[1]),
             " '", mytble[,-1]$Srch[1],
             "' Search Results\n", msg, "(n =", LVL_CT, ")")
  return(mn)
}


### Notes 2018-03-14
###@MichelleFairow.
### Desc: Pie Chart Colors
pchartcols = function(strtype) {
  if (strtype == "protocol") {
    vc <- c("darkorchid", "gold", "cadetblue", "deeppink",
            "darkorchid1", "gold1", "cadetblue1", "deeppink1",
            "darkorchid2", "gold2", "cadetblue2", "deeppink3")
  } else if (strtype == "tlds") {
    vc <- c("paleturquoise", "honeydew", "orchid", "lavenderblush",
            "paleturquoise1", "honeydew1", "orchid1", "lavenderblush1",
            "powderblue", "honeydew2", "orchid2", "lavenderblush2")
  } else if (strtype == "fqdn") {
    vc <- c("slategray1", "whitesmoke", "palevioletred", "hotpink",
            "slategray2", "thistle1", "palevioletred1", "hotpink1",
            "slategray3", "thistle2", "palevioletred2", "hotpink2")
  } else {
    vc <- c("seashell", "magenta", "cadetblue",
            "seashell1", "magenta1", "cadetblue1",
            "seashell2", "magenta2", "cadetblue2")
  }
  return(vc)
}


### Notes 2018-03-14
###@MichelleFairow.
### Desc: PROTOCOL (mytble[,-1]$Protocol)
resultProtocols = function(mytble) {
  PTR_CT = length((mytble[,-1]$Protocol))
  lvlCT <- c()
  for (i in seq_len(length(levels(mytble[,-1]$Protocol)))) {
    ### print(levels(mytble[,-1]$Protocol)[i]) }
    meh <- mytble$Protocol == levels(mytble[,-1]$Protocol)[i]
    z <- length(which(meh, arr.ind=TRUE))
    lvlCT <- c(lvlCT, z)
  }
  pie(x=lvlCT, labels=levels(mytble[,-1]$Protocol), radius=1,
      col=pchartcols(strtype="protocol"),
      main=pchartmain(mytble, strtype="protocol"))
}


### Notes 2018-03-14
###@MichelleFairow.
### Desc: TLDS (mytble[,-1]$TLDs)
resultTlds = function(mytble, mx) {
  TLD_CT = length((mytble[,-1]$TLDs))
  lvlCT <- c()
  topLBL <- c()
  for (i in seq_len(length(levels(mytble[,-1]$TLDs)))) {
      ### print(levels(mytble[,-1]$TLDs)[i]) }
      meh <- mytble$TLDs == levels(mytble[,-1]$TLDs)[i]
      z <- length(which(meh, arr.ind=TRUE))
      if (z > mx) {
        lvlCT <- c(lvlCT, z)
        topLBL <- c(topLBL, levels(mytble[,-1]$TLDs)[i])
      }
  }
  pie(x=lvlCT, labels=topLBL, radius=1,
      col=pchartcols(strtype="tlds"),
      main=paste(pchartmain(mytble, strtype="tlds"),
                 "\n (freq > ", mx, ")")) 
}


### Notes 2018-03-14
###@MichelleFairow.
### Desc: DOAMINS/SUBDOAMINS (mytble[,-1]$SD1-4)
resultFqdn = function(mytble, mx) {
  SD_CT = length((mytble[,-1]$FQDN))
  lvlCT <- c()
  topLBL <- c()
  for (i in seq_len(length(levels(mytble[,-1]$FQDN)))) {
    meh <- mytble$FQDN == levels(mytble[,-1]$FQDN)[i]
    z <- length(which(meh, arr.ind=TRUE))
    if (z > mx) {
      lvlCT <- c(lvlCT, z)
      topLBL <- c(topLBL, levels(mytble[,-1]$FQDN)[i])
    }
  }
  pie(x=lvlCT, labels=topLBL, radius=1,
      col=pchartcols(strtype="fqdn"),
      main=paste(pchartmain(mytble, strtype="fqdn"),
                 "\n (freq > ", mx, ")")) 
}


###### Notes 2018-03-14 CONDENSE/COMBINE (All Functions)
#### Notes 2018-03-09 (Using sgr_test.py)
## mytble <- read.table(file="C:\\Users\\Michelle\\Documents\\Testing123.txt",
##                     header=TRUE, sep="\t")
#### Notes 2018-03-14 Titles
## mytble0 <- read.table(file="C:\\Users\\Michelle\\Documents\\Testing456.txt",
##                      header=TRUE, sep="\t")
