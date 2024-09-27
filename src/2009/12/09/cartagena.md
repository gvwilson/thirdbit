---
title: "Cartagena"
date: 2009-12-09
---
A student was in my office looking for a little AI project today.  After a bit of discussion, she's going to try to write some agents for <em>Cartagena</em>, one of my favorite little games for 2-4 players.  If you haven't run into it, here are the rules we use:

<strong>Materials</strong>
<ol>
  <li>A deck of playing cards.</li>
  <li>Four tokens per player, such as coins or poker chips.</li>
</ol>
<strong>Setup</strong>
<ol>
  <li>Divide a deck of cards in two: Jacks, Queens, Kings, and Aces go in one pile, 2-10 in the other.</li>
  <li>Shuffle the first pile and lay the cards out in a straight line to create a racetrack with 16 spaces.</li>
  <li>Shuffle the second pile.  Deal each player three cards, and put the rest face-down as the draw pile.</li>
  <li>Place every player's tokens at one end of the racetrack.</li>
</ol>
<strong>Basic Play</strong>
<ol>
  <li>The first player to get all of their tokens off the end of the racetrack is the winner.</li>
  <li>Players move in turn. In each turn, a can either spend a card to move a token forward, or move a token backward to pick up one or two new cards.</li>
  <li>To move a token forward, play a card, and move a token to the next empty card on the racetrack that is of the same suit.  For example, if the card played is a Heart, move one token to the next empty Heart card.</li>
  <li>To pick up more cards, move one token backward to the closest <em>occupied</em> card.  If that card already has one token on it, pick up one card.  If it has two tokens, pick up two cards.  If three or more tokens are already on it, you cannot move back to it (i.e., you can never put more than three tokens on a card). You cannot back up over a card that already has three tokens on it.</li>
  <li>When the draw pile is exhausted, shuffle the discard pile to create a new one.</li>
</ol>
<strong>Example</strong>

At the start of Green's turn, the board looks like this:
<table class="centered">
<tbody>
<tr>
<td rowspan="3">
<img src="@root/files/2009/12/green.gif" alt="green" width="20" height="15" class="centered">
<img src="@root/files/2009/12/purple.gif" alt="purple" width="20" height="15" class="centered">
<img src="@root/files/2009/12/purple.gif" alt="purple" width="20" height="15" class="centered">
<img src="@root/files/2009/12/red.gif" alt="red" width="20" height="15" class="centered"></td>
<td>♠</td>
<td>♣</td>
<td>♦</td>
<td>♣</td>
<td>♣</td>
<td>♠</td>
<td>♥</td>
<td>♥</td>
<td>♣</td>
<td>♠</td>
<td>♦</td>
<td>♦</td>
<td>♠</td>
<td>♥</td>
<td>♦</td>
<td>♥</td>
<td rowspan="3"></td>
</tr>
<tr>
<td></td>
<td></td>
<td><img src="@root/files/2009/12/green.gif" alt="green" width="20" height="15" class="centered">
<img src="@root/files/2009/12/red.gif" alt="red" width="20" height="15" class="centered"></td>
<td><img src="@root/files/2009/12/purple.gif" alt="purple" width="20" height="15" class="centered"></td>
<td><img src="@root/files/2009/12/red.gif" alt="red" width="20" height="15" class="centered"></td>
<td></td>
<td></td>
<td></td>
<td><img src="@root/files/2009/12/green.gif" alt="green" width="20" height="15" class="centered">
<img src="@root/files/2009/12/purple.gif" alt="purple" width="20" height="15" class="centered">
<img src="@root/files/2009/12/red.gif" alt="red" width="20" height="15" class="centered"></td>
<td></td>
<td><img src="@root/files/2009/12/green.gif" alt="green" width="20" height="15" class="centered"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>14</td>
<td>15</td>
<td>16</td>
</tr>
</tbody></table>
She holds ♦ and ♣.  Her legal actions are:
<ol>
  <li>Play ♦ and move the off-board token to [12] (the first empty ♦ space).</li>
  <li>Play ♦ and move her token from [3] to [12].</li>
  <li>Play ♦ and move [9] to [12].</li>
  <li>Play ♦ and move [11] to [12].</li>
  <li>Play ♣ and move the off-board token to [2].</li>
  <li>Play ♣ and move that token from [3] off the board, since there are no unoccupied ♣ spaces between it and the end. Another way to think about this is that the end of the racetrack effectively has all suits, i.e., can always be moved to.</li>
  <li>Play ♣ and move [9] off the board.</li>
  <li>Play ♣ and move [11] off the board.</li>
  <li>Move [9] to [5] and pick up a card.</li>
</ol>
Note that she <em>cannot</em> move [11] to [9], since there are already three tokens on [9]. She also cannot move [11] back to [5] or another earlier space, since players cannot back up past spaces that have three tokens.

<strong>Advanced Play</strong>

The board game <a href="http://en.wikipedia.org/wiki/Cartagena_%28board_game%29"><em>Cartagena</em></a>, designed by Leo Colovini, is more complicated in two ways:
<ol>
  <li>Each play has six tokens, and the racetrack has 36 spaces (six spaces of six different types).  The movement deck also obviously has six types of cards.</li>
  <li>Each player gets to perform up to three consecutive actions in each turn.  For example, a player could discard a card to move one token forward, move that same token back to pick up a card, then play the card just picked up to move forward again.  This means that a player's available actions may change during a single turn.</li>
</ol>
