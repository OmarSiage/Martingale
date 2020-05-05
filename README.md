<h1> Martingale (Betting Sytem)  Simulation </h1>
*Built using Streamlit


<h3> What is Martingale : </h3>
<p> Martingale is a very simple betting strategy. It's currently heavily applied to roulette by many, but it's also applied in just about any game which has odds near 50% of winning. </p>

<br>

<p> The strategy is as follows : You'll place some initial bet x, if you were to lose your bet, you'll double the previous bet to make up for the loss. You'll continue doubling for every loss that occurs in a row, until you win. Once you win your bet, you've profited your initial bet x and start over at that value. </p> 

<br><br>


<h3> Example with numbers : </h3> 
*Chris is playing roulette with 500$. The minimum bet is 10$ and the maximum bet is 1000$. He decides to always bet on black. 

<b>Spin 1</b> :  <br>
<b>His bet</b> : 10$ <br>
<b>The outcome</b> : Red <br>
<b>His net gain </b> : -10$ <br>
<b>His balance </b> : 490$ <br>

*Since he lost the previous bet, he'll double his bet to make up for the loss

<b>Spin 2</b> :  <br>
<b>His bet</b> : 20$ <br>
<b>The outcome</b> : Green <br>
<b>His net gain </b> : -30$ <br>
<b>His balance </b> : 470$ <br>

*Since he lost the previous bet, he'll double his bet to make up for the loss
His current loss is currently at 30$
But betting only 30$ will only break him even if he were to win, so he adds his initial bet of 10$ 
Totaling his bet now at 40$

<b>Spin 3</b> : <br>
<b>His bet</b> : 40$  <br>
<b>The outcome</b> : Red  <br>
<b>His net gain </b> : -70$ <br>
<b>His balance </b> : 430$ <br>


*Doubling his previous bet, will force him now to bet 140$

<b>Spin 4</b> : <br>
<b>His bet</b> : 80$ <br>
<b>The outcome</b> : Black <br>
<b>His net gain </b> : +10$ <br>
<b>His balance </b> : 510$ <br>

After a stressful 4 spins, we was finally able to turn a profit of 10$. 

As you can see using this method causes your bet to increase drastically. It can be mathematically expressed as the following :

<em> current_bet = (2)^(consecutif_loss_count) * (inital_bet) </em>

An exponential function. Which if you were to get unlucky, after 10 consecutif losses, using an initial bet of 10$, you'll have to bet 10,240$ to make up for all your previous loss! QUITE a scary amount to gamble for just a 10$ gain.

I've already saw the math and using any finite sum of money and assuming no cap on the table, the expectation = 0$. The odds are on your side when making a small lump on money, but there's also a small chance to lose a disastrous amount and this will eventually even out to nothing gained.

So what's the point? I'm curious. I'll be taking into account real minimum/maximum table bets, initial bet amd gain desired and running thousands of simulations, graphing them and seeing the results.

