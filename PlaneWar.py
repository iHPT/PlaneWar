# -*- coding: utf-8 -*-

import time, random

import pygame
from pygame.locals import *


def keyControl(heroPlane):
	for event in pygame.event.get():
		if event.type == QUIT:	
			print('exit.')
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_a or event.key == K_LEFT:
				#print('left')
				heroPlane.moveLeft()
			elif event.key == K_d or event.key == K_RIGHT:
				#print('right')
				heroPlane.moveRight()
			elif event.key == K_SPACE:
				#print('space')
				heroPlane.fire()

class BasePlaneAndBullet(object):
	"""docstring for BasePlaneAndBullet"""
	def __init__(self, screen, x, y, imageName):
		self.x = x
		self.y = y
		self.screen = screen
		self.image = pygame.image.load(imageName)
		
		

class BasePlane(BasePlaneAndBullet):
	"""docstring for BasePlane"""
	def __init__(self, screen, x, y, imageName):
		super(BasePlane, self).__init__(screen, x, y, imageName)
		self.bulletList = []
	
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		# 显示子弹
		for bullet in self.bulletList:
			if bullet.judge():
				self.bulletList.remove(bullet)
			bullet.display()
			bullet.move()
		

class HeroPlane(BasePlane):
	"""docstring for HeroPlane"""
	def __init__(self, screen, x, y):
		super(HeroPlane, self).__init__(screen, x, y ,'./images/hero1.png')
	
	def moveLeft(self):
		self.x -= 10

	def moveRight(self):
		self.x += 10

	def fire(self):
		bullet = Bullet(self.screen, self.x, self.y)
		self.bulletList.append(bullet)


class EnemyPlane(BasePlane):
	"""docstring for EnemyPlane"""
	def __init__(self, screen, x, y):
		super(EnemyPlane, self).__init__(screen, x, y, './images/enemy0.png')
		self.direction = 'right'
	
	def move(self):
		#self.y += 10
		if self.direction == 'right':
			self.x += 3
		else:
			self.x -= 3

		if self.x >= 360:
			self.direction = 'left'
		elif self.x <= 0:
			self.direction = 'right'

	def fire(self):
		randomNum = random.randint(0, 100)
		if randomNum == 20 or randomNum == 50 or randomNum == 80:
			enemyBullet = EnemyBullet(self.screen, self.x, self.y, './images/bullet1.png')
			self.bulletList.append(enemyBullet)


class BaseBullet(BasePlaneAndBullet):
	"""docstring for BaseBullet"""
	def __init__(self, screen, x, y, imageName):
		super(BaseBullet, self).__init__(screen, x, y, imageName)
		
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

	def move(self):
		self.y += 5


class Bullet(BaseBullet):
	"""docstring for Bullet"""
	def __init__(self, screen, x, y):
		super(Bullet, self).__init__(screen, x + 40, y - 25, './images/bullet.png')

	def move(self):
		self.y -= 5
	
	def judge(self):
		if self.y <= -22: # 子弹高度22
			return True
		else:
			return False


class EnemyBullet(BaseBullet):
	"""docstring for EnemyBullet"""
	def __init__(self, screen, x, y, imageName):
		super(EnemyBullet, self).__init__(screen, x + 25, y + 40, './images/bullet1.png')
	
	# def move(self):
	# 	self.y += 5

	def judge(self):
		if self.y >= 721: # 子弹高度21
			return True
		else:
			return False


def main():
	screen = pygame.display.set_mode((400, 700), 0, 32)
	background = pygame.image.load('./images/background.png')
	# hero
	hero = HeroPlane(screen, 150, 580)

	enemyPlane = EnemyPlane(screen, 0, 0)

	while True:
		screen.blit(background, (0, 0))

		hero.display()
		enemyPlane.display()
		enemyPlane.fire()
		enemyPlane.move()

		pygame.display.update()
		keyControl(hero)
		time.sleep(0.01)


if __name__ == '__main__':
	main()

