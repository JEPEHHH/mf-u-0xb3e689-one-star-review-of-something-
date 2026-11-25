# Candidate exploration — One-Star Review of Something Essential

Goal: one single-line, deadpan one-star review (max 160 characters, no line break,
not only whitespace) of an everyday essential, written to `/output/entry.txt` by
`main.py`. The house judge compares two reviews at a time on five criteria, most
important first:

1. Is it a one-star review of an everyday essential, deadpan, unmistakably about the
   thing itself.
2. Does it find the sharpest true grievance — the small daily annoyance everyone
   recognises but has never seen written down.
3. Does it hold the deadpan: one star, no winking, no explaining the joke, no
   exclamation marks doing the work.
4. Does it turn in the last few words, so the sting lands after the complaint has been
   read straight.
5. Is it tight and specific: one joke told cleanly, no filler, no second joke crowding
   the first.

## Candidates

| # | Essential | Text | Read |
|---|-----------|------|------|
| 1 | sleep | One star for sleep. Eight hours a night for my whole life and the only thing I get back is not being tired. | Complaint read straight (a third of life gone), turn in the last words (the return is only the absence of tiredness). |
| 2 | sleep | One star for sleep. I do it every night without fail and have never once watched it work. | Deadpan, but "watched it work" is a wink at the idea rather than a grievance. |
| 3 | water | One star for water. Free, everywhere, and I still have to remember to use it or I die. | Sharp, but "or I die" explains the joke and breaks the deadpan. |
| 4 | gravity | One star for gravity. Always on, never a day off, and everything I set down ends up on the floor. | Good grievance, but "on the floor" is the obvious gag, no real turn. |
| 5 | the sun | One star for the sun. It gets up before me every day and has never once had somewhere to be. | Clean turn, but the grievance is thin — nobody resents the sun for rising. |
| 6 | oxygen | One star for oxygen. Free sample every few seconds and I still cannot get it out of my lungs. | Muddy: the image fights the grievance. |
| 7 | Monday | One star for Monday. It has never once been a day off and it still shows up every week. | Fine, but "Monday" is the default pick and the pool is full of it. |

## Pairwise comparison

- **1 vs 2** (both sleep): 1 wins on criterion 2. #2 states a fact about not observing
  your own sleep; #1 names the quiet grievance — you pay a third of your life for a
  benefit you can only feel as its absence. 1 wins.
- **1 vs 3** (sleep vs water): 3 wins criterion 2 narrowly but loses criterion 3 hard
  ("or I die" explains itself). The first criterion they differ on where 3 leads is 3,
  and 1 wins there. 1 wins.
- **1 vs 4** (sleep vs gravity): 4 wins nothing on 1 or 2; on criterion 4, 1 has a real
  turn (the return is only "not being tired") and 4 has none. 1 wins.
- **1 vs 5** (sleep vs sun): 5 is funny, but 1 wins criterion 2 (a sharper, less
  universal-aphorism grievance) and criterion 5 (tighter, one joke). 1 wins.
- **1 vs 6, 1 vs 7**: 1 wins criterion 2 and 5 in both.

## Choice

**#1 — `One star for sleep. Eight hours a night for my whole life and the only thing I
get back is not being tired.`**

Why it holds up under the brief:

- It is unmistakably a one-star review of an everyday essential: it opens "One star for
  sleep." so the judge never has to guess the genre or the target.
- The grievance is true and rarely written down: sleep is the one essential whose entire
  return is invisible. You can't see the repair, only the missing tiredness.
- It stays deadpan: no winking, no explanation, no exclamation marks, no second joke.
- It turns in the last few words: after "Eight hours a night for my whole life" reads as
  a complaint about something large, "the only thing I get back is not being tired."
  lands the anticlimax.
- It is tight and specific (under 110 characters, one joke), which also keeps the byte
  count low for the leaderboard's size tie-break.

The chosen text is the single source of truth in `main.py` (`REVIEW`), and
`tests/test_entry.py` asserts it against the competition's gate.
