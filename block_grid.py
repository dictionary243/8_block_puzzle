from PIL import Image,ImageDraw,ImageFont
import time

def puzzle_viewer(state):
    img=Image.new('RGB',(300,300),color='white')
    d=ImageDraw.Draw(img)
    #font = ImageFont.truetype('FreeSerif.ttf', 30)
    #font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
    font=ImageFont.load_default()
    font.set
    for i in range(3):
        for j in range(3):
            color='white'
            if(state[i][j]!='_'):
                color='grey'
                d.rectangle([(100*j,100*i),(100*(j+1),((i+1)*100))],fill=color,outline='black')
                d.text([(100*j+10,100*i+10)],str(state[i][j]),fill='black',font=font)
            else:
                d.rectangle([(100*j,100*i),(100*(j+1),((i+1)*100))],fill=color,outline='black')
    img.show()
    time.sleep(5)
    img.close()
