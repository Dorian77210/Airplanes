#!/Python
# -*-coding:Utf-8-*
import pygame;
from pygame.locals import *;
from constantes import *;
import random;
from fonctions_objets import *;

def render_life(screen,ship,ship_opponent):
	end = 0;
	font = pygame.font.Font(None,25);
	texte1 = font.render("Nombre de vies : " + str(ship.vie), 1,(255,0,0));
	texte2 = font.render("Nombre de vies : " + str(ship_opponent.vie), 1,(255,0,0));
	text = font.render("Press ESCAPE to quit...",1,(41,19,189));
	texte4 = font.render("Nombre de munitions : " + str(ship.nbrMissile), 1,(255,0,0));
	texte5 = font.render("Nombre de munitions : " +str(ship_opponent.nbrMissile),1,(255,0,0));
	if ship.vie == 0:
		end = end_wait(screen,ship,ship_opponent,"Le joueur 2 a gagne !!");
		if end:
			create_actors();
	elif ship_opponent.vie == 0:
		end = end_wait(screen,ship,ship_opponent, "Le joueur 1 a gagne !!");
		if end:
			create_actors();
	elif ship.vie == 0 and ship_opponent.vie == 0:
		end = end_wait(screen,ship,ship_opponent,"Egalite parfaite !!");
		if end:
			create_actors();
	screen.blit(texte2, (20,10));
	screen.blit(texte1,(20,560));
	screen.blit(texte4,(275,560));
	screen.blit(texte5, (275,10));
def create_actors():

	#background
	global object_list;
	object_list = [];
	global screen_show;
	screen_show = Screen();
	object_list.append(screen_show);
	global ship;
	ship = Ship();
	object_list.append(ship);
	global ship_opponent;
	ship_opponent = Ship_opponent();
	object_list.append(ship_opponent);

	
def action_event(liste_key,delta):
	global screen;
	if liste_key[K_RIGHT]:

		if liste_key[K_d]:
			ship_opponent.update_ship_opponent(delta,'droite');
		if liste_key[K_q]:
			ship_opponent.update_ship_opponent(delta,'gauche');
		if liste_key[K_UP]:
			ship.ship_attack(object_list,delta);
		ship.ship_update(delta, 'droite');
		if liste_key[K_a]:
			ship_opponent.ship_opponent_attack(object_list,delta);

	elif liste_key[K_LEFT]:

		if liste_key[K_q]:
			ship_opponent.update_ship_opponent(delta,'gauche');
		if liste_key[K_d]:
			ship_opponent.update_ship_opponent(delta,'droite');
		if liste_key[K_UP]:
			ship.ship_attack(object_list,delta);
		if liste_key[K_a]:
			ship_opponent.ship_opponent_attack(object_list,delta);
		ship.ship_update(delta, 'gauche');

	elif liste_key[K_UP]:
		if liste_key[K_a]:
			ship_opponent.ship_opponent_attack(object_list,delta);
		if liste_key[K_q]:
			ship_opponent.update_ship_opponent(delta,'gauche');
		if liste_key[K_d]:
			ship_opponent.update_ship_opponent(delta,'droite');
		ship.ship_attack(object_list,delta);

	elif liste_key[K_q]:

		if liste_key[K_a]:
			ship_opponent.ship_opponent_attack(object_list,delta);

		ship_opponent.update_ship_opponent(delta, 'gauche');

	elif liste_key[K_d]:

		if liste_key[K_a]:
			
			ship_opponent.ship_opponent_attack(object_list,delta);
		ship_opponent.update_ship_opponent(delta,'droite');

	elif liste_key[K_a]:

		ship_opponent.ship_opponent_attack(object_list,delta);

def action_update(delta):
	
	screen_show.update_background(delta);
#########################################

##########################################
def render_update(screen):

	screen.fill((0,0,0));
	for elt in object_list:
		screen.blit(elt.img, elt.rect);	
		if type(elt) is Bullet and elt.id and elt.ok:
			elt.bullet_update(delta_s,ship,object_list,ship_opponent);
		elif type(elt) is Bullet and not elt.id and elt.ok:
			elt.bullet_update(delta_s,ship_opponent,object_list,ship);
		elif type(elt) is Ship and not elt.ok:
			object_list.remove(elt);
		elif type(elt) is Ship_opponent and not elt.ok:
			object_list.remove(elt);

	render_life(screen,ship,ship_opponent);
	pygame.display.flip();	
###########################################

############################################
def main():
	global screen;
	pygame.init();
	running = True;
	screen = pygame.display.set_mode((width,height));
	
	pygame.display.set_caption("Airplane Fight");
	create_actors();
	pygame.key.set_repeat(30,30);
	while running:
		global delta_s;
		delta_s = pygame.time.Clock().tick(fps) / 1000;
		liste_key = pygame.key.get_pressed();
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False;

		action_event(liste_key,delta_s);
		action_update(delta_s);
		render_update(screen);
	
	return 0;

main();