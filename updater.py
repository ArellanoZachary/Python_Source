import webbrowser
def main():
  
  print('Which program would you like to download? \n' +\
        '\n' +\
        '1. Java 64 Bit \n' +\
        '2. Java 32 Bit \n' +\
        '3. Adobe Reader \n' +\
        '4. Microsoft Silverlight (windows 10 only) \n' +\
        '5. VLC media player'
        '6. I\'m ready to quit'
        '\n')
        
  answer = input('Please type in the number associated with the program, ex. 1 for Java 64 Bit. ')
  
  new = 2
    
  while answer not in ['1','2','3','4','5']:
    answer = input('Error you did not input a number between 1-5, Please input a choice between 1-5. ')
  if answer == '1':
    print('Answer is Java 64 Bit')
    url = 'http://javadl.oracle.com/webapps/download/AutoDL?BundleId=230542_2f38c3b165be4555a1fa6e98c45e0808'
    webbrowser.open(url,new==new)
  elif answer =='2':
    print('Answer is Java 32 Bit')
    url = 'http://javadl.oracle.com/webapps/download/AutoDL?BundleId=230539_2f38c3b165be4555a1fa6e98c45e0808'
    webbrowser.open(url,new==new)
  elif answer == '3':
    print('Answer is Adobe Reader')
    url = 'https://get.adobe.com/reader/'
    webbrowser.open(url,new==new)
  elif answer == '4':
    print('Answer is Microsoft Silverlight')
    url = 'http://go.microsoft.com/fwlink/?LinkID=229321'
    webbrowser.open(url,new==new)
  elif answer == '5':
    print('Now installing VLC media player')
    url = 'https://get.videolan.org/vlc/2.2.8/win32/vlc-2.2.8-win32.exe'
    webbrowser.open(url,new==new)
  else:
    print('Now quiting')
    
main()
