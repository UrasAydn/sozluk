meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MVP":'En değerli oyuncu'
        
            } 
 kelime=input ('kelime girin') 
 
 if kelime in meme_dict.keys():
     print(meme_dict[kelime])
else
    print('kelime listede yok')
