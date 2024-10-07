import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    


    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)

        self.image = pygame.image.load('Warrior_Blue_idle_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(*PLAYER_HITBOX_OFFSET)
       
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        
        # Player stats
        self.health = 100
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100        self.obstacle_sprites = obstacle_sprites
        
        # Inventory system
        self.inventory = []
        self.max_inventory_size = 20
        self.coins = 0    def input(self):
        
        # Magic system
        self.mana = 100
        self.max_mana = 100        keys = pygame.key.get_pressed()
        
        # Combat stats
        self.stamina = 100
        self.attack_power = 10
        self.defense = 5
        
        # Skills and systems
        self.skills = {}
        self.quests = []
        self.achievements = []        if keys[pygame.K_w] or keys[pygame.K_UP]:
        self.spells = []
        self.magic_power = 8            self.direction.y = -1
        self.reputation = 0
        self.karma = 0
        self.luck = 0        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        
        # Social systems
        self.guild = None
        self.friends = []
        self.energy = 100            self.direction.y = 1
        
        # Skill levels
        self.crafting_level = 1
        self.fishing_level = 1
        self.cooking_level = 1
        self.mining_level = 1        else:
        self.trading_level = 1
        self.social_level = 1
        self.diplomacy_level = 1            self.direction.y = 0
        
        # Companions
        self.pet = None
        self.mount = None
        
        # Advanced attributes
        self.leadership = 0
        self.charisma = 0        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        
        # Combat mechanics
        self.crit_chance = 0.1
        self.block_chance = 0.15            self.direction.x = 1
        
        # Professions
        self.alchemy_level = 1
        self.enchanting_level = 1
        self.blacksmithing_level = 1        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        
        # NPC interactions
        self.dialogue_history = []
        self.relationship_levels = {}            self.direction.x = -1
        
        # Transportation
        self.riding_level = 1
        self.vehicles_owned = []
        self.movement_speed_bonus = 0        else:
        
        # Construction
        self.construction_level = 1
        self.buildings_owned = []
        self.blueprint_collection = []            self.direction.x = 0
        
        # Economy
        self.bank_balance = 0
        self.trade_reputation = 0
        self.market_standing = {}
        
        # Battle system
        self.combo_count = 0
        self.battle_experience = 0
        self.fighting_style = "Balanced"    def move(self,speed):
        
        # Seasonal content
        self.seasonal_progress = {}
        self.event_participation = 0        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center


    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right #moving left

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update (self):
        self.input()
        self.move(self.speed)
    def get_position(self):
        """Get current player position."""
        return (self.rect.centerx, self.rect.centery)
    
    def get_tile_position(self):
        """Get current tile coordinates."""
        return (self.rect.centerx // TILESIZE, self.rect.centery // TILESIZE)
