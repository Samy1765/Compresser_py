import FreeSimpleGUI as gui
import zipfile as zf
import pathlib

def zip(filepaths,dict_path):
      dict=pathlib.Path(dict_path,"compressed.zip")
      with zf.ZipFile(dict,'w')as archieve:
          for file in filepaths:
              filepath=pathlib.Path(file)
              archieve.write(file,arcname=filepath.name)

lable1=gui.Text("Selet The File From Your Device: ")
input_txt1=gui.Input("File")
button1=gui.FileBrowse("Choose",key='file')

lable2=gui.Text("Selet The Folder To Save The : ")
input_txt2=gui.Input("File")
button2=gui.FolderBrowse("Choose",key='folder')

comb=gui.Button("Compress")

window=gui.Window("File Compresser",layout=[[lable1,input_txt1,button1],
                                            [lable2,input_txt2,button2],
                                            [comb]])
while True:
   event,values=window.read()
   if event==gui.WIN_CLOSED:
      break
   if event=='Compress':
      file_path=values['file']
      folder_path=values['folder']
      zip([file_path],folder_path)
      gui.popup("Compressed Successfully.")
window.close()