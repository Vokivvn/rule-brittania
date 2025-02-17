# Dynamic Variables


    Dynamic variables are read only variables that can be used in effects & triggers that accept variables.
    When they are used, the game will compute and return the value of the dynamic variable.
## Table of Content

* [global](#dynamic-variables-for-scope-global)
* [country](#dynamic-variables-for-scope-country)
* [state](#dynamic-variables-for-scope-state)
* [unit_leader](#dynamic-variables-for-scope-unit_leader)

## Dynamic variables for scope global

### year
* description: current year

### operations
* description: array of objects in operations database

### majors
* description: get array of all majors (including non existing

### num_days
* description: current total days

### date
* description: get date value that can be comparable to other date values and localized using GetDateString/GetDateStringShortMonth/GetDateStringNoHour/GetDateStringNoHourLong scripted locs

### threat
* description: check the global threat value. 0-1 value
* (Auto generated using the trigger with same name)

### countries
* description: get array of all countries (including non existing

### ideology_groups
* description: array of objects in ideology_groups database

### difficulty
* description: check if the difficulty is above or below specified value 0-2 (difficulty enum). Example: difficulty > 0 (above easy)
* (Auto generated using the trigger with same name)

## Dynamic variables for scope country

### political_power
* description: total political power of country

### resource_consumed
* description: number of resources consumed by country, resource type is defined in target resource_consumed@steel

### manpower
* description: DEPRECATED, MAY OVERFLOW. total manpower of country

### air_intel
* description: air intel against a target country. example GER.air_intel@ENG

### overlord
* description: master of this subject

### num_of_nukes
* description: check amount of nukes
* (Auto generated using the trigger with same name)

### command_power
* description: total command power of country

### enemies_of_allies
* description: array of enemies of allies

### owned_controlled_states
* description: array owned and core states

### navy_intel
* description: navy intel against a target country. example GER.navy_intel@ENG

### manpower_k
* description: total manpower of country in thousands

### num_battalions
* description: number of battalions

### max_manpower
* description: DEPRECATED, MAY OVERFLOW. maximum manpower of country

### faction_members
* description: array of faction members

### fuel_k
* description: total fuel of country in thousands

### max_fuel_k
* description: max fuel of country in thousands

### num_owned_controlled_states
* description: number of owned and core states

### agency_upgrade_number
* description: Checks the number of upgrade done in the intelligence agency. 
agency_upgrade_number > 4
* (Auto generated using the trigger with same name)

### max_available_manpower
* description: DEPRECATED, MAY OVERFLOW. total available manpower of country

### ai_strategy_dont_defend_ally_borders
* description: ai strategy value dont_defend_ally_borders against country. Example: GER.ai_strategy_dont_defend_ally_borders@ENG

### max_available_manpower_k
* description: total available manpower of country in thousands

### opinion
* description: opinion of a country targeted on another one. example GER.opinion@ENG

### owned_states
* description: array of owned states

### max_manpower_k
* description: maximum manpower of country in thousands

### any_war_score
* description: compares the warscore of all wars in a country to see if any fullfills the comparison condition 0-100 - Example: any_war_score > 40
* (Auto generated using the trigger with same name)

### num_armies
* description: number of armies

### ai_strategy_ignore_claim
* description: ai strategy value ignore_claim against country. Example: GER.ai_strategy_ignore_claim@ENG

### party_popularity
* description: popularity of targeted party [0.00, 1.00]. example party_popularity@democratic. May also target ruling_party. This also supports country variables, so you can party_popularity@my_var_name for variables that store ideologies

### num_ships
* description: number of ships

### enemies_naval_strength_ratio
* description: Compares the estimated navy strength between the scope country and all its enemies
* (Auto generated using the trigger with same name)

### num_deployed_planes
* description: number of deployed planes

### command_power_daily
* description: Checks if daily command power increase is more or less that specified value 
 command_power_daily > 1.5
* (Auto generated using the trigger with same name)

### num_deployed_planes_with_type
* description: number of deployed planes with equipment type. example num_deployed_planes_with_type@fighter

### legitimacy
* description: legitimacy of scope country. -1 if not an exile

### num_armies_in_state
* description: number of armies in state, state is in target. example num_armies_in_state@123

### num_ships_with_type
* description: number of ships controlled in country, ship type is defined in target. example num_ships_with_type@carrier. can be a sub unit def type or one of carrier,capital,screen, submarine

### num_armies_with_type
* description: number of armies with dominant type, dominant type is defined in target. example: num_armies_with_type@light_armor

### army_intel
* description: army intel against a target country. example GER.army_intel@ENG

### num_battalions_with_type
* description: number of battalions with sub unit type, sub unit type is defined in target. example: num_battalions_with_type@light_armor

### civilian_intel
* description: civilian intel against a target country. example GER.civilian_intel@ENG

### stability
* description: stability of a country

### modifier
* description: a modifier stored in country scope

### highest_party_ideology
* description: ideology of the most popular party. Can exclude the ruling party by using @exclude_ruling_party. Example: highest_party_ideology OR highest_party_ideology@exclude_ruling_party

### highest_party_popularity
* description: popularity size of the most popular party [0.00, 1.00]. Can exclude the ruling party by using @exclude_ruling_party. Example: highest_party_popularity OR highest_party_popularity@exclude_ruling_party

### neighbors_owned
* description: array of neighbors to owned states

### current_party_ideology_group
* description: returns the token for current party ideology group

### alliance_naval_strength_ratio
* description: Compares the estimated naval strength between the scope country, his allies and his enemies.
* (Auto generated using the trigger with same name)

### resource
* description: number of surplus resources in country, resource type is defined in target resource@steel

### num_controlled_states
* description: number of controlled states

### controlled_states
* description: array of controlled states

### potential_and_current_enemies
* description: array of potential and actual enemies

### capital
* description: capital state of the country

### encryption_strength
* description: total encryption strength of a country that is needed

### num_owned_states
* description: number of owned states

### resource_produced
* description: number of resources produced by country, resource type is defined in target. example resource_produced@steel

### core_resistance
* description: returns core resistance of target country

### num_core_states
* description: number of core states

### ai_attitude_wants_antagonize
* description: returns 1 if ai wants antagonize

### core_states
* description: array of core states

### enemies
* description: array of enemies at war with

### subjects
* description: array of subjects

### neighbors
* description: array of neighbors

### host
* description: exile host of this country

### exiles
* description: exile host of this country

### days_mission_timeout
* description: timeout in days for a specific timed mission, mission type token is defined in target. example: days_mission_timeout@GER_mefo_bills_mission

### allies
* description: array of allies (faction members). prefer using faction_members instead

### faction_leader
* description: faction leader of this country's faction

### ai_attitude_protective_weight
* description: weight for an ai attitude attitude_protectiveagainst country. Example: GER.ai_attitude_protective_weight@ENG

### resource_exported
* description: number of resources exported by country, resource type is defined in target resource_exported@steel

### num_equipment_in_armies
* description: number of equipment in armies of the country, equipment type token is defined in target. example num_equipment_in_armies@infantry_equipment

### resource_imported
* description: number of resources imported by country, resource type is defined in target resource_imported@steel

### num_target_equipment_in_armies
* description: number of equipment required in armies of the country, equipment type token is defined in target. example num_target_equipment_in_armies@infantry_equipment

### num_equipment
* description: number of equipment in country. example num_equipment@infantry_equipment

### num_of_operatives
* description: Checks the number of operatives the country controls
* (Auto generated using the trigger with same name)

### num_equipment_in_armies_k
* description: number of equipment in armies of the country in thousands, equipment type token is defined in target. example num_equipment_in_armies_k@infantry_equipment

### num_target_equipment_in_armies_k
* description: number of equipment required in armies of the country in thousands, equipment type token is defined in target. example num_target_equipment_in_armies_k@infantry_equipment

### autonomy_ratio
* description: autonomy of scope country. -1 if not a subject

### ai_attitude_wants_weaken
* description: returns 1 if ai wants weaken

### ai_attitude_wants_ally
* description: returns 1 if ai wants ally

### ai_attitude_wants_protect
* description: returns 1 if ai wants protect

### ai_attitude_wants_ignore
* description: returns 1 if ai wants ignore

### ai_attitude_is_threatened
* description: returns 1 if ai is threatened

### core_compliance
* description: returns core compliance of target country

### occupied_countries
* description: array of occupied countries

### original_tag
* description: returns the original tag of a country

### decryption_speed
* description: total encryption strength of a country that is needed

### cryptology_defense_level
* description: cryptology defense level of a country

### army_leaders
* description: all army leaders of a country

### navy_leaders
* description: all navy leaders of a country

### operatives
* description: all operatives of a country

### num_of_military_factories
* description: check amount of military factories
* (Auto generated using the trigger with same name)

### num_of_civilian_factories
* description: check amount of civilian factories
* (Auto generated using the trigger with same name)

### num_of_naval_factories
* description: check amount of naval factories
* (Auto generated using the trigger with same name)

### foreign_manpower
* description: check the amount of foreign garrison manpower we have
* (Auto generated using the trigger with same name)

### has_manpower
* description: check amount of manpower
* (Auto generated using the trigger with same name)

### num_subjects
* description: check the number of subjects of nation
* (Auto generated using the trigger with same name)

### has_political_power
* description: check amount of political power
* (Auto generated using the trigger with same name)

### num_of_available_military_factories
* description: check amount of available military factories
* (Auto generated using the trigger with same name)

### num_of_available_naval_factories
* description: check amount of available naval factories
* (Auto generated using the trigger with same name)

### num_of_available_civilian_factories
* description: check amount of available civilian factories
* (Auto generated using the trigger with same name)

### surrender_progress
* description: check if a country is close to surrendering
* (Auto generated using the trigger with same name)

### political_power_daily
* description: Checks if daily political power increase is more or less that specified value 
 political_power_daily > 1.5
* (Auto generated using the trigger with same name)

### land_doctrine_level
* description: checks researched land doctrine level
* (Auto generated using the trigger with same name)

### casualties
* description: Check the amount of casualties a country has suffered in all of it's wars
* (Auto generated using the trigger with same name)

### num_of_factories
* description: check amount of total factories
* (Auto generated using the trigger with same name)

### num_of_controlled_states
* description: check amount of controlled stats
* (Auto generated using the trigger with same name)

### has_added_tension_amount
* description: Compare if the country has added above or below the specified ammount of tension
* (Auto generated using the trigger with same name)

### ai_irrationality
* description: check the ai irrationality value
* (Auto generated using the trigger with same name)

### ai_strategy_antagonize
* description: ai strategy value antagonize against country. Example: GER.ai_strategy_antagonize@ENG

### num_divisions
* description: Will compare towards the amount of divisions a country has control over, if strength matters use has_army_size.
* (Auto generated using the trigger with same name)

### original_research_slots
* description: check number of research slots at start of game
* (Auto generated using the trigger with same name)

### ai_wants_divisions
* description: Will compare towards the amount of divisions an ai wants to have.
* (Auto generated using the trigger with same name)

### alliance_strength_ratio
* description: Compares the estimated army strength between the scope country, his allies and his enemies.
* (Auto generated using the trigger with same name)

### num_faction_members
* description: Compares the number of members in the faction for the current country. 
 Example: num_faction_members > 10
* (Auto generated using the trigger with same name)

### enemies_strength_ratio
* description: Compares the estimated army strength between the scope country and all its enemies
* (Auto generated using the trigger with same name)

### compare_autonomy_progress_ratio
* description: check if autonomy progress ratio is higher than value, example:
compare_autonomy_progress_ratio > 0.5
* (Auto generated using the trigger with same name)

### num_tech_sharing_groups
* description: checks how many groups a nation is a member of
* (Auto generated using the trigger with same name)

### ai_strategy_invade
* description: ai strategy value invade against country. Example: GER.ai_strategy_invade@ENG

### num_occupied_states
* description: check the number of states occupied by nation
* (Auto generated using the trigger with same name)

### amount_research_slots
* description: check number of research current research slots 
 amount_research_slots > 2
* (Auto generated using the trigger with same name)

### manpower_per_military_factory
* description: Number of available manpower per factory the country has. Excluding dockyards.
manpower_per_military_factory < 1000
* (Auto generated using the trigger with same name)

### has_stability
* description: check value of stability 0-1: Example has_stability < 0.6
* (Auto generated using the trigger with same name)

### has_war_support
* description: check value of war_support 0-1: Example has_war_support < 0.6
* (Auto generated using the trigger with same name)

### num_of_civilian_factories_available_for_projects
* description: check amount of civilian factories available for a new project to use
* (Auto generated using the trigger with same name)

### political_power_growth
* description: Check the value of political power daily growth.Exacmple: political_power_growth > 0
* (Auto generated using the trigger with same name)

### amount_manpower_in_deployment_queue
* description: Checks for amount manpower currently in deploymentview. amount_manpower_in_training > 10
* (Auto generated using the trigger with same name)

### has_legitimacy
* description: Check scope country legitimacy 0-100: Example has_legitimacy < 60
* (Auto generated using the trigger with same name)

### casualties_k
* description: Check the amount of casualties in thousands a country has suffered in all of it's wars
* (Auto generated using the trigger with same name)

### fuel_ratio
* description: Compares the fuel ratio to a variable.
Example: fuel_ratio > 0.5
* (Auto generated using the trigger with same name)

### days_since_capitulated
* description: Checks the number of days since the country last capitulated, even if it is no longer capitulated.
	If it has not ever capitulated, the value is extremely large.
	It is recommended to combine this with has_capitulated = yes when you specifically want to ignore non-active capitulations.
Examples:
	HOL = { has_capitulated = yes days_since_capitulated > 60 } # The Netherlands has been capitulated for more than two months
	FRA = { has_capitulated = yes days_since_capitulated < 21 } # France has capitulated sometime within the past three weeks
	GER = { OR = { has_capitulated = no days_since_capitulated > 14 } } # Germany is not both actively and recently capitulated

* (Auto generated using the trigger with same name)

### mine_threat
* description: A trigger to check how dangerous enemy mines are for a country. Controlled by NAVAL_MINE_DANGER defines. Returns a value between 0 and 1. Example mine_threat > 0.5 
* (Auto generated using the trigger with same name)

### convoy_threat
* description: A trigger to check convoy threat for a country. Controlled by NAVAL_CONVOY_DANGER defines. Returns a value between 0 and 1. Example convoy_threat > 0.5 
* (Auto generated using the trigger with same name)

### decryption_progress
* description: checks decryption ratio against a country. Example: 
decryption_progress = { 
 target = GER
 value > 0.5
} 
#or decryption_progress@GER as variable

* (Auto generated using the trigger with same name)

### garrison_manpower_need
* description: check the amount of manpower needed by garrisons
* (Auto generated using the trigger with same name)

### num_operative_slots
* description: Checks the number of available operative slots a country has.
If this differs from the number of operative, this does not mean the country can recruit an operative, but that it will eventually be able to.
* (Auto generated using the trigger with same name)

### num_free_operative_slots
* description: Checks the number of operative a country can recruit right now.
Note that this is not necessarily greater than zero if num_operative_slots returned a number greater than the number of operative.
* (Auto generated using the trigger with same name)

### num_fake_intel_divisions
* description: Will compare towards the amount of fake intel divisions a country has control over. .
* (Auto generated using the trigger with same name)

### has_collaboration
* description: checks the collaboration in a target country with our currently scoped country. Example: 
has_collaboration = { 
 target = GER
 value > 0.5
} 
#or has_collaboration@GER as variable

* (Auto generated using the trigger with same name)

### conscription_ratio
* description: Checks  conscription ratio of the country compared to target conscription ratio.

* (Auto generated using the trigger with same name)

### target_conscription_amount
* description: Checks the target conscription amount of the country.

* (Auto generated using the trigger with same name)

### current_conscription_amount
* description: Checks the current conscription amount of the country.

* (Auto generated using the trigger with same name)

### network_national_coverage
* description: checks network national coverage you have over a country. Example: 
network_national_coverage = { 
 target = GER
 value > 0.5
} 

* (Auto generated using the trigger with same name)

### ai_strategy_conquer
* description: ai strategy value conquer against country. Example: GER.ai_strategy_conquer@ENG

### ai_strategy_befriend
* description: ai strategy value befriend against country. Example: GER.ai_strategy_befriend@ENG

### ai_strategy_consider_weak
* description: ai strategy value consider_weak against country. Example: GER.ai_strategy_consider_weak@ENG

### ai_strategy_protect
* description: ai strategy value protect against country. Example: GER.ai_strategy_protect@ENG

### ai_strategy_alliance
* description: ai strategy value alliance against country. Example: GER.ai_strategy_alliance@ENG

### ai_strategy_contain
* description: ai strategy value contain against country. Example: GER.ai_strategy_contain@ENG

### ai_strategy_support
* description: ai strategy value support against country. Example: GER.ai_strategy_support@ENG

### ai_strategy_force_defend_ally_borders
* description: ai strategy value force_defend_ally_borders against country. Example: GER.ai_strategy_force_defend_ally_borders@ENG

### ai_strategy_influence
* description: ai strategy value influence against country. Example: GER.ai_strategy_influence@ENG

### ai_strategy_ignore
* description: ai strategy value ignore against country. Example: GER.ai_strategy_ignore@ENG

### ai_strategy_send_volunteers_desire
* description: ai strategy value send_volunteers_desire against country. Example: GER.ai_strategy_send_volunteers_desire@ENG

### ai_strategy_occupation_policy
* description: ai strategy value occupation_policy against country. Example: GER.ai_strategy_occupation_policy@ENG

### ai_strategy_declare_war
* description: ai strategy value declare_war against country. Example: GER.ai_strategy_declare_war@ENG

### ai_strategy_prepare_for_war
* description: ai strategy value prepare_for_war against country. Example: GER.ai_strategy_prepare_for_war@ENG

### ai_strategy_decrypt_target
* description: ai strategy value decrypt_target against country. Example: GER.ai_strategy_decrypt_target@ENG

### ai_strategy_activate_crypto
* description: ai strategy value activate_crypto against country. Example: GER.ai_strategy_activate_crypto@ENG

### ai_attitude_neutral_weight
* description: weight for an ai attitude attitude_neutralagainst country. Example: GER.ai_attitude_neutral_weight@ENG

### ai_attitude_hostile_weight
* description: weight for an ai attitude attitude_hostileagainst country. Example: GER.ai_attitude_hostile_weight@ENG

### ai_attitude_friendly_weight
* description: weight for an ai attitude attitude_friendlyagainst country. Example: GER.ai_attitude_friendly_weight@ENG

### ai_attitude_outraged_weight
* description: weight for an ai attitude attitude_outragedagainst country. Example: GER.ai_attitude_outraged_weight@ENG

### ai_attitude_threatened_weight
* description: weight for an ai attitude attitude_threatenedagainst country. Example: GER.ai_attitude_threatened_weight@ENG

### ai_attitude_allied_weight
* description: weight for an ai attitude attitude_alliedagainst country. Example: GER.ai_attitude_allied_weight@ENG

## Dynamic variables for scope state

### arms_factory_level
* description: military factory level in the state

### damaged_building_level
* description: damaged building level of a building with type, uses target as building type. example damaged_building_level@arms_factory

### modifier
* description: value of modifier stored in this state, uses target as modifier token, example: 123.modifier@local_manpower

### industrial_complex_level
* description: civilian factor level in the state

### core_countries
* description: countries that cores the state

### infrastructure_level
* description: infrastructure level in the state

### days_since_last_strategic_bombing
* description: Checks the days since last strategic bombing.
days_since_last_strategic_bombing < 10

* (Auto generated using the trigger with same name)

### distance_to
* description: distance to another state, uses target as another state. example: 123.distance_to@124

### non_damaged_building_level
* description: non damaged building level of a building with type, uses target as building type. example non_damaged_building_level@arms_factory

### building_level
* description: building level of a building with type, uses target as building type. example building_level@arms_factory

### resource
* description: resources produced in state. example resource@steel

### owner
* description: owner of the state

### controller
* description: controller of the state

### resistance
* description: Compares the current resistance level of a state to a value. Example: resistance > 50 
* (Auto generated using the trigger with same name)

### state_population
* description: check the population in the state
* (Auto generated using the trigger with same name)

### state_strategic_value
* description: Checks for state strategic value
* (Auto generated using the trigger with same name)

### state_and_terrain_strategic_value
* description: Checks for state strategic value
* (Auto generated using the trigger with same name)

### state_population_k
* description: check the population in the state in thousands (use to avoid variable overflows)
* (Auto generated using the trigger with same name)

### compliance
* description: Compares the current compliance level of a state to a value. Example: compliance > 50 
* (Auto generated using the trigger with same name)

### compliance_speed
* description: Compares the current compliance speed of a state to a value. Example: compliance_speed > 50 
* (Auto generated using the trigger with same name)

### resistance_speed
* description: Compares the current resistance speed of a state to a value. Example: resistance_speed > 50 
* (Auto generated using the trigger with same name)

### resistance_target
* description: Compares the target resistance level of a state to a value. Example: resistance_target > 50 
* (Auto generated using the trigger with same name)

## Dynamic variables for scope unit_leader

### num_units
* description: number of units controlled by leader

### num_units_with_type
* description: number of units with dominant type controlled by leader, dominant type is defined in target. example: num_units_with_type@light_armor

### has_orders_group
* description: 1 if leader has orders group, zero otherwise

### num_units_in_state
* description: number of units controlled by leader in state, state is in target. example num_units_in_state@123

### num_rocket
* description: number of units with rocket dominant type

### num_equipment
* description: number of equipment in army of a leader, equipment type token is defined in target. example num_equipment@infantry_equipment

### num_max_traits
* description: number of maximum assignable traits a leader can have

### num_cavalry
* description: number of units with cavalry dominant type

### avg_units_acclimation
* description: average unit acclimatization for a specific climate, acclimatization type is defined in target. example avg_units_acclimation@cold_climate

### num_artillery
* description: number of units with artillery dominant type

### num_target_equipment
* description: number of equipment required in army of a leader, equipment type token is defined in target. example num_target_equipment@infantry_equipment

### logistics_level
* description: logistics level of the leader

### num_infantry
* description: number of units with infantry dominant type

### num_units_defensive_combats_on
* description: number of units that are defensively fighting on a terrain, terrain type is defined as target. example: num_units_defensive_combats_on@plains

### num_ships_with_type
* description: number of ships controlled by leader, ship type is defined in target. example num_ships_with_type@carrier

### own_capture_chance_factor
* description: The chance this operative has to be captured, taking into account the country it is operating for and the country it is operating against.

### num_ships
* description: number of ships controlled by leader

### num_armored
* description: number of units with armored dominant type

### num_battalions
* description: number of battalions

### num_special
* description: number of units with special dominant type

### num_mechanized
* description: number of units with mechanized dominant type

### attack_level
* description: attack level of the leader

### num_personality_traits
* description: number of personality traits a leader has

### num_motorized
* description: number of units with motorized dominant type

### maneuvering_level
* description: maneuvering level of the leader

### num_battalions_with_type
* description: number of battalions with sub unit type, sub unit type is defined in target. example: num_battalions_with_type@light_armor

### own_harmed_time_factor
* description: The time factor applied to the status "harmed". Takes int accountthe country it is operating for and the country it is operating against.

### num_battle_plans
* description: number of battle plans of unit leader

### avg_defensive_combat_status
* description: average progress of defensive combats

### num_traits
* description: number of traits a leader has

### num_status_traits
* description: number of status traits a leader has

### defense_skill_level
* description: Compares defense skill level of a unit leader.
Example: defense_skill_level > 5
* (Auto generated using the trigger with same name)

### num_assigned_traits
* description: number of assigned traits the leader has

### leader_modifier
* description: value of a modifier stored in leader modifier, modifier token is defined in target. example leader_modifier@navy_max_range

### num_terrain_traits
* description: number of terrain traits a leader has

### avg_unit_planning_ratio
* description: average planning ratio of all units

### num_basic_traits
* description: number of basic traits a leader has

### skill_level
* description: skill level of the leader

### army_attack_level
* description: attack level of the leader

### attack_skill_level
* description: Compares attack skill level of a unit leader.
Example: attack_skill_level > 5
* (Auto generated using the trigger with same name)

### army_defense_level
* description: defense level of the leader

### defense_level
* description: defense level of the leader

### planning_level
* description: planning level of the leader

### avg_combat_status
* description: average progress of all combats

### coordination_level
* description: coordination level of the leader

### operation_state
* description: the state location the operative is assigned. 0 if it is not assigned to a state

### average_stats
* description: average stats of unit leader

### avg_offensive_combat_status
* description: average progress of offensive combats

### operation_type
* description: returns the operation token the operative is assigned

### sum_unit_terrain_modifier
* description: sum of terrain modifiers of each army's location, terrain type is defined in target. example: sum_unit_terrain_modifier@sickness_chance 

### unit_modifier
* description: value of a modifier stored in unit modifier, modifier token is defined in target. example unit_modifier@army_attack_factor

### num_units_in_combat
* description: number of units current fighting

### operation_country
* description: the country location the operative is assigned. 0 if it is not assigned to a country

### num_units_defensive_combats
* description: number of units in defensive combats

### num_units_on_climate
* description: number of units that are on an acclimatization required location, acclimatization type is defined in target. example num_units_on_climate@hot_climate

### num_units_offensive_combats
* description: number of units in offensive combats

### planning_skill_level
* description: Compares planning skill level of a unit leader.
Example: planning_skill_level > 5
* (Auto generated using the trigger with same name)

### unit_ratio_ready_for_plan
* description: ratio of units that are ready for plan

### num_units_crossing_river
* description: number of units currently passing through a river

### num_units_offensive_combats_against
* description: number of units that are offensively fighting against a terrain, terrain type is defined as target. example: num_units_offensive_combats_against@plains

### own_forced_into_hiding_time_factor
* description: The time factor applied to the status "forced into hiding". Takes into account the country it is operating for and the country it is operating against.

### skill
* description: compare leader skill levels
* (Auto generated using the trigger with same name)

### intel_yield_factor_on_capture
* description: Rate at which intel is extracted from this operative by an enemy country.

### operative_captor
* description: returns the country tag that captured the operative

### logistics_skill_level
* description: Compares logistics skill level of a unit leader.
Example: logistics_skill_level > 5
* (Auto generated using the trigger with same name)

