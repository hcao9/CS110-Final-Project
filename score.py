

class Score:
	def __init__(self):
		score = 0
		#black = (0,0,0)
		#smallfont = pygame.font.SysFont("comicsansms", 25)



	def score (score):
		with open(“score_record.txt”,”r”) as f:
			record=int(f.read())
		
		if score > record:
			with open(“score_record.txt”,”w”) as f:
				f.write(str(score))
				
		#text = smallfont.render("Score:  " + str(score), True, black)
		#gameDisplay.blit(text,[0,0])
		
	def getScore():
		return socore