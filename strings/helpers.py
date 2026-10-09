# 👑 Owner : Rich Yui
HELP_1 = """<b><u>⊚ admin commands:</b></u>

Just add <b>c</b> in the starting of the commands to use them for channel.

/pause : pause the current playing stream.

/resume : resume the paused stream.

/skip : skip the current playing stream and start streaming the next track in queue.

/end or /stop : clears the queue and end the current playing stream.

/queue : shows the queued tracks list.

/loop [Disable/enable] or [Between 1:10] 
: when activated bot will play the current playing stream in loop for 10 times or the number of requested loops.

/shuffle : shuffle the queued tracks.

/seek : seek the stream to the given duration.

/seekback : backward seek the stream to the the given duration.

/speed or /playback : for adjusting the audio playback speed in group.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_2 = """
<b><u>⊚ auth users :</b></u>

** Auth users can use admin rights in the bot without admin rights in the chat.**

/auth [Username/user_ID] : add a user to auth list of the bot.

/unauth [Username/user_ID] : remove a auth users from the auth users list.

/authusers : shows the list of auth users of the group.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_3 = """
<u><b>⊚ broadcast feature</b></u> [Only for sudoers] :

/broadcast [Message or reply to a message] : broadcast a message to served chats of the bot.

<b><u> Broadcasting modes :</u></b>

<b>-pin</b> : pins your broadcasted messages in served chats.

<b>-pinloud</b> : pins your broadcasted message in served chats and send notification to the members.

<b>-user</b> : broadcasts the message to the users who have started your bot.

<b>-assistant</b> : broadcast your message from the assitant account of the bot.

<b>-nobot</b> : forces the bot to not broadcast the message.

**⊚ example :-** 
```
/broadcast -user -assistant -pin testing broadcast
```
**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_4 = """<u><b>⊚ blacklist feature:</b></u> [Only for sudoers]

<b> Restrict shit chats to use our precious bot.</b>

/blacklistchat [Chat ID] : blacklist a chat from using the bot.

/whitelistchat [Chat ID] : whitelist the blacklisted chat.

/blacklistedchat : shows the list of blacklisted chats.

<u><b>⊚ block users :</b></u> [Only for sudoers]

<b> Starts ignoring the blacklisted user, so that he can't use bot commands.</b>

/block [Username or reply to a user] : block the user from our bot.

/unblock [Username or reply to a user] : unblocks the blocked user.

/blockedusers : shows the list of blocked users.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_5 = """
<u><b>⊚ play commands :</b></u>

<b>v :</b> stands for video play.
<b>force :</b> stands for force play.

/play or /vplay : starts streaming the requested track on videochat.

/playforce or /vplayforce : stops the ongoing stream and starts streaming the requested tra

<u><b>⊚ channel play commands:</b></u>

<b> You can stream audio/video in channel.</b>

/cplay : starts streaming the requested audio track on channel's videochat.

/cvplay : starts streaming the requested video track on channel's videochat.

/cplayforce or /cvplayforce : stops the ongoing stream and starts streaming the requested track.

/channelplay [Chat username or ID] or [Disable] : connect channel to a group and starts streaming tracks by the help of commands sent in group.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_6 = """
<u><b>⊚ global ban feature</b></u> [Only for sudoers] :

/gban [Username or reply to a user] : globally bans the chutiya from all the served chats and blacklist him from using the bot.

/ungban [Username or reply to a user] : globally unbans the globally banned user.

/gbannedusers : shows the list of globally banned users.

**⊚ created by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_7 = """
<b><u>⊚ help for active videochats</u></b> [Only for sudoers] :

** Active videochats :**

/activevoice : shows the list of active voicechats on the bot.

/activevideo : shows the list of active videochats on bot.

/ac : shows the list of both by bot.

/autoend [Enable|disable] : enable stream auto end if no one is listening.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_8 = """
<u><b>⊚ maintenance mode</b></u> [Only for sudoers] :

/logs : get logs of the bot.

/logger [Enable/disable] : bot will start logging the activities happen on bot.

/maintenance [Enable/disable] : enable or disable the maintenance mode of your bot.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""

HELP_9 = """
<b><u>⊚ some basic commands :</b></u>

/start : starts the music bot.

/help : get help menu with explanation of commands.

/ping : shows the ping and system stats of the bot.

/reboot : reboots the bot for your chat.

/settings : shows the group settings with an interactive inline menu.

/privacy : show our bot privacy.

/sudolist : shows the Sudo users of music bot.

/restart : restart bot agiain only owner & Sudo users.

/stats : shows the overall stats of the bot.

**⊚ powered by :- [Kirti bots](https://t.me/kriti_update)**
"""




HELP_10 = """
<b><u>⊚ playlist commands :</u></b>

/playlist : show your playlists.
/newplaylist [Name] : create a new playlist.
/addplaylist [Name] : add a song to a playlist.
/delplaylist [Name] : delete a playlist.
/playplaylist [Name] : play a playlist.
/addfav : add song to favourites.
/favs : show your favourites.
/playfav : play your favourites.
/playlist help : more details.
"""

HELP_11 = HELP_8 + "\n" + HELP_6
