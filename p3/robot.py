import rg

class Robot:
    def act(self, game):
        # if there are enemies around, attack them
        all_locs = {(x, y) for x in xrange(19) for y in xrange(19)}
        spawn = {loc for loc in all_locs if 'spawn' in rg.loc_types(loc)}
        obstacle = {loc for loc in all_locs if 'obstacle' in rg.loc_types(loc)}
        team = {loc for loc in game.robots if game.robots[loc].player_id == self.player_id}
        enemy = set(game.robots)-team

        adjacent = set(rg.locs_around(self.location)) - obstacle
        adjacent_enemy = adjacent & enemy
        adjacent_enemy2 = {loc for loc in adjacent if (set(rg.locs_around(loc)) & enemy)} - team
        safe = adjacent - adjacent_enemy - adjacent_enemy2 - spawn 
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]
        	if bot.player_id != self.player_id:
            	if rg.dist(loc, self.location) <= 5:   
					return ['move', rg.toward(self.location, loc)]
        	if bot.player_id != self.player_id:
            	if rg.dist(loc, self.location) <= 1:
                 	if rg.settings.robot_hp<=15:
            			return ['suicide']

        if self.location == rg.CENTER_POINT:
            return ['move', rg.toward(self.location, (8, 6))]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]