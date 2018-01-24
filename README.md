# README
**S.M.I.T.H.E.R.S.** is a Specialized Modern Interface To Help Evaluate Roll Successes. It is a collaboration project to create a discord bot for discord to assist with traditional pen and paper RPGs.

## Commands
__Commands must be preceded by a `!` to be recognized by SMITHERS.__

### !ping
Pong

### !pong
Ping

### !roll [NdN=1d20]

Rolls NdN dice


### !roll2 [NdN=1d20] [args...]

Test command for new dice roll functions
-----
roll - Rolls 1d20
roll adv/advantage - Rolls 2d20 and drops the lowest
roll dis/disadv/disadvantage - Rolls 2d20 and drops the highest
roll XdY - Rolls X Y-sided die
roll... + X - Adds X to the final dice roll
roll... - X - Subtracts X from the final dice roll
roll... d/dl X - Drops the lowest X dice rolls
roll... dh X - Drops the highest X dice rolls

Untested so far, and incredibly verbose. Good luck everybody!
TODO - Condense each modifier into one argument, vice a pair.