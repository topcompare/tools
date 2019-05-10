#Code for monitoring the changes in App mobile scores

is.installed=function(mypkg){
  is.element(mypkg, installed.packages()[,1])
} 
if(!is.installed("googlesheets")){
  install.packages("googlesheets")
}
if(!is.installed("readr")){
  install.packages("readr")
}
if(!is.installed("rvest")){
  install.packages("rvest")
}
library(googlesheets)
library(readr)
library(rvest)

options(stringsAsFactors = FALSE)
appmob=data.frame(matrix("a", ncol = 8, nrow = 20))
colnames(appmob)[colnames(appmob)=="X1"]="Bank"
colnames(appmob)[colnames(appmob)=="X2"]="Rate G Play"
colnames(appmob)[colnames(appmob)=="X3"]="Number of reviews G play"
colnames(appmob)[colnames(appmob)=="X4"]="Rate App store"
colnames(appmob)[colnames(appmob)=="X5"]="Number of reviews App store"
colnames(appmob)[colnames(appmob)=="X6"]="Final score"
colnames(appmob)[colnames(appmob)=="X7"]="URL G play"
colnames(appmob)[colnames(appmob)=="X8"]="URL App store"

# PART1: Specifying the url for desired website to be scraped
appmob[1,7]='https://play.google.com/store/apps/details?id=com.kbc.mobile.android.phone.cbc' #CBC
appmob[2,7]='https://play.google.com/store/apps/details?id=be.belfius.directmobile.android' #Belfius
appmob[3,7]='https://play.google.com/store/apps/details?id=be.argenta.bankieren' #Argenta
appmob[4,7]='https://play.google.com/store/apps/details?id=be.axa.mobilebanking' #Axa
appmob[5,7]='https://play.google.com/store/apps/details?id=com.bnpp.easybanking' #BNP
appmob[6,7]='https://play.google.com/store/apps/details?id=com.bpb.mobilebanking.smartphone.prd' #Bpost
appmob[7,7]='https://play.google.com/store/apps/details?id=be.crelan.channels.mobile.android.store' #Crelan
appmob[8,7]='https://play.google.com/store/apps/details?id=com.mobile.europabank' #Europabank
appmob[9,7]='https://play.google.com/store/apps/details?id=com.bnpp.hellobank' #Hello Bank
appmob[10,7]='https://play.google.com/store/apps/details?id=MyING.be' #ING
appmob[11,7]='https://play.google.com/store/apps/details?id=com.kbc.mobile.android.phone.kbc' #KBC
appmob[12,7]='https://play.google.com/store/apps/details?id=be.keytradebank.phone' #Keytrade
appmob[13,7]='https://play.google.com/store/apps/details?id=be.bankdekremer.mobile' #Bank de Kremer
appmob[14,7]='https://play.google.com/store/apps/details?id=be.montepaschi.android.app' #Banca Monte Paschi Belgio
appmob[15,7]='https://play.google.com/store/apps/details?id=com.db.pbc.mybankbelgium' #Deutsche Bank
appmob[16,7]='https://play.google.com/store/apps/details?id=com.bnpp.easybanking.fintro' #Fintro
appmob[17,7]='https://play.google.com/store/apps/details?id=be.dlbank.mobilebankingapp' #Nagelmackers
appmob[18,7]='https://play.google.com/store/apps/details?id=com.vdk.prod' #VDK
appmob[19,7]='https://play.google.com/store/apps/details?id=be.cph.cphmobile&hl=en' #CPH
appmob[20,7]='https://play.google.com/store/apps/details?id=com.beobank_prod.bad&hl=en' #Beobank




appmob[1,8]='https://itunes.apple.com/be/app/cbc-mobile/id458081756?mt=8' #CBC
appmob[2,8]='https://itunes.apple.com/be/app/belfius-mobile/id572835707?mt=8' #Belfius
appmob[3,8]='https://itunes.apple.com/be/app/argenta-banking/id893585833?mt=8&ign-mpt=uo%3D4' #Argenta
appmob[4,8]='https://itunes.apple.com/be/app/mobile-banking-service/id602565257?l=fr&mt=8' #Axa
appmob[5,8]='https://itunes.apple.com/be/app/easy-banking-app/id516502006?mt=8' #BNP
appmob[6,8]='https://itunes.apple.com/be/app/mobilebanking-smartphone/id1278930217?l=nl' #Bpost
appmob[7,8]='https://itunes.apple.com/be/app/crelan-mobile/id893189359?mt=8' #Crelan
appmob[8,8]= 0 #Europabank
appmob[9,8]='https://itunes.apple.com/be/app/hello-bank-for-smartphone/id642897716?mt=8' #Hello Bank
appmob[10,8]='https://itunes.apple.com/be/app/ing-smart-banking-for-iphone/id437203741?mt=8' #ING
appmob[11,8]='https://itunes.apple.com/be/app/kbc-mobile/id458066754?mt=8' #KBC
appmob[12,8]='https://itunes.apple.com/be/app/keytrade-bank/id640974593?mt=8' #Keytrade
appmob[13,8]='https://itunes.apple.com/be/app/bank-de-kremer/id1382705162?mt=8' #Bank de Kremer
appmob[14,8]='https://itunes.apple.com/be/app/paschi-mobile/id1364879675?l=fr&mt=8' #Banca Monte Paschi Belgio
appmob[15,8]='https://itunes.apple.com/be/app/mybank-belgium/id1082668633' #Deutsche Bank
appmob[16,8]='https://itunes.apple.com/be/app/fintro-easy-banking-smartphone/id544288649?mt=8' #Fintro
appmob[17,8]='https://itunes.apple.com/be/app/nagelmackers/id885804394?mt=8' #Nagelmackers
appmob[18,8]='https://itunes.apple.com/be/app/mobile-vdk/id895434057?mt=8' #VDK
appmob[19,8]='https://itunes.apple.com/be/app/cph-mobile/id935210539?l=fr&mt=8' #CPH
appmob[20,8]='https://itunes.apple.com/be/app/beobank-mobile/id1008666594?mt=8' #Beobank

#PART2: All the values in a table
for(i in 1:nrow(appmob)){
  #col1
  wpg=read_html(appmob[i,7])
  bankg_b=html_nodes(wpg,'.AHFaub span')
  bankg=html_text(bankg_b)
  appmob[i,1]=bankg
  #col2
  if(appmob[i,7]!=0){
    wpg=read_html(appmob[i,7])
    rateg_b=html_nodes(wpg,'.BHMmbe')
    rateg=html_text(rateg_b)
    appmob[i,2]=rateg
  }
  #col3
  if(appmob[i,7]!=0){
    wpg=read_html(appmob[i,7])
    reviewg_b=html_nodes(wpg,'.hzfjkd+ span')
    reviewg=html_text(reviewg_b)
    reviewg=gsub("[[:punct:] ]+","",reviewg)
    appmob[i,3]=reviewg
  }
  #col4
  if(appmob[i,8]!=0){
    wpa=read_html(appmob[i,8])
    ratea_b=html_nodes(wpa,'.we-customer-ratings__averages__display')
    ratea=html_text(ratea_b)
    appmob[i,4]=ratea
  }
  #col5
  if(appmob[i,8]!=0){
    wpa=read_html(appmob[i,8])
    reviewa_b=html_nodes(wpa,'.we-customer-ratings__count')
    reviewa=html_text(reviewa_b)
    reviewa=reviewa[-2]
    reviewa=gsub("\\s*\\w*$", "", reviewa)
    if(grepl("\\.",reviewa)==TRUE){
      reviewa=gsub("[[:punct:] ]+","",reviewa)
      reviewa=gsub("K","00",reviewa)
    }
    if(grepl("\\.",reviewa)==FALSE){
      reviewa=gsub("[[:punct:] ]+","",reviewa)
      reviewa=gsub("K","000",reviewa)
    }
    appmob[i,5]=reviewa
  }
}


#PART3: Make the link with the sheet in the "Accounts products catalog" googlesheet
for_gs=gs_title("Accounts product catalog")
for_gs_sheet=gs_read(for_gs)
gs_edit_cells(for_gs, ws = "Mobile App", anchor = "B2", input = appmob[,1], byrow = FALSE)
gs_edit_cells(for_gs, ws = "Mobile App", anchor = "C2", input = appmob[,2], byrow = FALSE)
gs_edit_cells(for_gs, ws = "Mobile App", anchor = "D2", input = appmob[,3], byrow = FALSE)
gs_edit_cells(for_gs, ws = "Mobile App", anchor = "E2", input = appmob[,4], byrow = FALSE)
gs_edit_cells(for_gs, ws = "Mobile App", anchor = "F2", input = appmob[,5], byrow = FALSE)
