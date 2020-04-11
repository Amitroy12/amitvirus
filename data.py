import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjA0MDQ3Nzg4OTg0MjM4MDgy.XToRkw.AevUJRfcN59MiVKKwzf4LiC8V4s'
self_bot_token = 'NTk3OTY2MTI1NzM2NjU2OTA2.XTnbng.O4W_i-O7rxKp80SFwv4E7BlpbF8'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '603342746480279553')

input_hq_private  = [
    "595639769904447502",
    "535675285211971584",
    "446448437119025154",
	    "570794448808837131",
	    "591600106818633729",
	    "590109407950667776",
	    "595639769904447502",
	    "590224806256050196",
	    "590182835948879872",
	    "570257859850272788",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "603342746480279553", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['603342746480279553']
command_channel = '603342746480279553' #trivia-answers
admin_chat = '603342746480279553' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
