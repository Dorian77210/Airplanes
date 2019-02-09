#!/Python
# -*-coding:Utf-8-*
import pygame;
from constantes import *;
from pygame.locals import *;
class Ship:

	def __init__(self):

		self.img = pygame.image.load("avion3.png").convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.center = ((width/2,height - self.rect.bottom));
		self.ok = 1;
		self.nbrMissile = 6;
		self.vie = 8;

	def ship_update(self,delta,direction):

		if direction == 'droite':

			if self.rect.right < width - 10:
				self.rect.x += 10;

		if direction == 'gauche':

			if self.rect.left > 10:
				self.rect.x -= 10;

	def ship_attack(self,liste,delta):

		if self.nbrMissile >0:
			bullet = Bullet(self,self.rect.x+55,self.rect.y-30,"bullet.png",1);
			liste.append(bullet);	
			self.nbrMissile -= 1;

class Ship_opponent:

	def __init__(self):

		self.img = pygame.image.load("avion2.png").convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.bottom = 60;
		self.rect.center = ((width/2, self.rect.bottom));
		self.ok = 1;
		self.nbrMissile = 6;
		self.vie = 8;

	def update_ship_opponent(self,delta,direction):
		
		if direction == 'droite':

			if self.rect.right < width - 10:
				self.rect.x += 10;

		if direction ==  'gauche':

			if self.rect.left > 10:
				self.rect.x -= 10;

	def ship_opponent_attack(self,liste,delta):
		if self.nbrMissile > 0:
			bullet = Bullet(self,self.rect.x+55,self.rect.y+110,"bullet2.png",0);
			liste.append(bullet);
			self.nbrMissile -= 1;
  
class Screen:

	def __init__(self):

		self.img = pygame.image.load("jungle.jpg").convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.top = 0;

	def update_background(self, delta):
		self.rect.y += int((SPEED * delta));
		if self.rect.y > 0:
			self.rect.bottom = height;

class Bullet:

	def __init__(self,ship,x,y,img,idi):

		self.img = pygame.image.load(img).convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.center = ((x, y));
		self.id = idi;
		self.ok = 1;

	def bullet_update(self,delta,ship,liste,bad_ship):
		delete_vies = 0;
		if self.id:
			
			if self.rect.bottom > 0:
				self.rect.y -= int(SPEED * delta * 3);
			elif self.rect.y < height:
				liste.remove(self);
				ship.nbrMissile += 1;
			if self.rect.colliderect(bad_ship):
				liste.remove(self);
				ship.nbrMissile += 1;
				delete_vies = 1;

			if delete_vies:
				bad_ship.vie -= 1;

		#vaisseau en haut
		elif self.id == 0:
			
			if self.rect.bottom < height:
				self.rect.y += int(SPEED * delta * 3);
			elif self.rect.y < height:
				liste.remove(self);
				ship.nbrMissile += 1;
			if self.rect.colliderect(bad_ship):
				liste.remove(self);
				ship.nbrMissile += 1;
				delete_vies = 1;

			if delete_vies:
				bad_ship.vie -= 1;
def end_wait(screen,ship,ship_opponent,string):
	end = True;
	font = pygame.font.Font(None,35);
	while end:

			pygame.time.Clock().tick(fps);
			texte3 = font.render(string, 1,(255,255,255));
			text = font.render("Press ESCAPE to retry... ",1,(255,255,255));
			screen.blit(texte3,((width/2 - 100),height/2));
			screen.blit(text, ((width /2 - 100), height / 2 + 40));
			liste_key = pygame.key.get_pressed();
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					end = False;
			pygame.display.flip();	


	return 1;	

