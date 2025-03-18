###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("flowers")

q1=codesters.Square(100,100,200, 'pink')
q2=codesters.Square(-100,100,200, 'pink')
q3=codesters.Square(-100,-100,200, 'pink')
q4=codesters.Square(100,-100,200, 'pink')

s1=codesters.Sprite("nfr",100,100)
s1.set_size(0.25)
s2=codesters.Sprite("brandy",100,-100)
s2.set_size(0.25)
s3=codesters.Sprite("phl",-100,-100)
s3.set_size(0.28)
s4=codesters.Sprite("flw",-100,100)
s4.set_size(0.32)

message1=codesters.Text("sarani bohacek",0,220,"pink")
message2=codesters.Text("yay!!",0,-220,"pink")